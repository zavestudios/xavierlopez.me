---
layout: single
title: "Helm CLI: Practical Command Notes"
date: 2024-01-29 08:00:00 +0000
last_modified_at: "2025-01-02"
categories:
  - devops
  - development
tags:
  - devops
  - package-management
  - devops
excerpt: "A practical collection of Helm CLI commands for inspecting releases, managing charts, and debugging deployments in Kubernetes clusters."
toc: true
toc_sticky: true
---

## Context

Helm is the de facto package manager for Kubernetes, but most real-world usage revolves around a **small, repeatable set of commands**.

These notes focus on the Helm CLI commands that show up most often when:

- inspecting deployed releases
- debugging failed upgrades
- validating rendered manifests
- managing release state across namespaces

This is not a Helm tutorial—it’s a working engineer’s reference.

---

## Listing Helm Releases

List all releases in the current namespace:

```bash
helm list
```

List releases across all namespaces:

```bash
helm list --all-namespaces
```

This is usually the first command to run when you’re orienting yourself in a cluster.

---

## Inspecting a Helm Release

View detailed information about a release:

```bash
helm status example-release -n example-namespace
```

This shows:

- deployment status
- revision history
- notes from the chart
- associated resources

It’s often more useful than checking Kubernetes resources directly.

---

## Viewing Release Values

Get the values used by an installed release:

```bash
helm get values example-release -n example-namespace
```

Include all values (defaults + overrides):

```bash
helm get values example-release -n example-namespace --all
```

This is critical when debugging configuration drift or unexpected behavior.

---

## Rendering Manifests Locally

Render templates without installing:

```bash
helm template example-release ./example-chart
```

Render with explicit values:

```bash
helm template example-release ./example-chart \
  -f values.yaml \
  -n example-namespace
```

Local rendering is one of the fastest ways to debug Helm issues **before** touching the cluster.

---

## Installing and Upgrading Releases

Install a release:

```bash
helm install example-release ./example-chart -n example-namespace
```

Upgrade an existing release:

```bash
helm upgrade example-release ./example-chart -n example-namespace
```

Upgrade and install if missing:

```bash
helm upgrade --install example-release ./example-chart -n example-namespace
```

This pattern is common in CI/CD pipelines.

---

## Checking Release History

View revision history:

```bash
helm history example-release -n example-namespace
```

This is useful for:

- understanding rollout order
- identifying failed revisions
- preparing for rollbacks

---

## Rolling Back a Release

Rollback to a specific revision:

```bash
helm rollback example-release 3 -n example-namespace
```

Rollbacks reuse stored release data and are usually fast and reliable.

---

## Uninstalling a Release

Remove a release:

```bash
helm uninstall example-release -n example-namespace
```

This deletes:

- the Helm release record
- associated Kubernetes resources (unless otherwise configured)

Always confirm the namespace before uninstalling.

---

## Debugging Failed Deployments

Common debugging flow:

1. `helm status`
2. `helm get values`
3. `helm history`
4. `helm template`
5. Inspect Kubernetes events and pods

Helm failures are often **configuration or values issues**, not chart bugs.

---

## Practical Tips

- Always be explicit about namespaces
- Render templates locally before deploying
- Check release history before rolling back
- Treat values files as first-class config
- Avoid “helm install” without understanding defaults

Helm rewards inspection before action.

---

## Takeaways

- Helm usage centers on a small set of commands
- Release inspection explains most failures
- Local rendering prevents cluster-side mistakes
- History and rollback provide safety
- Clear Helm workflows reduce operational risk

For a concrete example of using Helm to install cluster infrastructure, see:  
[Installing the NFS Subdir External Provisioner with Helm](/2024/02/26/installing-nfs-subdir-external-provisioner-with-helm/)
