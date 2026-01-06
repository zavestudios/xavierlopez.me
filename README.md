# xavierlopez.me (Blog Repo)

This repo contains the source for my personal engineering blog (Jekyll / Minimal Mistakes).

The blog is intentionally written for platform engineers and adjacent roles (SRE, DevOps, security-minded infrastructure engineers). The style is “mental models first, implementation second.”

## Current Status

- The migration of legacy notes/posts into the current format is complete.
- CI guardrails are in place (build, lint, link checks, front matter validation, security scan).
- The blog is “done for now” in the sense that it is stable and publishable.

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

## Workflow

- Content lives in `_posts/`.
- Pages live in `_pages/` (or the site’s chosen pages dir).
- Local dev:
  - `bundle install`
  - `bundle exec jekyll serve`

## Conventions

- Posts include front matter: `title`, `date`, `last_modified_at`, `categories`, `tags`, `excerpt`, `toc`.
- Code fences always specify a language (e.g., `bash`, `yaml`, `ruby`, `text`).
- Avoid Markdown patterns that break rendering (no nested fences, no “mega-code-block posts”).

## Backlog Tracking

Work is tracked as GitHub Issues in this repo.
