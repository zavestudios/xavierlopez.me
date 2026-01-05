---
title: "Network Concepts for Platform Engineers"
date: 2023-12-08 23:45:00 +0000
last_modified_at: "2025-09-10"
categories: [linux, networking]
tags: [osi, layer2, layer3, vlan, subnet, kubernetes, aws]
excerpt: "A practical refresher on Layer 2 vs Layer 3 networking, VLANs vs subnets, and how these concepts actually show up in day-to-day platform engineering work."
toc: true
toc_sticky: true
layout: single
---

## Context

If you work as a platform engineer, you rarely think in terms of “OSI layers” explicitly — until something breaks.

Traffic isn’t flowing between pods.  
A node can’t reach a service endpoint.  
Two systems *should* be isolated but somehow aren’t.

At that point, most issues collapse down to **Layer 2 vs Layer 3 boundaries** and how segmentation is being applied. This post is a focused refresher on those concepts, framed around how they actually show up in real infrastructure.

---

## Core Concepts: Layer 2 vs Layer 3

### Layer 2 — Data Link Layer

Layer 2 is concerned with **local, same-network communication**.

**Key characteristics:**

- **Scope:** One broadcast domain
- **Addressing:** MAC addresses
- **Devices:** Switches
- **Data unit:** Frames

At this layer, devices don’t care about IP addresses. If two devices are in the same Layer 2 domain, they can communicate directly using MAC addressing.

**Mental model:**  
> “Can I reach you without a router?”

If yes, you’re operating at Layer 2.

---

### Layer 3 — Network Layer

Layer 3 is responsible for **communication between different networks**.

**Key characteristics:**

- **Scope:** Multiple networks
- **Addressing:** IP addresses
- **Devices:** Routers
- **Data unit:** Packets

Layer 3 introduces routing logic — decisions about *where* traffic should go next to reach a different network.

**Mental model:**  
> “Do I need a route to reach you?”

If yes, you’re operating at Layer 3.

---

## VLANs vs Subnets (Where Confusion Usually Starts)

VLANs and subnets are often talked about interchangeably, but they solve **different problems at different layers**.

| Concept | OSI Layer | Purpose | Isolation Type |
|------|---------|--------|---------------|
| VLAN | Layer 2 | Split a physical network into logical broadcast domains | L2 isolation |
| Subnet | Layer 3 | Divide IP space into manageable routing domains | L3 isolation |

---

### VLANs (Virtual Local Area Networks)

**What they do well:**

- Segment a physical switch into multiple logical networks
- Reduce broadcast noise
- Provide Layer 2 isolation

**Important properties:**

- Devices in the same VLAN behave as if they are on the same physical network
- VLANs are identified by a **VLAN ID**
- VLAN isolation happens **before IP routing**

**Key limitation:**  
VLANs alone do *not* provide routing. Traffic between VLANs requires a Layer 3 device.

---

### Subnets

**What they do well:**

- Partition IP address space
- Define routing boundaries
- Enable policy and traffic control at Layer 3

**Important properties:**

- Devices in the same subnet can communicate directly
- Traffic between subnets *always* requires routing
- Subnets are fundamental to cloud networking (VPCs, route tables)

---

## In Practice: How This Shows Up in Platform Engineering

### Kubernetes

- **Pods** typically communicate across nodes using Layer 3 routing
- **CNIs** abstract away VLANs but still rely on routing concepts
- NetworkPolicies operate at L3/L4 (and sometimes L7)

When pod-to-pod traffic fails:

- Ask whether it’s a **routing** issue (L3)
- Or a **segmentation** issue (policy / isolation)

---

### Cloud (AWS as an Example)

- **VPCs** are Layer 3 constructs
- **Subnets** define routing domains within a VPC
- **Security Groups** and **NACLs** enforce policy on top of L3 boundaries

There are no traditional VLANs exposed — AWS hides L2 and forces you to reason in terms of routing and IP space.

---

### CI/CD and Platform Tooling

- Runners failing to reach registries?
- Pipelines timing out on internal endpoints?

These often trace back to:

- Missing routes
- Incorrect subnet placement
- Assumptions about “same network” that aren’t true

---

## Common Failure Modes

| Symptom | Likely Cause | What to Check |
|------|------------|--------------|
| Pods can’t reach each other across nodes | Routing issue | CNI config, node routes |
| Traffic works in one AZ but not another | Subnet isolation | Route tables |
| Services unexpectedly reachable | Overly flat L2/L3 design | Network policies, segmentation |
| Broadcast storms or noisy networks | Poor L2 segmentation | VLAN design (on-prem) |

---

## Takeaways

- **Layer 2 is about locality; Layer 3 is about reachability**
- VLANs segment *broadcast domains*; subnets segment *IP space*
- Cloud platforms push you to think in Layer 3 terms
- Most “mysterious” network bugs become obvious once you identify the layer involved

If you’re debugging platform networking issues, start by asking:
> “Am I crossing an L2 boundary, an L3 boundary, or both?”

That question alone eliminates a surprising amount of guesswork.
