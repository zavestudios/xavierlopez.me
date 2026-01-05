---
layout: single
title: "Creating and Understanding kubeconfig Files"
date: 2024-03-02 08:00:00 +0000
last_modified_at: 2025-01-10
categories:
  - kubernetes
  - security
  - operations
tags:
  - kubernetes
  - kubeconfig
  - kubectl
  - authentication
  - access-control
excerpt: "A practical mental model for creating and understanding kubeconfig files, including clusters, users, contexts, and how kubectl actually authenticates."
toc: true
toc_sticky: true
---

## Context

`kubectl` feels simple once it works.

But when access breaks—or when you need to create access from scratch—the kubeconfig file suddenly becomes mysterious. Tokens, certificates, contexts, users, clusters: everything is there, but rarely explained clearly.

This post explains what a kubeconfig actually is, how it’s structured, and how to create or modify one intentionally instead of relying on magic.

---

## What a kubeconfig Really Is

A kubeconfig file is **not credentials**.

It is a **configuration document** that tells `kubectl`:
- which cluster to talk to
- how to authenticate
- which identity to use
- which context ties those together

Think of it as a **connection profile**, not a secret store.

---

## The Four Core Concepts

Every kubeconfig is built from four pieces.

### Cluster
Defines:
- API server endpoint
- CA certificate used to trust the server

### User
Defines:
- how authentication happens
- certificates, tokens, or exec plugins

### Context
Binds:
- one cluster
- one user
- optionally a namespace

### Current Context
Tells `kubectl` which context to use by default.

Nothing works unless all four line up.

---

## Inspecting an Existing kubeconfig

To see what `kubectl` is currently using:

```
kubectl config view
```

To see only the active context:

```
kubectl config current-context
```

To list all contexts:

```
kubectl config get-contexts
```

These commands are often enough to diagnose access confusion.

---

## Creating a kubeconfig Manually (Step by Step)

Creating a kubeconfig intentionally makes the model click.

### Step 1: Define the Cluster

```
kubectl config set-cluster example-cluster \
  --server=https://api.example.internal:6443 \
  --certificate-authority=/path/to/ca.crt
```

This tells `kubectl` *where* the API server is and *how to trust it*.

---

### Step 2: Define the User

Example using a client certificate:

```
kubectl config set-credentials example-user \
  --client-certificate=/path/to/client.crt \
  --client-key=/path/to/client.key
```

Other authentication methods exist, but the structure is the same.

---

### Step 3: Create a Context

```
kubectl config set-context example-context \
  --cluster=example-cluster \
  --user=example-user \
  --namespace=default
```

This binds identity to destination.

---

### Step 4: Activate the Context

```
kubectl config use-context example-context
```

At this point, `kubectl` is fully configured.

---

## Where kubeconfig Files Live

By default, `kubectl` looks for:

```
~/.kube/config
```

You can override this with:

```
KUBECONFIG=/path/to/config kubectl get pods
```

Multiple kubeconfig files can be merged automatically via the `KUBECONFIG` environment variable.

---

## Why Contexts Matter More Than Credentials

Most access mistakes are **context mistakes**, not auth failures.

Common issues include:
- talking to the wrong cluster
- using the wrong namespace
- reusing similarly named contexts
- assuming the current context is what you think it is

Always check the context before acting.

---

## How This Relates to RBAC

A kubeconfig:
- defines *how* you authenticate
- does **not** define *what you can do*

Authorization is enforced by:
- Kubernetes RBAC
- Roles and RoleBindings
- ClusterRoles and ClusterRoleBindings

If access is denied, the kubeconfig is usually fine—the permissions are not.

---
### Verifying Access with kubectl auth can-i

Once authentication is working, the next question is authorization.

`kubectl auth can-i` answers a simple but critical question:

> “Is this identity allowed to do this action?”

### Basic check

    kubectl auth can-i get pods

This checks whether the **current context’s user** is allowed to list pods in the current namespace.

### Explicit namespace check

    kubectl auth can-i create deployments -n example-namespace

This avoids false assumptions caused by the active namespace.

### Cluster-scoped permissions

    kubectl auth can-i list nodes

This verifies permissions that are not namespace-bound.

## Why This Command Is So Valuable

`kubectl auth can-i` is the fastest way to distinguish between:

- authentication problems (kubeconfig, credentials)
- authorization problems (RBAC)

If the command returns `no`, authentication succeeded but permissions are insufficient.

If the command errors, the kubeconfig itself may be misconfigured.

## Make It a Habit

Before debugging:
- forbidden errors
- CI/CD access failures
- “works for me” discrepancies
- broken automation

Run:

    kubectl auth can-i <verb> <resource>

It turns RBAC from guesswork into something concrete.


---
## Practical Guidance

- treat kubeconfig as connection metadata
- keep contexts clearly named
- never assume the current context
- avoid sharing kubeconfig files directly
- regenerate credentials instead of copying them

Understanding kubeconfig reduces both mistakes and anxiety.

---

## Why This Mental Model Scales

Once this clicks:
- EKS/GKE/AKS configs make sense
- CI/CD kubeconfigs are less scary
- access rotation becomes manageable
- multi-cluster workflows are predictable

The file didn’t change—your understanding did.
