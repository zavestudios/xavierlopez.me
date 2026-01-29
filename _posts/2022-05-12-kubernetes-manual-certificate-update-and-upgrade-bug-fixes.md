---
layout: single
title: "Kubernetes Manual Certificate Updates and Upgrade Bug Fixes"
date: 2022-05-12 08:40:00 +0000
last_modified_at: "2025-02-27"
categories:
  - devops
  - devops
  - security
excerpt: "How to manually update Kubernetes certificates, why certificate issues often surface during upgrades, and how to safely recover clusters when automation falls short."
toc: true
toc_sticky: true
---

## Context

Kubernetes certificate problems rarely appear during calm periods.

They surface during:

- control plane upgrades
- node replacements
- API server restarts
- long-lived clusters reaching certificate expiration

When certificate automation fails—or was never fully implemented—operators are left performing **manual recovery on critical infrastructure**.

This post documents how and why manual certificate updates become necessary, and how to approach them safely.

---

## Why Kubernetes Certificates Matter

Kubernetes relies heavily on **mutual TLS**.

Certificates secure:

- API server communication
- kubelet authentication
- controller-manager and scheduler access
- etcd traffic
- kubectl client access

If certificates expire or mismatch, the cluster doesn’t degrade gracefully—it stops working.

---

## Common Triggers for Manual Intervention

Manual certificate updates are often required when:

- clusters run longer than expected without rotation
- upgrades expose latent certificate drift
- bootstrap tools were misconfigured
- control plane nodes were restored from snapshots
- time skew invalidates certificates

In many cases, the problem existed long before symptoms appeared.

---

## Understanding the Certificate Landscape

Key certificate locations typically include:

- `/etc/kubernetes/pki`
- kubeconfig files under `/etc/kubernetes`
- embedded certificates inside kubeconfigs

Each component may rely on different certificates with different lifetimes.

Blind rotation is dangerous without understanding dependencies.

---

## Checking Certificate Expiration

On clusters bootstrapped with `kubeadm`, start with:

```bash
kubeadm certs check-expiration
```

This provides a clear overview of:

- which certificates are expired
- which are approaching expiration
- which components are affected

If this command fails, you’re already in partial outage territory.

---

## Renewing Certificates with kubeadm

When possible, prefer kubeadm-managed renewal:

```bash
kubeadm certs renew all
```

This regenerates control plane certificates but does **not** automatically restart components.

After renewal, you must restart:

- kube-apiserver
- kube-controller-manager
- kube-scheduler
- kubelet (in some cases)

Plan for controlled restarts.

---

## Updating kubeconfig Files

Renewing certificates is only half the job.

kubeconfig files often embed client certificates that must be updated:

- `admin.conf`
- `controller-manager.conf`
- `scheduler.conf`
- `kubelet.conf`

Regenerate them as needed:

```bash
kubeadm init phase kubeconfig all
```

Then copy updated configs to their expected locations.

---

## Restarting Control Plane Components

After certificate and kubeconfig updates:

- restart static pods (usually via kubelet restart)
- confirm API server health
- verify component logs

A certificate update without restarts leaves the cluster in a broken half-state.

---

## Upgrade-Related Certificate Bugs

Upgrades sometimes surface certificate bugs such as:

- mismatched CA bundles
- outdated kubeconfigs
- components referencing old cert paths
- control plane components failing silently

These issues often appear as:

- API server refusing connections
- kubelet registration failures
- controllers stuck in crash loops

Treat upgrades as stress tests for certificate hygiene.

---

## Debugging Tips

When diagnosing certificate-related failures:

- check system time on all nodes
- inspect logs for TLS errors
- verify file permissions under `/etc/kubernetes/pki`
- ensure components reference the correct kubeconfigs

Certificate errors are usually explicit—once you know where to look.

---

## When Manual Rotation Is Unsafe

Avoid manual rotation when:

- etcd health is unknown
- backups are unavailable
- cluster state is already inconsistent

In these cases, recovery planning is more important than speed.

---

## Preventing Future Issues

Long-term fixes include:

- enabling automatic rotation
- monitoring certificate expiration proactively
- documenting bootstrap procedures
- testing upgrades in long-lived environments

Manual intervention should be a last resort, not a routine operation.

---

## Takeaways

- Certificate issues often surface during upgrades
- Kubernetes depends heavily on PKI correctness
- kubeadm provides tooling—but requires operator follow-through
- kubeconfigs are as important as certificates themselves
- Proactive rotation and monitoring prevent emergencies

When Kubernetes certificates fail, the cluster doesn’t limp—it stops.  
Understanding manual recovery is essential for anyone operating long-lived clusters.
