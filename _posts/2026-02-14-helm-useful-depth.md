---

layout: single
title: "Deterministic Systems Can Still Be Illegible: A Lesson from Flux, BigBang, and Helm"
date: 2026-02-14T22:20:00-08:00
last_modified_at: 2026-02-14T22:20:00-08:00
categories: [operations, platform]
tags: [gitops, flux, helm, bigbang, platform-engineering, mental-models]
excerpt: "Modern GitOps stacks are composed of deterministic tools, yet the resulting system can still be opaque. The problem is not randomness — it is boundary visibility."
toc: true
toc_sticky: true
---

## Context

While working through a BigBang deployment, I set out to understand how Helm charts were resolving configuration. The assumption was straightforward: Helm must be the source of complexity. If I could trace value precedence through charts, the system would become predictable.

Instead, the exercise revealed something more interesting. Helm was not the source of confusion at all. The opacity came from how multiple deterministic systems were composed together.

The deployment stack looked roughly like this:

| Layer      | Responsibility           | What it actually controls               |
| ---------- | ------------------------ | --------------------------------------- |
| Flux       | Repository orchestration | which charts run and with which values  |
| BigBang    | Platform composition     | how packages are configured and related |
| Helm       | Template evaluation      | how values merge and manifests render   |
| Kubernetes | Execution                | how resources behave once applied       |

Each tool is internally consistent. The difficulty arises because none of them expose their reasoning across boundaries.

## Mental Model

It is tempting to think of Helm as the root of deployment logic. In practice, Helm is only the final interpreter in a larger pipeline.

The evaluation sequence is closer to this:

| Phase                 | System     | What happens                                        |
| --------------------- | ---------- | --------------------------------------------------- |
| Repository resolution | Flux       | determines which charts and values enter the system |
| Platform wiring       | BigBang    | injects global configuration and package defaults   |
| Template evaluation   | Helm       | merges values and renders manifests                 |
| Resource execution    | Kubernetes | enforces the declared state                         |

Helm does not decide what charts exist or which values are authoritative. By the time Helm runs, most structural decisions have already been made upstream.

That means debugging Helm first is often backwards.

## Observation

The difficulty in GitOps environments is not non-determinism. It is lack of observability across system boundaries.

During inspection, several facts became clear:

| Observation                                     | Implication                                                      |
| ----------------------------------------------- | ---------------------------------------------------------------- |
| Helm charts often have shallow dependency trees | most complexity lives in values and orchestration, not subcharts |
| Flux determines which charts even run           | the real execution graph begins before Helm                      |
| BigBang injects configuration implicitly        | value lineage frequently originates outside the chart itself     |
| Rendered manifests show outcomes, not decisions | tracing backwards requires cross-layer visibility                |

The system behaves predictably. It simply does not make its reasoning visible.

## Technique

Instead of tracing templates upward from manifests, start tracing configuration downward from orchestration inputs.

A more effective inspection workflow looks like this:

| Step                             | Question answered                       |
| -------------------------------- | --------------------------------------- |
| Identify Flux inputs             | what charts and values enter the system |
| Locate platform overrides        | what BigBang injects or modifies        |
| Render once with Helm            | what final state Helm produces          |
| Inspect templates only if needed | how specific values were transformed    |

This mirrors the actual execution path. It treats Helm as an interpreter, not as the source of truth.

Once configuration lineage is known, template inspection becomes a confirmation step rather than an exploratory one.

## Implication

Modern platform stacks are increasingly composed of layered tools, each deterministic in isolation. When those tools are combined, determinism alone does not guarantee legibility.

A system can be perfectly predictable and still feel opaque if:

| Condition                             | Result                                     |
| ------------------------------------- | ------------------------------------------ |
| Decision boundaries are hidden        | engineers cannot see why outcomes occurred |
| Configuration flows cross tools       | lineage becomes fragmented                 |
| Orchestration precedes interpretation | debugging starts in the wrong place        |

This suggests that platform engineering is less about simplifying tools and more about exposing the evaluation path between them.

## Closing Thought

Complex systems rarely become understandable by adding more tooling. They become understandable when their decision paths are made visible.

Flux, BigBang, and Helm all behave deterministically. The challenge is not randomness, but visibility.

Once the execution path is clear, the system stops feeling magical and starts feeling mechanical — and mechanical systems are the ones we can reason about.
