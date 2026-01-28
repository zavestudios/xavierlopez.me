---
layout: single
title: "Kubernetes Cheatsheet: Practical kubectl Commands"
date: 2022-03-11 08:00:00 +0000
last_modified_at: "2025-01-10"
categories:
  - devops
  - cli
  - productivity
tags:
  - devops
  - kubectl
  - devops
  - troubleshooting
  - devops
excerpt: "A practical Kubernetes cheatsheet focused on kubectl commands and patterns you actually use when operating clusters and debugging workloads."
toc: true
toc_sticky: true
---

## Context

Kubernetes has a large surface area, but day-to-day operations rely on a **small, repeatable set of kubectl commands**.

This cheatsheet emphasizes:

- inspection over modification
- safety before speed
- commands that scale from dev clusters to production

It’s meant to be referenced, not memorized.

---

## Cluster and Context

View current context:

```bash
kubectl config current-context
```

List contexts:

```bash
kubectl config get-contexts
```

Switch context:

```bash
kubectl config use-context my-context
```

Always confirm context before making changes—many incidents start here.

---

## Namespaces

List namespaces:

```bash
kubectl get ns
```

Set a default namespace for the current context:

```bash
kubectl config set-context --current --namespace=my-namespace
```

Explicit namespaces reduce accidental cross-environment changes.

---

## Pods

List pods:

```bash
kubectl get pods
```

List pods with more detail:

```bash
kubectl get pods -o wide
```

Describe a pod:

```bash
kubectl describe pod my-pod
```

View pod logs:

```bash
kubectl logs my-pod
```

Follow logs:

```bash
kubectl logs -f my-pod
```

Logs and describe usually tell you more than guessing.

---

## Containers Inside Pods

Execute a shell:

```bash
kubectl exec -it my-pod -- /bin/sh
```

For multi-container pods:

```bash
kubectl exec -it my-pod -c my-container -- /bin/sh
```

Know which container you’re debugging.

---

## Deployments

List deployments:

```bash
kubectl get deployments
```

Describe a deployment:

```bash
kubectl describe deployment my-deployment
```

Check rollout status:

```bash
kubectl rollout status deployment my-deployment
```

Restart a deployment:

```bash
kubectl rollout restart deployment my-deployment
```

Rollouts provide safer change visibility than manual restarts.

---

## Services

List services:

```bash
kubectl get svc
```

Describe a service:

```bash
kubectl describe svc my-service
```

View endpoints:

```bash
kubectl get endpoints my-service
```

Service issues are often endpoint issues.

---

## Nodes

List nodes:

```bash
kubectl get nodes
```

Describe a node:

```bash
kubectl describe node my-node
```

Check node resource usage:

```bash
kubectl top node
```

Node health underpins everything else.

---

## Resource Usage

Check pod resource usage:

```bash
kubectl top pod
```

For a specific namespace:

```bash
kubectl top pod -n my-namespace
```

Resource pressure explains many “random” failures.

---

## Events

View recent events:

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

Events often explain:

- scheduling failures
- image pull issues
- permission problems

They’re one of the most underused debugging tools.

---

## Applying and Inspecting Manifests

Apply a manifest:

```bash
kubectl apply -f file.yaml
```

Dry-run before applying:

```bash
kubectl apply -f file.yaml --dry-run=client
```

View rendered resources:

```bash
kubectl get -f file.yaml
```

Prefer `apply` over imperative commands for repeatability.

---

## Deleting Resources (Be Careful)

Delete by name:

```sql
kubectl delete pod my-pod
```

Delete from a manifest:

```sql
kubectl delete -f file.yaml
```

Deletion is irreversible—confirm scope first.

---

## Debugging Patterns

Common workflow:

1. `kubectl get`
2. `kubectl describe`
3. `kubectl logs`
4. `kubectl exec`
5. `kubectl get events`

Skipping steps usually costs time.

---

## Practical Tips

- Alias frequently used commands (`k=kubectl`)
- Always know your context and namespace
- Read before you write
- Prefer inspection over intervention
- Let the cluster tell you what’s wrong

Kubernetes is verbose—listen to it.

---

## Takeaways

- kubectl is primarily an inspection tool
- A small command set covers most operational needs
- Events and describe output are critical
- Context mistakes cause real incidents
- Calm, repeatable workflows beat heroics

Comfort with kubectl turns Kubernetes from intimidating to manageable.
