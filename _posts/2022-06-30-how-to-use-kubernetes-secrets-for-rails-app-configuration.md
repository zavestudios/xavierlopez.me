---
layout: single
title: "Using Kubernetes Secrets for Rails Application Configuration"
date: 2022-06-30 09:05:00 +0000
last_modified_at: "2025-01-14"
categories:
  - kubernetes
  - application-configuration
  - security
tags:
  - kubernetes
  - secrets
  - rails
  - configuration
  - twelve-factor
excerpt: "How to configure a Rails application using Kubernetes Secrets, why this pattern works well in containerized environments, and what pitfalls to avoid."
toc: true
toc_sticky: true
---

## Context

Rails applications have always needed configuration:
- database credentials
- API keys
- encryption secrets
- environment-specific settings

In containerized environments, baking this information into images or committing it to source control quickly becomes unsafe and inflexible.

Kubernetes Secrets provide a **runtime configuration mechanism** that aligns well with Rails and modern deployment practices—when used correctly.

---

## Why Kubernetes Secrets Work Well for Rails

Rails already expects configuration to arrive via **environment variables**.

This aligns naturally with:
- the Twelve-Factor App methodology
- container immutability
- environment-specific deployments

Kubernetes Secrets allow you to:
- decouple configuration from images
- rotate credentials without rebuilding
- keep sensitive data out of Git
- scope access tightly via RBAC

---

## What Belongs in a Secret (and What Doesn’t)

Good candidates for Secrets:
- database passwords
- Rails `SECRET_KEY_BASE`
- third-party API keys
- encryption credentials

Poor candidates:
- non-sensitive configuration
- feature flags
- large blobs of data
- application logic

If it wouldn’t be a problem to leak, it probably doesn’t belong in a Secret.

---

## Creating a Kubernetes Secret

Secrets can be created imperatively or declaratively.

### Imperative example

```bash
kubectl create secret generic rails-secrets \
  --from-literal=DATABASE_PASSWORD=supersecret \
  --from-literal=SECRET_KEY_BASE=longrandomstring
```

This is quick, but not ideal for versioned infrastructure.

---

### Declarative example (recommended)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: rails-secrets
type: Opaque
stringData:
  DATABASE_PASSWORD: supersecret
  SECRET_KEY_BASE: longrandomstring
```

Declarative secrets integrate cleanly with GitOps workflows (with proper encryption or secret management).

---

## Injecting Secrets into a Rails Pod

### As Environment Variables

This is the most common and Rails-friendly approach.

```yaml
env:
  - name: DATABASE_PASSWORD
    valueFrom:
      secretKeyRef:
        name: rails-secrets
        key: DATABASE_PASSWORD
  - name: SECRET_KEY_BASE
    valueFrom:
      secretKeyRef:
        name: rails-secrets
        key: SECRET_KEY_BASE
```

Rails will automatically read these via `ENV`.

---

### As a Group

For larger sets of values:

```yaml
envFrom:
  - secretRef:
      name: rails-secrets
```

This keeps manifests cleaner but makes it easier to accidentally expose unused values.

---

## Configuring Rails to Use Environment Variables

In `config/database.yml`:

```yaml
production:
  adapter: postgresql
  database: myapp_production
  username: myapp
  password: <%= ENV["DATABASE_PASSWORD"] %>
  host: db.example.com
```

For secrets like `SECRET_KEY_BASE`, Rails already expects an environment variable in production.

---

## Secret Rotation and Deployments

Kubernetes does **not** automatically restart pods when Secrets change.

Common patterns:
- manually restart deployments
- trigger rollouts via CI/CD
- annotate pods to force restarts

Plan for rotation explicitly—don’t assume it happens automatically.

---

## Security Considerations

### Access Control

Secrets are only as secure as:
- namespace boundaries
- RBAC policies
- who can read them

Avoid:
- granting `get secrets` broadly
- using default service accounts
- sharing namespaces unnecessarily

---

### Visibility and Leakage

Remember:
- environment variables can appear in logs
- crash dumps may include env state
- anyone with pod exec access can read them

Secrets reduce risk—but don’t eliminate it.

---

## Alternatives and Complements

Kubernetes Secrets are often combined with:
- external secret managers (Vault, AWS Secrets Manager)
- sealed secrets
- encrypted GitOps workflows

For higher-risk environments, native Secrets are a building block—not the entire solution.

---

## Common Failure Modes

| Symptom | Likely Cause |
|------|-------------|
| App fails to boot | Missing secret or typo |
| Works locally, fails in prod | Secret not mounted |
| Secret updated, app unchanged | Pod not restarted |
| Credentials leaked | Over-permissive access |

Most issues are operational, not Rails-specific.

---

## Takeaways

- Rails aligns naturally with env-based configuration
- Kubernetes Secrets decouple config from images
- Declarative management improves safety
- Rotation requires explicit action
- RBAC determines real security boundaries

Used carefully, Kubernetes Secrets provide a clean, scalable way to manage Rails configuration in production.
