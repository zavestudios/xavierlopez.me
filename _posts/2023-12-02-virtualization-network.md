---
layout: single
title: "Virtualization – Network"
date: 2023-12-03 11:00:00 +0000
last_modified_at: "2025-01-07"
categories:
  - devops
  - networking
excerpt: "An overview of how networking works in virtualized environments, what gets abstracted, and why troubleshooting virtual networks is often harder than physical ones."
toc: true
toc_sticky: true
---

## Context

Networking is one of the first areas where virtualization **breaks intuition**.

Packets still flow, IP addresses still exist, and protocols still behave the same — but the **path a packet takes** is no longer obvious. Once networking is virtualized, traffic may traverse multiple software layers before ever touching a physical wire.

This post explains what changes when networks are virtualized, what stays the same, and where engineers typically get tripped up.

---

## What Is Virtualized Networking?

In a virtualized environment, networking is **implemented in software** rather than directly on physical switches and NICs.

At a high level:

- Virtual machines connect to **virtual network interfaces**
- These interfaces attach to **virtual switches**
- Virtual switches map traffic onto **physical network interfaces**

The result is a software-defined network path that *looks* simple from inside a VM, but is layered underneath.

---

## Core Components

### Virtual Network Interface (vNIC)

Each VM is assigned one or more **virtual NICs**.

From inside the guest OS:

- the vNIC appears like a normal network card
- it has a MAC address
- it participates in IP networking normally

The guest is unaware that the NIC is virtual.

---

### Virtual Switch

A **virtual switch** exists inside the hypervisor.

Its responsibilities include:

- switching traffic between VMs on the same host
- enforcing VLANs or port groups
- forwarding traffic to physical NICs

From a networking perspective, a virtual switch behaves much like a physical Layer 2 switch — except it’s implemented entirely in software.

---

### Physical Network Interface

Eventually, traffic must leave the host.

The hypervisor maps virtual switch traffic onto one or more **physical NICs**, which connect to the real network.

This is where:

- bandwidth becomes shared
- congestion becomes possible
- performance characteristics change

---

## The Virtual Network Path

A simplified packet journey looks like this:

1. Application inside the VM sends traffic
2. Packet exits via the VM’s vNIC
3. Packet enters the virtual switch
4. Virtual switch applies policies (VLANs, filtering, forwarding)
5. Packet exits through a physical NIC
6. Packet enters the physical network

Each step adds flexibility — and complexity.

---

## Overcommitment and Shared I/O

Just like CPU and memory, **network I/O is shared**.

Multiple VMs may:

- share the same virtual switch
- compete for the same physical NIC
- burst traffic simultaneously

This leads to:

- unpredictable latency
- noisy-neighbor effects
- contention that’s invisible from inside a VM

From the guest’s point of view, “the network is slow” — even when nothing looks wrong internally.

---

## Why Troubleshooting Gets Harder

Virtualization inserts layers:

- application
- guest OS networking
- virtual NIC
- virtual switch
- hypervisor
- physical NIC
- physical switch

A failure or bottleneck in *any* layer can look identical from the VM.

Common pain points:

- packet loss without interface errors
- latency spikes without CPU saturation
- traffic blocked by virtual policy, not physical ACLs

The abstraction that makes virtualization powerful also obscures root cause.

---

## Virtual I/O and Abstraction

Virtualized networking is part of a broader **virtual I/O model**, which includes:

- virtual ethernet
- virtual storage paths
- abstracted hardware access

The VM does not interact with hardware directly. Instead, the hypervisor mediates all I/O, enabling:

- portability
- isolation
- hardware independence

But mediation always has a cost.

---

## In Practice

Virtual networking enables:

- rapid provisioning
- flexible topology changes
- software-defined segmentation

It also demands:

- good observability
- awareness of host-level constraints
- discipline when troubleshooting

When diagnosing network issues in virtualized systems, engineers must think **below the guest OS**, not just inside it.

---

## Takeaways

- Virtual networking is real networking, implemented in software
- Virtual switches behave like physical switches, but with different failure modes
- Network I/O is shared and overcommitted
- Abstraction improves flexibility but complicates troubleshooting
- When performance feels “mysterious,” inspect the virtualization layer

Understanding the virtual network path is essential for diagnosing modern systems — especially when nothing appears broken, yet everything feels slow.
