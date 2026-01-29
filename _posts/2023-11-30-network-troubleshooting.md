---
layout: single
title: "Network Troubleshooting: A Practical, Layered Approach"
date: 2023-11-30 10:44:00 +0000
last_modified_at: "2025-02-03"
categories:
  - networking
  - development
tags:
  - networking
  - tcp-ip
  - dns
  - latency
  - packet-loss
excerpt: "A step-by-step approach to diagnosing network problems, focusing on isolating failure domains and validating assumptions layer by layer."
toc: true
toc_sticky: true
---

## Context

Network issues are rarely binary.

Most of the time, the network is:

- *partially* working
- working for some clients but not others
- fast sometimes and slow at others

This makes network troubleshooting feel chaotic. The cure is **structure**.

This post lays out a **layered, repeatable approach** to diagnosing network problems without guessing.

---

## The Core Principle: Eliminate Layers

Effective troubleshooting is about answering one question at a time:

> *What is the highest layer I can confidently rule out?*

Each step narrows the failure domain until the problem becomes obvious—or at least localized.

---

## Step 1: Is the Host Reachable?

Start with the simplest possible test.

```bash
ping <destination>
```

What this tells you:

- basic IP connectivity exists
- routing is functioning (at least one way)
- ICMP is not blocked

What it **does not** tell you:

- application reachability
- TCP/UDP health
- latency under load

If ping fails, don’t go higher.

---

## Step 2: Is Name Resolution Working?

Many “network” problems are actually **DNS problems**.

```bash
nslookup <hostname>
dig <hostname>
```

Verify:

- the hostname resolves
- it resolves to the expected IP
- the result is consistent across hosts

If DNS is broken, everything above it lies.

---

## Step 3: Can You Reach the Port?

ICMP working does not mean services are reachable.

```bash
nc -vz <host> <port>
```

Or with curl:

```bash
curl -v http://<host>:<port>
```

This validates:

- TCP connectivity
- firewall rules
- service listening state

If the port is unreachable, application debugging is premature.

---

## Step 4: Inspect the Local Network State

Look at the local interface and routing table.

```bash
ip addr
ip route
```

Check for:

- correct IP assignment
- expected default route
- multiple routes competing unexpectedly

Misrouting often looks like “random” failures.

---

## Step 5: Identify Latency or Loss

When things are slow but not broken:

```bash
traceroute <destination>
mtr <destination>
```

These tools help surface:

- where latency increases
- where packet loss begins
- whether the issue is local or upstream

Remember: packet loss at one hop does not always mean failure at that hop—but trends matter.

---

## Step 6: Validate the Service Itself

If the network path is healthy, verify the application endpoint.

- Is the service running?
- Is it bound to the correct interface?
- Is it overloaded?

Many “network outages” are healthy networks exposing failing services.

---

## Common Failure Patterns

| Symptom | Likely Cause |
|------|-------------|
| Ping works, app fails | Port blocked or service down |
| Works by IP, not hostname | DNS issue |
| Intermittent slowness | Congestion or shared I/O |
| Works from some hosts | Routing or policy asymmetry |
| Random timeouts | Packet loss or MTU mismatch |

Patterns save time.

---

## Virtualized and Platform Environments

In VMs and containers, add more layers:

- virtual switches
- overlay networks
- policy engines
- NAT and port mapping

Always ask:
> *Is this failure inside the guest, on the host, or in the fabric?*

Troubleshooting stops being linear once virtualization is involved.

---

## What Not to Do

- Don’t jump straight to packet captures
- Don’t assume “the network is fine”
- Don’t debug applications before validating connectivity
- Don’t change things before you understand the failure

Structure beats heroics.

---

## Takeaways

- Network troubleshooting is about **elimination**, not intuition
- DNS failures masquerade as everything else
- Validate reachability before services
- Latency and loss require different tools than outages
- Virtualization adds layers—be explicit about where you’re looking

A calm, layered approach turns “the network is broken” into a solvable problem.
