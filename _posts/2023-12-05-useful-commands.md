---
title: "Useful Linux Commands for Platform Engineers"
date: 2023-12-05 10:50:00 +0000
last_modified_at: "2025-04-03"
categories:
  - linux
  - administration
  - platform
tags:
  - linux
  - troubleshooting
  - observability
  - cli
excerpt: "A small but high-leverage set of Linux commands platform engineers reach for when debugging performance, identity, and system state."
toc: true
toc_sticky: true
layout: single
---

## Context

Platform engineers don’t memorize *every* Linux command — they memorize the **few that unblock everything else**.

When a system is slow, access looks wrong, or behavior differs from expectations, these commands help answer the first critical question:

> *What is the system actually doing right now?*

This post collects a handful of commands that repeatedly prove useful in real platform and operations work.

---

## Process and Resource Visibility

### `top`

`top` provides a dynamic, real-time view of a running system. It’s often the first command to run when performance feels off.

Key fields worth understanding:

- **PID** — Process ID
- **USER** — Process owner
- **PR** — Kernel priority
- **NI** — Nice value (user-space priority hint)
- **VIRT** — Total virtual memory used
- **RES** — Resident (non-swapped) memory
- **SHR** — Shared memory
- **%CPU** — CPU usage
- **%MEM** — Memory usage
- **TIME+** — Total CPU time consumed
- **COMMAND** — Executable name

### Why this matters for platform engineers

- Identifies runaway processes
- Surfaces CPU vs memory pressure
- Helps distinguish real load from noisy neighbors
- Provides immediate feedback without additional tooling

When combined with knowledge of virtualization or container limits, `top` helps explain *why* systems behave the way they do.

---

## Filtering Meaningful Configuration Lines

### Removing comments and blank lines

A common task is counting or extracting **active configuration lines** from files that include comments and whitespace.

```bash
grep -Ev '^($|#)' <path-to-file> | wc -l > <path-to-new-file>
```

What this does:

- `grep -Ev '^($|#)'` removes blank lines and comments
- `wc -l` counts remaining lines
- Output is redirected to a new file

### Why this matters

- Auditing configuration size
- Comparing rendered configs
- Debugging templated output
- Validating policy or rule sets

This pattern shows up constantly in automation and compliance workflows.

---

## Name Service and Identity Inspection

### `getent`

`getent` queries the Name Service Switch (NSS), which may pull data from:

- local files
- LDAP
- SSSD
- NIS
- other identity providers

Examples:

```bash
getent hosts
getent group
getent passwd
getent shadow
getent services
```

### Why platform engineers care

- Confirms **what the system believes** about users, groups, and hosts
- Helps debug authentication and authorization issues
- Works consistently across local and directory-backed systems

If identity or access looks wrong, `getent` is often the fastest truth source.

---

## In Practice: Platform Engineering Scenarios

- **CI runner behaving oddly?**  

  Use `top` to check CPU saturation or memory pressure.

- **Config drift suspected?**  

  Strip comments and compare active lines.

- **Access control failing mysteriously?**  

  Use `getent` to verify NSS resolution.

These commands help validate assumptions before deeper investigation.

---

## Common Failure Modes

| Symptom | Likely Cause | What to Check |
|------|------------|--------------|
| High load but low throughput | CPU contention | `top`, virtualization layer |
| Access denied unexpectedly | Identity mismatch | `getent passwd/group` |
| Config looks correct but behaves wrong | Hidden differences | comment-stripped diff |

---

## Takeaways

- You don’t need hundreds of commands — you need the *right* ones
- Real-time visibility beats guesswork
- NSS can hide complexity behind simple files
- These commands pair well with automation and observability tools

If you can quickly answer *“what’s happening right now?”*, you can usually figure out *what to do next*.
