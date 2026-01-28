---
layout: single
title: "Host Storage Management: Capacity, Performance, and Failure Modes"
date: 2023-11-29 10:43:00 +0000
last_modified_at: "2025-03-17"
categories:
  - linux
  - systems
  - storage
tags:
  - storage
  - capacity-planning
  - filesystems
  - operations
  - troubleshooting
excerpt: "A practical guide to managing host-level storage, focusing on capacity, performance characteristics, and the failure modes engineers actually encounter in production."
toc: true
toc_sticky: true
---

## Context

Host storage problems rarely announce themselves loudly.

More often, they surface as:

- gradual performance degradation
- unrelated services failing mysteriously
- nodes becoming unstable
- alerts that don’t clearly point to disk

This post focuses on **host-level storage management**—what actually matters when you’re responsible for keeping systems running, whether on bare metal, virtual machines, or cluster nodes.

---

## What “Host Storage” Really Includes

At the host level, storage is a stack of layers:

- physical disks (HDD, SSD, NVMe)
- device abstraction (RAID, device-mapper)
- logical volumes (LVM)
- filesystems
- mount points
- swap
- ephemeral vs persistent data

Most real failures happen **between layers**, not inside a single one.

---

## Capacity Management (The Quiet Risk)

### Disk Space vs Inodes

Running out of disk space is obvious.  
Running out of **inodes** is not.

Always check both:

```bash
df -h
df -i
```

You can have plenty of free space and still be unable to create files.

---

### Growth Is Usually Predictable

Common sources of silent growth:

- application logs
- metrics and traces
- caches
- temporary files
- crash dumps

The pattern is almost always:
> slow → steady → ignored → catastrophic

Capacity management is about noticing trends **before** they matter.

---

## Performance Characteristics That Matter

### Random vs Sequential I/O

Different workloads stress disks differently:

- databases and metadata-heavy operations → random I/O
- logs, backups, streaming writes → sequential I/O

A disk that performs well for one may struggle badly with the other.

---

### Latency Beats Throughput

High throughput with high latency still feels slow.

When diagnosing storage performance:

- latency spikes are usually more damaging than bandwidth limits
- shared storage amplifies latency under contention

---

## Swap: Symptom, Not Solution

Swap exists to:

- absorb memory pressure
- prevent immediate OOM conditions

But heavy swap usage usually indicates:

- memory overcommitment
- poor workload sizing
- storage-backed performance collapse

Check usage:

```bash
free -h
swapon --show
```

Swap activity often turns memory problems into storage problems.

---

## Finding What’s Using Disk

Start broad:

```bash
du -sh /*
```

Then narrow down:

```bash
du -sh /var/*
```

Pay special attention to:

- `/var/log`
- `/var/lib`
- application-specific data directories

---

## Deleted Files Still Using Space

A classic and dangerous scenario:

- file is deleted
- process keeps it open
- disk space is not reclaimed

Find them:

```bash
lsof | grep deleted
```

This is common with:

- log files
- rotated output
- long-running services

---

## Filesystem-Level Issues

### Mount Options Matter

Options like:

- `noatime`
- journaling modes
- write barriers

can materially affect performance and durability.

Default options are safe—but not always optimal.

---

### Corruption and Recovery

Filesystems trade performance for safety differently.

Symptoms of trouble:

- sudden read-only mounts
- I/O errors in logs
- kernel warnings

Never ignore filesystem warnings—they tend to escalate.

---

## Virtualized and Platform Environments

Storage issues compound under abstraction:

- multiple VMs sharing the same physical disks
- containers writing to host filesystems
- ephemeral storage filling node disks
- shared volumes becoming contention points

Host storage problems often appear as:

- pod evictions
- CI failures
- unexplained latency
- “random” crashes

Always consider the host when higher layers misbehave.

---

## Common Failure Patterns

| Symptom | Likely Cause |
|------|-------------|
| Disk full alerts | Log or cache growth |
| Writes failing with space free | Inode exhaustion |
| System slow under load | I/O contention |
| Memory pressure + slowness | Swap thrashing |
| Space not reclaimed | Deleted open files |

Patterns save time.

---

## What Not to Do

- Don’t assume disks are fast enough
- Don’t ignore inode usage
- Don’t treat swap as a fix
- Don’t debug applications before validating storage health
- Don’t wait for alerts to investigate growth

---

## Takeaways

- Host storage fails quietly until it doesn’t
- Capacity is more than free space
- Performance issues often start with latency
- Swap usually signals deeper problems
- Storage issues propagate upward through the stack

If systems feel unstable or unpredictable, **check storage early**—it’s often the root cause hiding in plain sight.
