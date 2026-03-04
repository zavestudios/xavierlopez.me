---
layout: single
title: "Working With AI Agents in a Platform Environment"
date: 2026-03-04T12:00:00-08:00
last_modified_at: 2026-03-04T12:00:00-08:00
categories: [platform, ai]
tags: [ai-agents, claude-code, platform-engineering, collaboration, governance]
excerpt: "How I learned to collaborate with AI agents while building ZaveStudios - a story about controlled delegation, instruction hierarchies, and maintaining human authority in governed systems."
toc: true
toc_sticky: true
---

## Introduction

Over the past few months, I've been building an internal developer platform called ZaveStudios with an unusual collaborator: Claude Code, an AI agent. This isn't a story about AI replacing platform engineers or automating away the need for human judgment. It's about something more nuanced — learning to work with a capable assistant within a system that has strong opinions about boundaries.

The platform wasn't designed for AI agents. It was designed with principles like explicit contracts, machine-readable governance, and clear authority boundaries. What I discovered is that those same principles that make a platform maintainable also make it agent-friendly.

## The Philosophy: Controlled Delegation

When I first started working with Claude, I had a question: how much authority should an AI agent have?

The answer I arrived at was: **enough to be useful, not enough to be dangerous**.

Agents in my workflow can read anything, write code, create branches, and propose changes through pull requests. What they cannot do is merge those changes, access production clusters directly, or bypass governance gates.

This creates what I call "controlled delegation" — the agent operates within the same constraints as any other developer on the platform. It's not a special case. It's just another contributor, albeit one with impressive productivity and perfect recall of documentation.

## The Workspace: Physical and Conceptual

I work from a single VS Code workspace that contains every repository in the ZaveStudios organization. The workspace file lives in my Dev directory alongside all the repos themselves — a flat structure where the workspace file orchestrates the logical grouping.

Each repository is cloned as a sibling directory. The workspace organizes them by category: control plane, infrastructure, platform services, tenant workloads, and portfolio sites. The folder names in VS Code carry prefixes like "control-plane", "infra-kubernetes", "tenant-panchito" — making the taxonomy visible in every file path.

This serves two purposes. For me, it's instant navigation. I can find what I need without thinking. For agents, it's context. When Claude reads a file path, it immediately knows whether it's looking at authoritative governance, infrastructure configuration, or a tenant application.

The taxonomy isn't just organizational convenience. It's architectural information that both humans and agents use to understand scope and impact.

## The Instruction Hierarchy

I use a two-layer system for configuring how agents work in my environment.

**Layer 1: Global preferences**

In my home directory, I maintain a file at `~/.claude/CLAUDE.md` that contains personal preferences applying to all projects, not just ZaveStudios. The main thing it does is tell agents to prefer CLI tools over MCP servers.

Why? Token efficiency.

MCP servers add persistent tool definitions to every request. GitHub MCP might add 50 tools, AWS MCP might add 200. Over a long session with hundreds of interactions, this compounds. CLI tools are ephemeral — they run, return results, and disappear without occupying context.

For operations like listing GitHub pull requests or checking AWS resources, the CLI is faster and cheaper. MCP is reserved for cases where CLI tools don't provide the functionality or where complex stateful operations justify the overhead.

This layer also contains guidance about Context7 MCP (for library documentation). Use it selectively — only for new libraries, version-specific details, or cases where my training data might be outdated. Don't use it for well-established libraries where the 10-15k token cost doesn't justify the benefit.

**Layer 2: Workspace contract**

At the root of my Dev directory (alongside all the repos and the workspace file), I maintain two files: `AGENTS.md` and `CLAUDE.md`. They contain identical content — the "Workspace Agent Contract".

Why two files? Compatibility. `AGENTS.md` is generic and works with any agent tool. `CLAUDE.md` is specific to Claude Code, which looks for this file by convention. The redundancy ensures agents always find the contract.

This contract defines:

- **Mandatory reads**: Eleven platform documents agents must read in sequence before acting
- **Authority constraints**: What agents can and cannot do (no kubectl, no direct cluster access, no merging)
- **Identity rules**: When to use my identity vs the agent identity
- **Workflow expectations**: How to handle single-repo vs cross-repo changes

The contract is prescriptive, not descriptive. It tells agents how to operate in this specific platform environment.

## The Mandatory Reads

The workspace contract requires agents to read eleven platform documents in a specific order:

1. Architectural Doctrine (the foundation — why the platform exists)
2. Repository Taxonomy (which repos do what)
3. Operating Model (what phase we're in — formation vs operation)
4. Control Plane Model (who has authority over what)
5. Contract Schema (the workload interface)
6. Contract Validation (how contracts are enforced)
7. Lifecycle Model (how workloads evolve)
8. Generator Model (how scaffolding works)
9. Developer Experience (local development standards)
10. Operating Model Validation (governance checkpoints)
11. PR Workflow (how to contribute changes)

This ordering matters. It builds understanding progressively — from principles to structure to mechanics to process.

By the time an agent reaches the PR workflow document, it has full context for why branches are mandatory, why main is protected, and why manual kubectl is prohibited. The rules aren't arbitrary. They're derived from the control plane model and the platform's authority boundaries.

In practice, Claude reads these automatically when it needs to understand repository context. The contract ensures it reads them in the correct order, not randomly based on what seems relevant in the moment.

## Authority Boundaries

The workspace contract explicitly lists what agents cannot do:

- No kubectl access
- No direct cluster access
- No merging pull requests
- No mutation of production state

Why these prohibitions?

They align with the platform's control plane model. GitOps is the state authority — kubectl bypasses Git, creating drift. Pull requests are review gates — direct merges bypass human approval. Production changes require human sign-off.

This creates a safe collaboration boundary. Agents can research, write code, and propose changes. Humans maintain authority over production mutations.

When an agent encounters a task requiring kubectl, it labels those steps "Run manually by human." This makes it explicit that I need to execute that step myself. The agent doesn't fail or complain — it just documents the handoff point.

## The Two-Identity Model

The workspace contract defines two identities for agent work.

**Default identity: Me (Xavier Lopez)**

For code changes, commits, branches, and pull requests, the agent uses my Git identity. This keeps contribution attribution on my GitHub profile.

When I collaborate with an agent to write a feature, the commit history shows my name as the primary author, with a co-authorship footer acknowledging Claude's involvement. The contribution graph remains accurate — I built this platform, with agent assistance.

**Agent identity: @zavestudios-agent**

For code reviews and certain automation tasks, I use a separate GitHub user account called `@zavestudios-agent`. This is a regular user account (not a GitHub App) that's a member of the organization and part of the "platform-governance-reviewers" team.

When I ask an agent to review a pull request for governance compliance, it uses this identity to post review comments. This makes it clear that the feedback is agent-generated, not human review.

Why a user account instead of a GitHub App? Simplicity. Apps require infrastructure — webhook endpoints, key management. A user account with team-based permissions is easier to maintain.

The two-identity model maintains clarity about who did what. Commits show human authorship. Reviews show agent assistance. There's no ambiguity.

## The Workflow: Request to Pull Request

A typical collaboration session flows like this:

I ask Claude to add a feature or fix something. The agent reads the workspace contract and loads the mandatory platform documents. It uses the repository taxonomy to identify which repos are affected. It determines whether the change is single-repo or cross-repo.

The agent creates a feature branch (never committing directly to main), writes the code, commits using my identity, pushes the branch, and creates a pull request with a detailed description.

Then it waits. I review the PR, approve if it looks good, and merge. The agent proposed, I decided.

This workflow ensures agents have full context before acting, changes follow taxonomy and lifecycle rules, and human review is mandatory before production impact.

## Cross-Repo Coordination

Single-repo changes are straightforward. Cross-repo changes require coordination.

If a feature requires updating the contract schema in the control plane repo and modifying validation logic in the platform pipelines repo, the agent:

1. Identifies all affected repositories (using the taxonomy)
2. Creates separate feature branches in each repo
3. Creates separate pull requests for each repo
4. Documents the dependency relationship in PR descriptions
5. Calls out merge order if sequencing matters

My responsibility is to review all PRs together, treating them as an atomic changeset, and merge in the correct order.

Why not a monorepo? The multi-repo structure reflects the platform's separation of concerns. Control plane defines doctrine. Platform services provide capabilities. Tenant repos are workload-specific.

A monorepo would collapse these boundaries. The taxonomy structure preserves them, at the cost of cross-repo coordination overhead. Agents make this overhead manageable by automating branch creation, PR generation, and dependency documentation.

## What Makes This Work

Several things enable productive human-agent collaboration in this environment:

**Explicitness over convention**

The platform documents everything — repository categories, contract schemas, authority boundaries, workflow rules. Agents can read these and understand the system. There's no hidden tribal knowledge.

**Machine-readable governance**

The workspace contract is structured instruction: ordered mandatory reads, explicit prohibitions, identity rules. Agents don't need to infer — they follow the contract.

**Pull requests as review gates**

All changes go through PRs. This creates a human approval checkpoint before production impact. Agents propose, humans decide.

**Identity separation**

Using two identities maintains accurate contribution attribution and clear signal about who did what.

**Taxonomy-driven navigation**

The workspace structure mirrors the taxonomy. Agents (and humans) can navigate by category without needing to memorize which repo does what.

**Token efficiency discipline**

Preferring CLI tools over MCP servers keeps context budgets manageable. Over hundreds of interactions, this matters.

## Limitations and Trade-offs

This model doesn't handle everything well.

**Break-glass scenarios** where production is on fire and I need immediate kubectl intervention — agents can't help. The workspace contract prohibits direct cluster access. Trade-off accepted: production safety over agent autonomy.

**Complex multi-stage cross-repo changes** involving five or more repos with intricate sequencing create significant coordination overhead. Trade-off accepted: repository separation preserves architectural boundaries. Coordination complexity is the cost.

**External system integration** — agents work within repos. They can't directly interact with external systems (AWS console, Kubernetes dashboard, monitoring tools) unless mediated through CLI tools or APIs. Trade-off accepted: this maintains the GitOps control plane model.

There's room for improvement. The `@zavestudios-agent` user currently uses my personal access token. A proper GitHub App would be more robust but requires infrastructure I haven't built yet. Cross-repo coordination could be automated with dependency declarations and CI checks that verify consistency. MCP server usage could be optimized with caching and lazy-loading.

But these are refinements, not blockers. The current model works.

## Conclusion

Working with AI agents in ZaveStudios is about amplifying human capability within governed boundaries.

The platform's architectural rigor — doctrine, taxonomy, contracts — creates a structured environment where agents can understand the system by reading authoritative documents, propose changes through pull requests, follow consistent workflows, and operate safely without direct production access.

The two-layer instruction system ensures agents have the right context and constraints. The two-identity model maintains accurate attribution while enabling flexible collaboration.

The result is a collaboration model where I maintain strategic authority (reviews, merges, production decisions), agents handle tactical execution (research, code writing, PR creation), and the platform's governance enforces safety automatically.

This isn't "AI replaces the platform engineer." This is "AI becomes a governed collaborator within the platform's control plane model."

And that's what makes it sustainable.
