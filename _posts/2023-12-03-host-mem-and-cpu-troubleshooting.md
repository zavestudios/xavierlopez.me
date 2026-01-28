---
title: "Host Memory and CPU Troubleshooting: A Practical Playbook"
date: 2023-12-03 10:43:00 +0000
last_modified_at: "2025-01-11"
categories:
  - linux
  - systems
  - development
tags:
  - cpu
  - memory
  - devops
  - sysstat
  - observability
excerpt: "A practical, host-level troubleshooting guide for diagnosing CPU and memory pressure using sysstat, procfs, and core Linux tools."
toc: true
toc_sticky: true
layout: single
---

## Context

When a Linux host is “slow,” the hardest part is not fixing the problem — it’s **figuring out where to look first**.

This guide is a **host-level troubleshooting playbook** for:

- high CPU usage
- memory pressure
- load average confusion
- performance complaints without clear errors

It’s written for engineers who need **ground truth from the OS**, whether the host runs bare metal, VMs, or Kubernetes nodes.

---

## Step 0: Make Sure You’re Collecting Data

Many useful diagnostics rely on **historical metrics**. If `sysstat` isn’t running, you’re blind to the past.

### Install and enable sysstat

```bash
systemctl enable --now sysstat
systemctl status sysstat
```

### Enable data collection

Edit:

```bash
sudo vim /etc/default/sysstat
```

Ensure:

```bash
ENABLED="true"
```

### Verify cron configuration

```bash
sudo cat /etc/cron.d/sysstat
```

If sysstat isn’t collecting, tools like `sar` won’t help you retroactively.

---

## Step 1: Understand Uptime and Load

### Check uptime and load averages

```bash
uptime
```

This shows:

- how long the system has been running
- load averages over **1, 5, and 15 minutes**

### Variants worth knowing

```bash
uptime -s   # system start time
uptime -p   # human-readable uptime
cat /proc/uptime
```

### Why load averages matter

Load average is **not CPU usage**.

It represents:

- runnable processes
- processes waiting on CPU or I/O

High load with low CPU usage often means:

- I/O contention
- memory pressure
- blocked processes

---

## Step 2: Know Your CPU Topology

Before interpreting CPU metrics, know what “100%” actually means.

### List CPU details

```bash
lscpu
```

### Just the CPU count

```bash
lscpu | grep '^CPU(s)'
```

This matters on:

- multi-core systems
- hyperthreaded CPUs
- virtual machines with vCPUs

---

## Step 3: Diagnose CPU Pressure

### Real-time CPU usage

```bash
mpstat
```

### Sample every second for a minute

```bash
mpstat 1 60
```

### Inspect a single CPU

```bash
mpstat -P 0 1 60
```

### Historical CPU usage

```bash
sar -u
sar -u -P 0
```

### Identify CPU hogs

```bash
top
```

Look for:

- sustained high `%CPU`
- many runnable processes
- uneven CPU utilization

---

## Step 4: Investigate Memory and Swap

### Quick overview

```bash
free -h
```

### Kernel memory details

```bash
cat /proc/meminfo
```

### Historical memory usage

```bash
sar -r
```

### Memory-heavy processes

In `top`:

- press `f` (fields)
- move to `MEM`
- press `s` (select)
- `q` to quit

High memory pressure often manifests as:

- swap activity
- CPU spikes (due to reclaim)
- latency under load

---

## Understanding `/proc` (Why This Works)

The `/proc` filesystem is a **pseudo-filesystem** exposing kernel data structures.

It’s authoritative.

If monitoring tools disagree, `/proc` usually wins.

Learn more:

```bash
man procfs
```

---

## Common Failure Patterns

| Symptom | Likely Cause | What to Check |
|------|------------|--------------|
| High load, low CPU | I/O wait | `mpstat`, `sar -u` |
| CPU spikes under memory pressure | Reclaim activity | `free`, `/proc/meminfo` |
| One core pegged | Single-threaded workload | `mpstat -P` |
| “Random” slowness | Historical saturation | `sar` |

---

## Platform & Virtualization Notes

- Kubernetes nodes often hide host pressure until pods fail
- VM CPU steal time can look like “slow hardware”
- Memory overcommitment amplifies reclaim costs

Host-level visibility is still essential — even in abstracted platforms.

---

## Takeaways

- Always enable historical metrics *before* you need them
- Load averages require context
- CPU and memory issues are often intertwined
- `/proc` provides ground truth
- Host-level diagnostics still matter in modern platforms

When performance feels vague or intermittent, **start at the host** — it usually tells the truth faster than higher layers.
