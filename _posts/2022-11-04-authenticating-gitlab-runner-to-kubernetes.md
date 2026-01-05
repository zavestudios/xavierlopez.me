---
layout: single
title: "Authenticating GitLab Runner to Kubernetes"
date: 2022-11-04 08:55:00 +0000
last_modified_at: "2025-02-21"
categories:
  - ci-cd
  - kubernetes
  - security
tags:
  - gitlab
  - gitlab-runner
  - kubernetes
  - authentication
  - rbac
  - service-accounts
excerpt: "How GitLab Runner authenticates to Kubernetes, the security implications of each method, and how to choose the right approach for production clusters."
toc: true
toc_sticky: true
---

## Context

When GitLab Runner executes jobs against Kubernetes, it must authenticate to the cluster with **enough permissions to function—but no more**.

This is a deceptively important problem. Over-permissioned runners are a common source of:
- lateral movement
- privilege escalation
- accidental cluster-wide changes

This post breaks down **how GitLab Runner authenticates to Kubernetes**, the mechanisms involved, and the tradeoffs between simplicity and security.

---

## What GitLab Runner Actually Needs

At a minimum, a Kubernetes-backed GitLab Runner must be able to:
- create and delete pods
- read pod status and logs
- mount secrets and config maps
- clean up resources after jobs complete

Everything else should be considered optional—and potentially dangerous.

---

## Authentication vs Authorization (Important Distinction)

- **Authentication** answers: *Who are you?*
- **Authorization** answers: *What are you allowed to do?*

GitLab Runner authentication establishes identity; **RBAC** determines blast radius.

Most security failures happen when these are conflated.

---

## Common Authentication Methods

### 1️⃣ Service Account Tokens (Recommended)

The most common and secure approach is to authenticate using a **Kubernetes ServiceAccount**.

How it works:
- GitLab Runner is deployed inside the cluster
- It runs under a dedicated ServiceAccount
- Kubernetes automatically mounts a token into the runner pod
- API requests are authenticated using that token

This approach is:
- native to Kubernetes
- auditable
- revocable
- compatible with RBAC

This should be the default choice for in-cluster runners.

---

### 2️⃣ kubeconfig (Generally Discouraged)

Some setups use a `kubeconfig` file containing:
- cluster endpoint
- certificate authority
- user credentials or tokens

Problems with this approach:
- credentials are often long-lived
- secrets tend to sprawl
- revocation is painful
- easy to accidentally over-permission

This method is sometimes used for:
- legacy runners
- external runners
- quick experiments

It should be avoided in production clusters.

---

### 3️⃣ Static Tokens (High Risk)

Hard-coded tokens (even if stored as secrets) are risky:

- no automatic rotation
- often cluster-admin scoped
- difficult to audit usage
- high blast radius if leaked

If you see this in production, it’s worth revisiting immediately.

---

## RBAC: Where Safety Is Enforced

Authentication gets the runner in the door. **RBAC decides what happens next.**

### Namespace-Scoped Roles

A strong default pattern:
- one namespace per runner or workload class
- namespace-scoped `Role`
- minimal permissions required to run jobs

This contains failures and limits damage.

---

### Avoid ClusterRole Unless Necessary

Granting `ClusterRole` permissions to a runner:
- expands blast radius
- increases accidental damage risk
- makes audits harder

Only do this when jobs legitimately need cluster-wide access—and document why.

---

## A Safe Baseline Pattern

A common, sane setup looks like this:

- Dedicated namespace for CI jobs
- Dedicated ServiceAccount for GitLab Runner
- Namespace-scoped Role allowing:
  - pod creation/deletion
  - pod logs access
  - config map and secret reads
- Explicit denial of cluster-wide access

This balances usability with safety.

---

## Token Rotation and Lifecycle

Modern Kubernetes clusters support:
- projected service account tokens
- bounded lifetimes
- automatic rotation

This reduces risk from:
- leaked tokens
- stale credentials
- forgotten secrets

If your cluster supports this, enable it.

---

## Common Failure Modes

| Symptom | Likely Cause |
|------|-------------|
| Jobs fail to start | Missing pod permissions |
| Logs unavailable | Insufficient log access |
| Cleanup failures | Delete permissions missing |
| Works once, then fails | Expired or rotated token |
| Too much power | ClusterRole misuse |

Authentication problems often masquerade as CI failures.

---

## Observability and Auditing

Enable and monitor:
- Kubernetes audit logs
- API server requests from runner identities
- unexpected resource access

Runners are automation engines—visibility matters.

---

## What Not to Do

- Don’t run runners as `cluster-admin`
- Don’t reuse service accounts across environments
- Don’t embed kubeconfigs in repositories
- Don’t assume CI jobs are “trusted”

CI systems execute arbitrary code by design.

---

## Takeaways

- GitLab Runner authentication is a security boundary
- ServiceAccounts + RBAC are the safest default
- Minimize permissions aggressively
- Prefer short-lived, rotated credentials
- Treat runners as semi-trusted automation

A well-authenticated runner quietly does its job.  
A poorly authenticated one eventually becomes an incident.
