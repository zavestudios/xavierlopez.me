---
layout: single
title: "Understanding Byte Size Units (Without Overthinking Them)"
date: 2024-02-28 08:00:00 +0000
last_modified_at: "2025-01-09"
categories:
  - fundamentals
  - systems
  - storage
tags:
  - bytes
  - storage
  - memory
  - fundamentals
  - systems
excerpt: "A practical explanation of byte size units—KB vs KiB, MB vs MiB—and why the distinction matters in real systems."
toc: true
toc_sticky: true
---

## Context

Most engineers *know* that there’s a difference between decimal and binary byte units.

Fewer engineers can confidently say:

- which one a given system is using
- when the distinction matters
- when it’s safe to ignore

This post explains byte size units in the way that’s actually useful in practice—without turning it into a standards lecture.

---

## The Two Systems You’ll Encounter

There are **two** byte size systems in common use:

### Decimal (Base-10)

Used primarily for:

- disk marketing
- network throughput
- vendor specifications

```text
1 KB = 1,000 bytes
1 MB = 1,000,000 bytes
1 GB = 1,000,000,000 bytes
1 TB = 1,000,000,000,000 bytes
```

These scale cleanly by powers of 10.

---

### Binary (Base-2)

Used primarily by:

- operating systems
- memory reporting
- filesystems
- low-level tooling

```text
1 KiB = 1,024 bytes
1 MiB = 1,048,576 bytes
1 GiB = 1,073,741,824 bytes
1 TiB = 1,099,511,627,776 bytes
```

These scale by powers of 2.

---

## Why the Names Look So Similar

The confusion comes from history.

For years, binary quantities were labeled using decimal names:

- “KB” meant 1024 bytes
- “MB” meant 1024² bytes

That shorthand stuck—long after it became misleading.

The **IEC standard** introduced:

- KiB, MiB, GiB, TiB

Not to complicate things—but to be precise.

---

## Where This Actually Matters

In practice, you’ll most often see:

- **Disks advertised in GB/TB (decimal)**
- **Operating systems reporting GiB/TiB (binary)**
- **Memory measured in GiB**
- **Network speeds measured in Gb/s (decimal bits)**

This is why a “1 TB disk” doesn’t show up as “1 TB” in your OS.

Nothing is missing. Nothing is broken.

The units changed.

---

## A Practical Example

A disk advertised as **1 TB** contains:

```text
1,000,000,000,000 bytes
```

Your OS reports in GiB:

```text
1,000,000,000,000 ÷ 1,073,741,824 ≈ 931 GiB
```

That ~7% difference is expected.

It’s not overhead. It’s arithmetic.

---

## When You Should Care

You should pay attention to units when:

- capacity planning
- comparing vendor claims
- sizing storage or memory limits
- troubleshooting “missing” space
- interpreting monitoring metrics

This is especially true in:

- Kubernetes resource limits
- cloud storage pricing
- filesystem usage reports

---

## When You Can Mostly Ignore It

You can often ignore the distinction when:

- working at small scales
- eyeballing approximate usage
- doing relative comparisons within the same system

Just don’t mix unit systems mid-calculation.

---

## Practical Guidance

A simple rule of thumb:

- **If it’s hardware, bandwidth, or marketing → decimal**
- **If it’s an OS, memory, or filesystem → binary**

When precision matters, check the unit label explicitly.

If the tool says `GiB`, believe it.

---

## Why This Is Still Worth Knowing

This confusion persists because:

- both systems are valid
- both are widely used
- tools are inconsistent about labeling

Understanding the distinction once prevents years of second-guessing.

It’s a small mental model with a long shelf life.
