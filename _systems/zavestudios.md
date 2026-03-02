---
title: "ZaveStudios"
excerpt: "Contract-driven platform demonstrating infrastructure-as-product and bounded declarative interfaces."
---

## Intent

ZaveStudios is a reference implementation demonstrating how platforms can work when infrastructure decisions are reduced to bounded declarative contracts.

Most platforms operate as evolving design spaces where every tenant makes infrastructure decisions. ZaveStudios constrains those decisions to a single contract file (`zave.yaml`), and the platform handles everything else—CI/CD, GitOps, database provisioning, observability, security.

This is not a product. It's a reference implementation showing platform-as-product thinking applied deliberately from formation.

---

## Problem Space

**Unbounded architectural variance** across workloads creates entropy, fragility, and platform teams that devolve into reactive support functions.

When every tenant repository has custom CI logic, unique deployment patterns, and bespoke infrastructure requests, platforms become unmaintainable. The solution isn't better ticket systems—it's structural constraint.

ZaveStudios eliminates variance in infrastructure composition while preserving autonomy in application logic.

---

## Architectural Philosophy

**Contracts over conventions.**
Requirements are explicit (`zave.yaml`), not inferred from repository structure or tribal knowledge.

**Declarative reconciliation.**
Tenants declare intent. The platform chooses how to satisfy based on environment. Same contract works in sandbox (libvirt/QEMU + k3s) and production target (AWS EKS).

**Governance encoded structurally.**
Contract validation happens at commit time. Schema violations block PRs. No manual review gates. No policy documents that drift from reality.

**Infrastructure portability.**
Kubernetes distribution, database engine, and cloud provider are replaceable without tenant code changes. Portability validates that abstractions work.

**Formation before optimization.**
Prove patterns work at reference scale before investing in generators. Manual scaffolding is acceptable during formation. Automation eliminates repetition only after patterns stabilize.

---

## Control Plane Model

ZaveStudios implements a **four-plane control architecture:**

**1. Contract Plane**
- Authority: `zave.yaml` in tenant repositories
- Tenants declare: runtime, persistence, exposure, delivery
- Single source of requirements

**2. CI Plane**
- Authority: `platform-pipelines` shared workflows
- Validates contracts, builds images, semantic versioning
- Triggers GitOps updates

**3. GitOps Plane**
- Authority: `gitops` repository (Flux + ArgoCD)
- Declarative cluster state in Git
- Reconciliation loops ensure cluster matches declared state

**4. Runtime Plane**
- Authority: Kubernetes cluster + shared infrastructure
- Namespace isolation per tenant
- Database isolation (schema-per-tenant)
- Observability, security, service mesh via BigBang

No tenant has direct cluster access. All mutations flow through: Contract → CI → GitOps → Runtime.

---

## Current State: Formation Phase

The platform is in **Formation Phase**, focused on:

- Surface stabilization (contract schema, repository taxonomy)
- Reference implementation (6 tenant workloads operational)
- Manual Conformance Mode (scaffolding manual until generators implemented)
- Multi-tenant database architecture validation

**Exit criteria:**
- ≥80% of workloads deploy via contract without repo design decisions
- Contract schema stable for 90 days (no breaking changes)
- Generator automation operational (Stages 1-3)
- Multi-tenant database architecture proven

No revenue dependencies. No customer commitments. Just deliberate architecture and patient execution.

---

## Implementation Repositories

**Canonical documentation and governance:**
- [platform-docs](https://github.com/zavestudios/platform-docs) - Platform operating model, architectural doctrine, contract schema, lifecycle model, generator specifications

**Active repositories:**
- [platform-pipelines](https://github.com/zavestudios/platform-pipelines) - Shared CI/CD workflows
- [gitops](https://github.com/zavestudios/gitops) - GitOps state (Flux + ArgoCD)
- [kubernetes-platform-infrastructure](https://github.com/zavestudios/kubernetes-platform-infrastructure) - Cluster definitions
- [pg](https://github.com/zavestudios/pg) - Multi-tenant PostgreSQL provisioning
- [image-factory](https://github.com/zavestudios/image-factory) - Base container images

**Tenant workloads:**
- [mia](https://github.com/zavestudios/mia) - AI assistant (Formation)
- [panchito](https://github.com/zavestudios/panchito) - Real estate ETL (Python, Flask, Celery)
- [rigoberta](https://github.com/zavestudios/rigoberta) - Rails reference template
- [thehouseguy](https://github.com/zavestudios/thehouseguy) - Real estate listings (Rails)
- [oracle](https://github.com/zavestudios/oracle) - Market analysis service
- [data-pipelines](https://github.com/zavestudios/data-pipelines) - Data orchestration

**Public site:**
- [zavestudios.com](https://zavestudios.com) - Narrative entry point and philosophy

---

## Related Writing

Essays exploring platform engineering concepts demonstrated in ZaveStudios:

- [Operational Guardrails for Multi-Tenant Postgres](/writing/operational-guardrails-for-multi-tenant-postgres/) - Database isolation patterns
- [Building Production-Grade k3s Cluster on Spare Capacity](/writing/building-production-grade-k3s-cluster-on-spare-capacity/) - Infrastructure portability validation

---

**Note:** This page explains architectural intent and philosophy. Implementation details, contracts, and configuration live in GitHub repositories linked above.
