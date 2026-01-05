---
layout: single
title: "Installing the NFS Subdir External Provisioner with Helm"
date: 2024-02-26 08:00:00 +0000
last_modified_at: "2025-01-08"
categories:
  - kubernetes
  - storage
  - platform
tags:
  - kubernetes
  - helm
  - nfs
  - storageclass
  - persistent-volumes
excerpt: "How to install and reason about the NFS Subdir External Provisioner using Helm, enabling dynamic NFS-backed Persistent Volumes in Kubernetes."
toc: true
toc_sticky: true
---

## Context

Understanding how Kubernetes storage works is one thing.  
Actually **enabling** that capability in a cluster is another.

If you want dynamic NFS-backed Persistent Volumes, Kubernetes needs a component that can:

- watch for PersistentVolumeClaims
- create directories on an NFS server
- register those directories as PersistentVolumes

That component is the **NFS Subdir External Provisioner**.

This post focuses on installing it intentionally using Helm—and understanding what you’re enabling when you do.

---

## What This Provisioner Does

The NFS Subdir External Provisioner:

- runs as a pod in your cluster
- listens for PVCs referencing its StorageClass
- creates subdirectories on an external NFS server
- dynamically provisions PersistentVolumes

Kubernetes itself does **not** talk to NFS directly.  
This provisioner is the bridge.

---

## Prerequisites

Before installing anything, you need:

- a reachable NFS server
- an exported directory writable by the provisioner
- network connectivity from cluster nodes to the NFS server
- Helm installed and configured

If the NFS server isn’t healthy, this installation will succeed—but provisioning will not.

---

## Adding the Helm Repository

First, add the Helm repository that hosts the chart:

```
helm repo add nfs-subdir-external-provisioner \
  https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/

helm repo update
```

This makes the chart available locally.

---

## Installing the Provisioner

The core installation uses `helm install` with a small but important set of values.

Example:

```
helm install nfs-provisioner \
  nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
  --namespace storage-system \
  --create-namespace \
  --set nfs.server=192.0.2.50 \
  --set nfs.path=/exports/kubernetes \
  --set storageClass.name=managed-nfs
```

Key values explained:

- `nfs.server`  

  Address of the external NFS server

- `nfs.path`  

  Base directory where subdirectories will be created

- `storageClass.name`  

  The StorageClass PVCs will reference

This command installs the provisioner and registers a new StorageClass.

---

## What Helm Is Actually Creating

After installation, you should see:

- a Deployment running the provisioner
- a Pod connected to the NFS server
- a StorageClass pointing to this provisioner

Helm handles object creation, but **you are responsible** for understanding the consequences.

---

## Verifying the Installation

Check that the pod is running:

```
kubectl get pods -n storage-system
```

Confirm the StorageClass exists:

```
kubectl get storageclass
```

You should see the `managed-nfs` StorageClass listed.

---

## Validating Dynamic Provisioning

Create a simple PVC referencing the StorageClass:

```
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-nfs-claim
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: managed-nfs
  resources:
    requests:
      storage: 1Gi
EOF
```

If provisioning works:

- a PersistentVolume will be created automatically
- a new directory will appear on the NFS server
- the PVC will bind successfully

This confirms end-to-end functionality.

If the reported size appears smaller than expected, this is often a unit conversion issue rather than a provisioning failure.  
See: [Understanding Byte Size Units (Without Overthinking Them)](/2024/02/28/understanding-byte-size-units/)

---

## Common Failure Modes

If things don’t work, check:

- NFS server permissions
- firewall rules
- pod logs for the provisioner
- correctness of `nfs.server` and `nfs.path`
- whether the StorageClass name matches the PVC

Most failures are external to Kubernetes.

---

## When This Is (and Isn’t) the Right Choice

This approach works well for:

- shared storage
- development clusters
- on-prem environments
- workloads needing `ReadWriteMany`

It may not be appropriate for:

- high-performance databases
- latency-sensitive workloads
- cloud-native block storage replacements

NFS is a tool, not a default.

---

## How This Fits the Bigger Picture

This installation enables the architecture described in:

> *How NFS-Backed Persistent Volumes Actually Work in Kubernetes*

Understanding the model first makes this step predictable instead of magical.

Helm just applies the intent—you still own the system.
