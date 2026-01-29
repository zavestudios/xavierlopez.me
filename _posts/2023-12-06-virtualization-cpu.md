---
title: "Virtualization and CPU: vCPU, Scheduling, and Overcommitment"
date: 2023-12-06 10:51:00 +0000
last_modified_at: "2025-02-19"
categories: [devops]
excerpt: "A platform engineer’s guide to how CPUs are virtualized, how vCPUs are scheduled, and why CPU overcommitment usually works—until it doesn’t."
toc: true
toc_sticky: true
layout: single
---

## Context

CPU issues in virtualized environments rarely show up as clean failures.

Instead, they appear as:

- intermittent latency,
- unpredictable performance,
- noisy-neighbor behavior,
- or workloads that “just feel slow.”

To reason about these problems, platform engineers need to understand how **physical CPUs**, **vCPUs**, and **hypervisor schedulers** actually interact.

---

## Physical CPU vs vCPU

### Physical CPU

The **CPU (Central Processing Unit)** is the physical hardware responsible for executing instructions.

It provides:

- cores
- threads
- cache
- instruction pipelines

These are finite, shared resources.

---

### vCPU (Virtual CPU)

A **vCPU** is a **software abstraction** created by the hypervisor.

Key characteristics:

- Represents a *share* of a physical CPU core
- Is scheduled by the hypervisor
- Is not permanently tied to a single physical core

From inside a VM, a vCPU looks like a real CPU. In reality, it is **time-sliced** alongside other vCPUs.

---

## The Relationship Between CPU and vCPU

- Multiple vCPUs can map to the same physical core
- A single VM can have many vCPUs
- Hypervisors schedule vCPUs dynamically based on demand

### Example: CPU Overcommitment

- Physical host: 4 cores
- Three VMs, each with 2 vCPUs
- Total vCPUs: 6

This is **intentional overcommitment**.

It works because:

- Most workloads are not CPU-bound all the time
- Hypervisors are efficient at scheduling short CPU bursts

---

## CPU Scheduling (Where the Magic—and Pain—Happens)

Hypervisors:

- track runnable vCPUs
- allocate CPU time slices
- attempt fairness and efficiency

Problems arise when:

- too many vCPUs want CPU at the same time
- latency-sensitive workloads are mixed with batch jobs
- monitoring focuses only on averages

From a platform perspective, **CPU contention is often invisible until it’s severe**.

---

## Overcommitment: Powerful but Dangerous

### Why Overcommitment Exists

Overcommitment enables:

- higher utilization
- better cost efficiency
- fewer idle resources

Most environments rely on it.

---

### When Overcommitment Becomes a Problem

- sustained CPU saturation
- high ready time / run-queue depth
- latency spikes under load
- “everything slows down” symptoms

This is where platform engineers earn their keep.

---

## Virtualization Side Effects That Matter

### Noisy Neighbor Effects

When multiple VMs:

- share the same physical CPU
- peak simultaneously

Performance degrades in non-obvious ways.

---

### Troubleshooting Complexity

Virtualization introduces layers:

- application
- guest OS
- hypervisor
- physical hardware

CPU issues may originate **below the VM**, even if symptoms appear inside it.

---

## In Practice: Platform Engineering Examples

### Kubernetes

- Nodes are usually VMs
- Pods compete for vCPU time indirectly
- CPU limits and requests interact with hypervisor scheduling

When pods throttle unexpectedly, the problem may be:

- node-level CPU contention
- host overcommitment
- scheduler fairness, not Kubernetes itself

---

### CI/CD and Build Workloads

- Short, CPU-intensive jobs
- Bursty demand
- Often co-located with steady services

This combination amplifies scheduling issues.

---

## Observability Signals to Watch

- CPU ready / steal time
- sustained high load averages
- latency under moderate utilization
- uneven performance across identical VMs

These signals usually matter more than raw CPU percentages.

---

## Takeaways

- vCPUs are abstractions, not guarantees
- Overcommitment is normal—and necessary
- CPU contention often manifests as latency, not failure
- Platform engineers need visibility below the guest OS
- When performance feels “weird,” think scheduler first

If virtualization is the abstraction layer beneath your platform, CPU scheduling is where that abstraction is most likely to leak.
