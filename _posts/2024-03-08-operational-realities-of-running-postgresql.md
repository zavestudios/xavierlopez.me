---
layout: single
title: "Operational Realities of Running PostgreSQL"
date: 2024-03-08 08:00:00 +0000
last_modified_at: "2025-01-12"
categories:
  - databases
  - devops
  - devops
tags:
  - postgresql
  - databases
  - devops
  - storage
  - stateful-workloads
excerpt: "Practical lessons about running PostgreSQL as a system: memory, storage, I/O, and why defaults and containers don’t remove operational responsibility."
toc: true
toc_sticky: true
---

## Context

PostgreSQL is often treated like a dependency:

- install it
- point an app at it
- scale when it gets slow

In reality, PostgreSQL is a **stateful system** with strong opinions about memory, disk, and durability. When those expectations aren’t met, performance problems and outages tend to look mysterious.

This post captures practical realities of running PostgreSQL in production—especially in containerized and Kubernetes environments—without turning into a tuning checklist.

---

## PostgreSQL Is a System, Not a Library

PostgreSQL:

- runs multiple cooperating processes
- manages its own memory aggressively
- assumes durable storage
- trades performance for correctness by default

You don’t “embed” Postgres. You **host** it.

Treating it like a stateless service almost always leads to surprises.

---

## Memory: Connections Matter More Than Queries

One of the most common misconceptions is that PostgreSQL memory usage scales primarily with data size or query complexity.

In practice, it scales with **connections**.

Each connection:

- consumes memory
- spawns backend processes
- increases scheduling and locking overhead

A large number of idle connections can be just as harmful as active ones.

This is why:

- connection pooling matters
- unbounded client connections are dangerous
- “it works locally” doesn’t translate to production

---

## CPU Is Rarely the First Bottleneck

When PostgreSQL is slow, adding CPU is often the first instinct.

In reality, PostgreSQL performance issues are more commonly caused by:

- disk I/O latency
- WAL contention
- excessive connections
- lock contention
- memory pressure

CPU becomes a bottleneck *after* those are addressed.

---

## Disk and WAL Are Central to Performance

PostgreSQL’s durability guarantees rely heavily on the **Write-Ahead Log (WAL)**.

This means:

- every write involves disk I/O
- latency matters more than raw throughput
- storage performance directly affects commit speed

Slow or inconsistent disks show up as:

- slow transactions
- replication lag
- unexplained query latency

This is especially important in virtualized or networked storage environments.

---

## Containers Don’t Change the Fundamentals

Running PostgreSQL in a container does not change how PostgreSQL works.

It still:

- writes to disk
- uses shared memory
- expects predictable I/O
- assumes stable filesystem semantics

Common container mistakes include:

- ephemeral storage for data directories
- ignoring filesystem sync behavior
- assuming resource limits replace tuning
- placing Postgres on storage designed for stateless workloads

Containers change packaging, not physics.

---

## Kubernetes Adds Indirection, Not Immunity

Kubernetes can help manage PostgreSQL, but it does not remove operational requirements.

In Kubernetes:

- PersistentVolumes define durability
- StorageClasses define behavior
- the underlying storage still matters
- noisy neighbors still exist

If the storage layer is slow or misconfigured, PostgreSQL will faithfully surface those problems.

---

## Defaults Are Conservative (for a Reason)

PostgreSQL defaults prioritize:

- correctness
- durability
- broad compatibility

They are intentionally conservative.

This is good for safety, but it means:

- defaults are rarely optimal for high-throughput systems
- tuning should be intentional and informed
- copying random config snippets is risky

Understanding *why* a setting exists matters more than memorizing values.

---

## Monitoring Tells the Truth

PostgreSQL is verbose when asked correctly.

Key signals include:

- connection counts
- transaction duration
- lock waits
- WAL write latency
- disk I/O wait times

When Postgres is unhealthy, it usually tells you—just not always in the place people look first.

---

## Common Anti-Patterns

A few patterns show up repeatedly in troubled deployments:

- treating Postgres like stateless infrastructure
- scaling application replicas without considering DB impact
- ignoring connection pooling
- placing data on slow or inconsistent storage
- assuming Kubernetes abstracts database concerns away

None of these fail immediately. They fail under load.

---

## Practical Guidance

- plan connections before planning CPU
- treat storage latency as a first-class concern
- assume containers do not change database fundamentals
- understand WAL behavior before tuning performance
- observe before optimizing

PostgreSQL rewards understanding. It punishes assumptions.

---

## Closing Thought

Most PostgreSQL outages aren’t caused by bugs.

They’re caused by mismatches between:

- what PostgreSQL expects
- and what the platform provides

Once you treat Postgres as a system with real physical constraints, its behavior becomes predictable—and manageable.
