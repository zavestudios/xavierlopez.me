# xavierlopez.me (Blog Repo)

This repo contains the source for my personal engineering blog (Jekyll / Minimal Mistakes).

**Repository Category:** `portfolio` (canonical classification in [REPO_TAXONOMY.md](https://github.com/zavestudios/platform-docs/blob/main/_platform/REPO_TAXONOMY.md))

**Contract Governance:** This repository is a contract-governed portfolio workload.
Canonical contract: [`zave.yaml`](./zave.yaml)

The blog is intentionally written for platform engineers and adjacent roles (SRE, DevOps, security-minded infrastructure engineers). The style is “mental models first, implementation second.”

## Current Status

- The migration of legacy notes/posts into the current format is complete.
- CI guardrails are in place (build, lint, link checks, front matter validation, security scan).
- The blog is “done for now” in the sense that it is stable and publishable.

## Part of ZaveStudios Platform

This application is deployed as a contract-governed static workload on the ZaveStudios platform.

**Platform integration:**

- Runtime profile: `spec.runtime: static`
- Exposure: `spec.exposure: public-http`
- Delivery strategy: `spec.delivery: rolling`
- Lifecycle authority: GitOps-managed deployment flow

## Next Actions (Backlog)

### Phase 1 — Light curation (no new writing required)

1. Create a **Start Here** page:

   - who this blog is for
   - how to use it
   - links to foundational posts

2. Add **light internal linking**:

   - connect obvious related posts (storage/auth/tooling/etc.)
   - avoid exhaustive linking; focus on the “reader path”
3. Identify **fundamentals / pillars**:

   - small set of posts that serve as long-term anchors
   - future posts should link back to these where relevant

### Phase 2 — Resume-driven editorial roadmap

The source for future posts will be my resume:

- Every major skill and experience area in the resume becomes a candidate post.
- The goal is not to rewrite the resume as prose, but to produce durable essays that demonstrate the underlying thinking.

Guiding principles:

- Use real experience as context, not as autobiography.
- Prefer “why this matters” and “how to think about it” over step-by-step tutorials.
- Write to be useful to peers, not to impress recruiters.

## Local Development

### Prerequisites

- Docker and Docker Compose
- Git

### Quick Start

- Copy the environment template:
  `cp .env.example .env`
- Start the site:
  `docker compose up`
- Open the site at `http://localhost:4000`

## Workflow

### Writing and Publishing

- Content lives in `_posts/`.
- Pages live in `_pages/` (or the site's chosen pages dir).
- Local dev:
  - `docker-compose up`

Alternative host workflow (optional, not primary):

- `bundle install`
- `bundle exec jekyll serve`

### Publishing Cadence

**Goal:** Publish at least one post every 2 weeks.

**Process:**

1. Draft posts are written on the `posts/unpublished` branch (branch is protected from deletion)
2. Every 2 weeks, review all posts on `posts/unpublished`
3. For each post, make a decision: **publish** or **delete**
   - No "hold" option — forces decision-making
   - If not ready to publish, either finish it now or delete it
4. To publish: cherry-pick post to main, merge, deploy
5. To delete: remove from `posts/unpublished` branch

**Tracking:** Set a recurring calendar reminder every 2 weeks: "Review unpublished posts"

This cadence ensures consistent publishing velocity and prevents draft accumulation.

## Conventions

- Posts include front matter: `title`, `date`, `last_modified_at`, `categories`, `tags`, `excerpt`, `toc`.
- Code fences always specify a language (e.g., `bash`, `yaml`, `ruby`, `text`).
- Avoid Markdown patterns that break rendering (no nested fences, no “mega-code-block posts”).

## Backlog Tracking

Work is tracked as GitHub Issues in this repo.
