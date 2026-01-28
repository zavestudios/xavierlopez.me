---
layout: single
title: "Restarting Unicorn Without Dropping Requests"
date: 2022-02-04 07:30:00 +0000
last_modified_at: "2025-01-01"
categories:
  - rails
  - devops
tags:
  - unicorn
  - rails
  - process-management
  - zero-downtime
excerpt: "How to restart a Unicorn-based Rails application safely, what signals Unicorn responds to, and how to avoid dropping requests during restarts."
toc: true
toc_sticky: true
---

## Context

Unicorn is designed to be **simple, predictable, and Unix-friendly**.

That simplicity shows up most clearly in how Unicorn handles restarts: via **signals**, not complex orchestration. If you understand which signals Unicorn listens for—and what they do—you can restart or reload your app **without dropping traffic**.

This post explains the common restart patterns and when to use each one.

---

## How Unicorn Is Structured

A typical Unicorn setup includes:

- one **master process**
- multiple **worker processes**
- a shared listening socket

The master process manages workers. Workers handle requests. Restart behavior depends on which process receives which signal.

---

## Finding the Unicorn Master PID

Before sending signals, you need the master PID.

Common approaches:

- a PID file (configured in `unicorn.rb`)
- process listing

Example using a PID file:

```bash
cat /path/to/unicorn.pid
```

Or via process inspection:

```bash
ps aux | grep unicorn
```

Always confirm you’re signaling the **master**, not a worker.

---

## Graceful Restart (Recommended)

To perform a **graceful restart**:

```bash
kill -USR2 <unicorn_master_pid>
```

What this does:

- starts a new master process
- spins up new workers
- allows old workers to finish in-flight requests
- shuts down old workers cleanly

This is the preferred way to deploy code changes with zero downtime.

---

## Graceful Reload (Configuration Changes)

If you’ve only changed configuration and want workers to reload:

```bash
kill -HUP <unicorn_master_pid>
```

This:

- reloads configuration
- restarts worker processes
- keeps the same master process

Use this when you don’t need a full master restart.

---

## Immediate Restart (Use Carefully)

To force Unicorn to stop immediately:

```bash
kill -TERM <unicorn_master_pid>
```

or

```bash
kill -INT <unicorn_master_pid>
```

This:

- stops accepting new requests
- terminates workers
- may drop active connections

Only use this during emergencies or controlled shutdowns.

---

## Rolling Restarts and Zero Downtime

Unicorn’s graceful restart model works best when:

- a load balancer sits in front
- multiple workers are running
- requests are short-lived

During `USR2` restarts:

- old and new masters coexist briefly
- sockets are handed off
- traffic continues flowing

This design avoids request loss without complex coordination.

---

## Common Deployment Pattern

A typical deploy flow:

1. update application code
2. verify configs and permissions
3. send `USR2` to the master
4. monitor logs and worker health
5. confirm old workers exit cleanly

This keeps deploys boring—which is the goal.

---

## Verifying a Successful Restart

After restarting:

- check logs for new master startup
- confirm workers are accepting requests
- ensure old workers have exited
- watch error rates briefly

If something looks wrong, Unicorn’s signal-based control makes rollback straightforward.

---

## Common Mistakes

- signaling worker PIDs instead of the master
- using `KILL` instead of graceful signals
- restarting without a load balancer
- forgetting to update the PID file
- assuming a restart reloads configuration automatically

Most restart issues are procedural, not technical.

---

## Practical Tips

- Always prefer `USR2` for deploys
- Use `HUP` for config reloads
- Avoid `TERM` unless you intend downtime
- Keep Unicorn logs verbose during restarts
- Document your signal usage for the team

Understanding signals turns Unicorn from “mysterious” into predictable.

---

## Takeaways

- Unicorn restarts are signal-driven
- `USR2` enables zero-downtime deploys
- `HUP` reloads workers and configuration
- Hard stops risk dropped requests
- Simple process models reward careful handling

With the right signal, Unicorn restarts are quiet, fast, and drama-free.
