---
layout: single
title: "Creating Kubernetes Secrets from the Command Line (and When Not To)"
date: 2024-02-19 08:00:00 +0000
last_modified_at: "2025-01-06"
categories:
  - kubernetes
  - security
  - operations
tags:
  - kubectl
  - secrets
  - kubernetes
  - configuration-management
  - security
excerpt: "Practical notes on creating Kubernetes Secrets from the command line, including when kubectl create secret is appropriate—and when it becomes a liability."
toc: true
toc_sticky: true
---

## Context

Kubernetes Secrets are often introduced early, but rarely explained clearly.

Most examples focus on *how* to create a Secret, not:

- **why** you’d choose one method over another
- what tradeoffs you’re making
- how Secrets fit into a broader operational model

This post focuses specifically on creating Secrets from the command line using `kubectl create secret`, and—just as importantly—when *not* to do that.

---

## What kubectl create secret Actually Does

At a high level, `kubectl create secret`:

- takes input (literals, files, or environment variables)
- base64-encodes the values
- submits a Secret object to the Kubernetes API server

It does **not**:

- encrypt values by itself
- manage secret rotation
- track provenance
- enforce security policies

It is a creation mechanism, not a secrets management system.

---

## Creating a Secret from Literal Values

The most direct pattern uses literals:

```sql
kubectl create secret generic example-db-creds \
  --from-literal=username=example_user \
  --from-literal=password=example_password
```

This is useful for:

- quick experiments
- local clusters
- validating application wiring

It is **not** ideal for long-lived or production secrets.

---

## Creating a Secret from a File

A more common pattern is file-based creation:

```sql
kubectl create secret generic example-config \
  --from-file=application.yaml
```

This creates a Secret where:

- the key is the filename
- the value is the file contents

This works well for:

- config blobs
- certificates
- structured files

But it still raises questions about where that file lives and how it’s protected.

---

## Creating Secrets from Environment Files

Environment-style files can also be used:

```sql
kubectl create secret generic example-env \
  --from-env-file=.env
```

This is convenient, but dangerous if:

- `.env` files are committed accidentally
- shell history is not managed carefully
- multiple environments share similar filenames

Convenience and risk scale together here.

---

## Namespaces Matter More Than Syntax

By default, Secrets are created in the **current namespace**.

This is one of the most common failure modes.

Always be explicit:

```sql
kubectl create secret generic example-db-creds \
  --from-literal=username=example_user \
  --from-literal=password=example_password \
  -n example-namespace
```

Secrets in the wrong namespace are indistinguishable from missing secrets.

---

## Inspecting What You Created

You can confirm a Secret exists with:

```bash
kubectl get secret example-db-creds -n example-namespace
```

And inspect metadata with:

```bash
kubectl describe secret example-db-creds -n example-namespace
```

Avoid decoding values casually unless you need to verify wiring.

If you *do* decode, do it intentionally and clean up afterward.

---

## When kubectl create secret Is the Right Tool

This approach works well when:

- bootstrapping a cluster
- validating application configuration
- working in ephemeral environments
- teaching or learning Kubernetes mechanics

It’s a **mechanical tool**, not a long-term strategy.

---

## When kubectl create secret Becomes a Liability

Problems arise when:

- secrets are created manually and forgotten
- values live in shell history
- environments drift
- rotation becomes manual and error-prone
- auditability matters

At scale, this approach does not age well.

---

## Better Patterns for the Long Term

As systems mature, secrets creation usually moves toward:

- GitOps workflows
- external secret managers
- sealed or encrypted manifests
- automated rotation

In those models:

- `kubectl create secret` is often replaced
- or used only as a bootstrap mechanism

That’s not a failure—it’s progress.

---

## Practical Takeaways

- `kubectl create secret` is about *object creation*, not security
- be explicit about namespaces
- understand where secret material lives
- treat manual creation as transitional
- plan for replacement as systems grow

Secrets are less about syntax and more about discipline.

Understanding the limits of your tools is part of operating Kubernetes responsibly.
