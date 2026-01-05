---
layout: single
title: "Kubernetes ServiceAccount Tokens and CI/CD Authentication"
date: 2024-03-05 08:00:00 +0000
last_modified_at: 2025-01-11
categories:
  - kubernetes
  - security
  - ci-cd
tags:
  - kubernetes
  - serviceaccounts
  - authentication
  - kubeconfig
  - cicd
excerpt: "A practical explanation of how Kubernetes ServiceAccount authentication works for CI/CD systems, what changed in Kubernetes 1.24, and why previously working pipelines broke."
toc: true
toc_sticky: true
---

## Context

CI/CD systems frequently need non-interactive access to Kubernetes clusters.

Historically, this was straightforward:
- create a ServiceAccount
- bind it with RBAC
- extract a token
- embed it in a kubeconfig
- deploy

In Kubernetes 1.24 and later, that workflow quietly broke.

---

## How CI/CD Auth to Kubernetes Works

In a CI/CD environment:
- the job runs outside the cluster
- it uses a kubeconfig file
- the kubeconfig authenticates as a ServiceAccount
- Kubernetes evaluates RBAC rules for that identity

This requires a long-lived credential.

---

## How ServiceAccount Tokens Used to Work

Before Kubernetes 1.24:
- ServiceAccounts automatically created token Secrets
- tokens were long-lived
- stored as Kubernetes Secrets
- easy to extract for CI usage

Many pipelines relied on this behavior.

---

## What Changed in Kubernetes 1.24

Starting in Kubernetes 1.24:
- token Secrets are no longer auto-created
- Kubernetes uses bound ServiceAccount tokens
- tokens are short-lived
- projected only into pods
- not stored as Secrets

This improves security but breaks external CI workflows.

---

## Why CI/CD Pipelines Break

CI systems:
- run outside the cluster
- cannot receive projected tokens
- cannot refresh short-lived credentials

The ServiceAccount exists.
RBAC is correct.
But no token exists to authenticate with.

---

## Detecting the Issue

You can confirm this by inspecting the ServiceAccount:

    kubectl get serviceaccount deployer-service-account -o jsonpath='{.secrets}'

If the output is empty, no token Secret exists.

---

## Bound Tokens vs Secret Tokens

Bound tokens:
- short-lived
- pod-scoped
- secure by default
- unsuitable for external CI

Secret-based tokens:
- long-lived
- manually created
- usable by CI systems
- require explicit lifecycle management

---

## Creating a Token Secret Explicitly

When CI access is required, a token Secret can be created manually:

    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: deployer-sa-token
      annotations:
        kubernetes.io/service-account.name: deployer-service-account
    type: kubernetes.io/service-account-token
    EOF

Kubernetes will populate the token automatically.

---

## Security Implications

Manually created tokens:
- reintroduce long-lived credentials
- require rotation discipline
- increase blast radius if leaked

They should be treated as exceptions, not defaults.

---

## Modern Alternatives

More robust approaches include:
- OIDC federation
- cloud IAM integrations
- exec-based kubeconfig plugins
- workload identity systems

These eliminate static tokens entirely.

---

## Practical Guidance

- do not assume ServiceAccounts have tokens
- distinguish authentication from authorization
- validate permissions with kubectl auth can-i
- treat long-lived tokens as transitional

The system did not break.
The defaults changed.
The model finally caught up with security reality.
