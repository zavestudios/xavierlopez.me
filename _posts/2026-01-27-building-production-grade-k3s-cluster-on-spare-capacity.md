---
layout: single
title: "Building a Production-Grade k3s Cluster on Spare Capacity"
date: 2026-01-27 12:00:00 +0000
last_modified_at: "2026-01-27"
categories:
  - devops
tags:
  - devops
  - k3s
  - kvm
  - libvirt
  - devops
  - devops
excerpt: "I built a 3-node k3s cluster that deploys automatically in 5 minutes using Terraform and cloud-init. Here's how it works and what I learned."
toc: true
toc_sticky: true
---

## Context

I needed a Kubernetes cluster that could run continuously for platform engineering work - deploying services, testing GitOps workflows, running applications. The cluster needed to be production-grade in its automation and reliability, even if it wasn't serving production traffic.

I chose k3s running on KVM/libvirt virtual machines. The entire deployment is automated: Terraform provisions three VMs, cloud-init configures networking and installs k3s, and within about five minutes a working cluster is operational. No manual steps, no configuration drift, completely reproducible.

This post walks through the architecture, the automation decisions, and the technical solutions that make it work. If you're building Kubernetes infrastructure on virtualization platforms, some of these patterns might be useful.

## The Architecture

The cluster runs three virtual machines managed by KVM/libvirt:

- One control plane node (k3s-cp-01)
- Two worker nodes (k3s-worker-01, k3s-worker-02)

Each VM has 6 vCPUs, 10GB RAM, and 80GB disk. They run Ubuntu 24.04 LTS with the containerd runtime. The k3s version is pinned to v1.34.3+k3s1 - I'll explain why that matters later.

The network uses libvirt's default network (192.168.122.0/24) with static IP assignments:

- Control plane: 192.168.122.10
- Worker 1: 192.168.122.11
- Worker 2: 192.168.122.12

Static IPs are configured via cloud-init's network_config, not DHCP reservations. This eliminates any dependency on DHCP lease stability and ensures nodes always come up with the correct addresses.

The deployment is managed entirely through infrastructure as code. Packer builds the base Ubuntu image with k3s prerequisites. Terraform provisions the VMs using the libvirt provider. Cloud-init handles node-specific configuration and k3s installation. The entire process is declarative and reproducible.

## Automation Decisions

### Why Static IPs Instead of DHCP

The initial implementation used DHCP with MAC address reservations in libvirt's network configuration. This worked, but introduced instability. Occasionally nodes would come up with different IPs or fail to get leases at all. Debugging network issues in a distributed system is painful when you're not sure if the problem is application-level or infrastructure-level.

Static IPs configured via cloud-init eliminate this entire class of problems. Each VM's network configuration is defined in its cloud-init network_config. The IP addresses are assigned before any services start. There's no lease negotiation, no timing dependencies, no opportunity for the network layer to behave differently between deployments.

The trade-off is that you need to manage IP address allocation manually. For a three-node cluster, that's trivial. For larger deployments, you'd want tooling to generate network_config from an IP allocation database. But the reliability improvement is worth it.

### Why Pinned k3s Versions

K3s supports installing from a "stable" channel, which automatically pulls the latest stable release. This seems convenient - you always get the newest version without manual updates.

In practice, this creates deployment instability. The k3s version can change between cluster deployments, introducing variables when troubleshooting. Different nodes might end up with different versions if they pull from the channel at different times. And k3s releases sometimes introduce breaking changes that affect existing workloads.

Pinning to a specific version (v1.34.3+k3s1 in this case) makes deployments reproducible. Every node gets exactly the same k3s binary. If I destroy and recreate the cluster six months from now, it will be identical to today's deployment. When I'm ready to upgrade, I test the new version, update the pin, and deploy deliberately.

This is a standard practice in production environments. Version pinning trades convenience for predictability. For a platform that exists to demonstrate capabilities, predictability matters more than running the absolute latest release.

### Why Cloud-Init Network Validation

The k3s installation script runs automatically via cloud-init. If networking isn't fully operational when k3s starts, the installation can fail in subtle ways - certificates might be generated with wrong IPs, the API server might bind to the wrong interface, nodes might not be able to join the cluster.

The cloud-init configuration includes network validation before k3s installation:

```yaml
runcmd:
  - |
    # Wait for network interface to be operational
    for i in {1..30}; do
      IFACE=$(ip -o -4 route show to default | awk '{print $5}' | head -n1)
      if [ -n "$IFACE" ]; then
        echo "Network interface $IFACE is up"
        break
      fi
      echo "Waiting for network interface... ($i/30)"
      sleep 2
    done
    
  - |
    # Verify DNS resolution
    for i in {1..30}; do
      if nslookup google.com > /dev/null 2>&1; then
        echo "DNS resolution working"
        break
      fi
      echo "Waiting for DNS... ($i/30)"
      sleep 2
    done
    
  - |
    # Install k3s after network is confirmed operational
    curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.34.3+k3s1 sh -s - server
```

This adds maybe 10-15 seconds to deployment time, but eliminates an entire class of timing-related failures. The k3s installation doesn't start until the network is confirmed working. Simple, reliable, worth the wait.

### Why Clean Base Images

The Packer template builds a base Ubuntu 24.04 image with k3s prerequisites installed. Early versions of this image had problems: hardcoded MAC addresses from the build environment, residual netplan configurations, cloud-init state that didn't reset properly between VM deployments.

These issues caused VMs to come up with duplicate MAC addresses or incorrect network configurations. The solution was a cleanup script that runs at the end of the Packer build:

```bash
# Remove machine-specific identifiers
rm -f /etc/machine-id
rm -f /var/lib/dbus/machine-id

# Clean cloud-init state
cloud-init clean --logs --seed

# Remove netplan configs (cloud-init will regenerate)
rm -f /etc/netplan/*.yaml

# Clean logs
find /var/log -type f -delete
```

This ensures the base image is truly generic. Each VM that boots from this image gets fresh identifiers, clean cloud-init state, and network configuration from its own cloud-init data source.

## Technical Implementation

### Terraform Structure

The Terraform configuration provisions VMs using the dmacvicar/libvirt provider. For each node, it creates:

1. A cloud-init ISO that contains user_data and network_config
2. A disk volume cloned from the base image
3. A domain (VM) with the disk and cloud-init ISO attached

The libvirt provider connects to a remote libvirtd instance over SSH. This means Terraform runs on my laptop but manages VMs on a separate Linux host. The provider handles the SSH connection transparently.

Key Terraform resources:

```hcl
resource "libvirt_cloudinit_disk" "k3s_cp" {
  name           = "k3s-cp-01-cloudinit.iso"
  user_data      = templatefile("${path.module}/cloud-init/k3s-cp.yml.tpl", {...})
  network_config = templatefile("${path.module}/cloud-init/network-config.yml.tpl", {...})
}

resource "libvirt_volume" "k3s_cp" {
  name           = "k3s-cp-01.qcow2"
  base_volume_id = libvirt_volume.base.id
  size           = 85899345920  # 80GB
}

resource "libvirt_domain" "k3s_cp" {
  name   = "k3s-cp-01"
  memory = 10240
  vcpu   = 6
  
  cloudinit = libvirt_cloudinit_disk.k3s_cp.id
  
  disk {
    volume_id = libvirt_volume.k3s_cp.id
  }
  
  network_interface {
    network_name   = "default"
    addresses      = ["192.168.122.10"]
    wait_for_lease = false
  }
}
```

The `wait_for_lease = false` parameter is important. It tells Terraform not to wait for a DHCP lease, since we're using static IPs. Without this, Terraform would hang waiting for a lease that will never come.

### Cloud-Init Configuration

The cloud-init configuration has two parts: user_data (what to do) and network_config (how to configure networking).

The network_config is straightforward - static IP, gateway, DNS servers:

```yaml
version: 2
ethernets:
  ens3:
    addresses:
      - 192.168.122.10/24
    gateway4: 192.168.122.1
    nameservers:
      addresses:
        - 8.8.8.8
        - 1.1.1.1
```

The user_data is more complex. For the control plane:

```yaml
#cloud-config
hostname: k3s-cp-01
fqdn: k3s-cp-01.local

users:
  - name: ubuntu
    ssh_authorized_keys:
      - ${ssh_public_key}
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash

runcmd:
  # Network validation (shown earlier)
  # K3s installation
  - curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.34.3+k3s1 sh -s - server
  
  # Wait for k3s to be ready
  - |
    for i in {1..60}; do
      if sudo k3s kubectl get nodes > /dev/null 2>&1; then
        echo "k3s control plane is ready"
        break
      fi
      sleep 5
    done
```

For worker nodes, the configuration is similar but joins the cluster instead of initializing it:

```yaml
runcmd:
  # Network validation
  # K3s agent installation
  - |
    curl -sfL https://get.k3s.io | \
      INSTALL_K3S_VERSION=v1.34.3+k3s1 \
      K3S_URL=https://192.168.122.10:6443 \
      K3S_TOKEN=${k3s_token} \
      sh -s - agent
```

The k3s token comes from Terraform variables and is templated into the cloud-init configuration. In a production environment, you'd want to manage this more securely (maybe HashiCorp Vault or AWS Secrets Manager), but for a demonstration cluster, templating it directly works fine.

### Deployment Workflow

From a clean state, deploying the cluster:

```bash
# Terraform provisions VMs and attaches cloud-init
terraform apply

# Wait ~5 minutes for cloud-init to complete
# VMs boot, network configures, k3s installs

# Verify cluster is operational
ssh ubuntu@192.168.122.10 'sudo k3s kubectl get nodes -o wide'
```

The entire process takes about five minutes. Most of that is waiting for VMs to boot and cloud-init to run. The actual k3s installation is fast once the network is ready.

Destroying and recreating the cluster:

```bash
terraform destroy
terraform apply
# Another 5 minutes, identical cluster
```

Complete reproducibility. No manual steps. No configuration drift.

## What's Next

This cluster is the foundation for platform services. The next steps are:

**Install Flux GitOps controllers** to manage platform and application deployments declaratively. Flux will sync from Git repositories and keep the cluster state in sync with the desired state defined in code.

**Deploy Big Bang platform services** - the DoD-maintained DevSecOps baseline that provides Istio service mesh, Prometheus monitoring, GitLab CI/CD, and other core capabilities. This gives the cluster a production-grade platform layer.

**Add applications** - once the platform is operational, deploy actual applications to demonstrate the full stack working together.

**AWS compatibility** - This architecture is designed with Kubernetes portability in mind. The application layer uses standard Kubernetes primitives. Environment-specific infrastructure differences (storage classes, load balancers, ingress) are handled through Kustomize overlays. The same manifests and GitOps workflows that work on k3s can deploy to AWS EKS.

Future posts will cover the Flux and Big Bang deployment process, and eventually demonstrate AWS integrations using services like Direct Connect, Storage Gateway, and Outposts.

## Lessons Learned

**Static networking is worth the small amount of extra configuration.** DHCP adds moving parts and timing dependencies. For infrastructure that needs to be reliable, static IPs eliminate an entire class of problems.

**Version pinning trades convenience for predictability.** Always getting the latest version sounds good until you need to debug why a deployment behaves differently than it did last month.

**Network validation before service installation prevents subtle failures.** The 10-15 seconds spent confirming DNS works and interfaces are up saves hours of debugging certificate problems and API server binding issues.

**Clean base images are not optional.** Residual state in images causes mysterious problems that are hard to diagnose. Taking the time to properly clean machine IDs, cloud-init state, and network configs is essential.

**Automation enables experimentation.** Being able to destroy and recreate the cluster in 5 minutes means you can test ideas without fear. If something breaks, just rebuild. This changes how you approach learning and troubleshooting.

The cluster runs continuously now, stable and operational. It's ready for the platform services layer. The automation is solid enough that I trust it, which means I can focus on building the interesting parts - the platform and applications - instead of fighting infrastructure problems.
