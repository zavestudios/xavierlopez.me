# xavierlopez.me

This repository contains Xavier Lopez's professional platform-engineering portfolio, built with Jekyll and Minimal Mistakes.

**Repository Category:** `portfolio` (canonical classification in [REPO_TAXONOMY.md](https://github.com/zavestudios/platform-docs/blob/main/_platform/REPO_TAXONOMY.md))

**Contract Governance:** This repository is a contract-governed portfolio workload.
Canonical contract: [`zave.yaml`](./zave.yaml)

The site introduces Xavier's platform-engineering work, selected career outcomes, and independent ZaveStudios practice. Legacy technical writing remains available as an archive, not the primary site purpose.

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

### Content

- Portfolio pages live in `_pages/`.
- Legacy posts live in `_posts/` and `_writing/`; their public URLs are preserved.
- The maintained public portfolio and resume surface lives in this repository.
- Use `docker compose up` for local development.

## Conventions

- Posts include front matter: `title`, `date`, `last_modified_at`, `categories`, `tags`, `excerpt`, `toc`.
- Code fences always specify a language (e.g., `bash`, `yaml`, `ruby`, `text`).
- Avoid Markdown patterns that break rendering (no nested fences, no “mega-code-block posts”).

## Backlog Tracking

Work is tracked as GitHub Issues in this repo.
