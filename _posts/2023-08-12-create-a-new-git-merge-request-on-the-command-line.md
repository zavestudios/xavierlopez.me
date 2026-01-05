---
layout: single
title: "Create a New Git Merge Request from the Command Line"
date: 2023-08-12 09:15:00 +0000
last_modified_at: "2025-01-29"
categories:
  - git
  - workflow
  - automation
tags:
  - git
  - merge-request
  - cli
  - ci-cd
  - developer-workflow
excerpt: "A practical guide to creating Git merge requests directly from the command line, streamlining review workflows without leaving the terminal."
toc: true
toc_sticky: true
---

## Context

If you spend most of your day in a terminal, switching to a web UI just to open a merge request feels unnecessary.

For many teams—especially those working in CI/CD-heavy environments—**creating merge requests from the command line** reduces friction, keeps context local, and speeds up feedback loops.

This post focuses on practical, repeatable ways to open merge requests without breaking flow.

---

## Why Create Merge Requests from the CLI?

Creating merge requests from the command line helps when:

- you already have a clean local branch
- CI is triggered automatically on push
- your workflow is terminal-centric
- you want to script or automate parts of the process

It’s not about avoiding the UI entirely—it’s about **starting the workflow efficiently**.

---

## Prerequisites

Before proceeding, ensure:

- your branch is pushed to the remote
- your repository is hosted on a platform that supports CLI-based MR creation (e.g., GitLab)
- authentication is already configured (SSH keys or tokens)

The CLI assumes identity and access are already solved.

---

## Basic Workflow (Push First)

At minimum, you need to push your branch:

```bash
git push -u origin my-feature-branch
```

Most platforms will detect the new branch and offer a merge request link automatically.

This alone is often enough.

---

## GitLab: Creating a Merge Request via CLI

GitLab provides built-in support for creating merge requests directly from the CLI.

### Push and create a merge request

```bash
git push -o merge_request.create origin my-feature-branch
```

Optional flags allow you to:
- set the target branch
- assign reviewers
- mark the MR as draft

Example:

```bash
git push -o merge_request.create \
         -o merge_request.target=main \
         -o merge_request.draft \
         origin my-feature-branch
```

This creates the merge request immediately after pushing.

---

## Why This Works Well in CI/CD Environments

This approach fits naturally into automation-heavy workflows:

- branch push triggers pipelines
- merge request is created deterministically
- no manual UI steps
- easy to document and standardize

It’s especially useful when:
- working across many repos
- enforcing consistent MR metadata
- scripting developer workflows

---

## Using CLI Tools (Optional)

Some platforms offer dedicated CLI tools (e.g., `glab` for GitLab).

These tools can:
- create merge requests
- set labels and reviewers
- open MRs in the browser if needed

They’re helpful, but not required—the native `git push` options are often sufficient.

---

## Common Failure Modes

### Authentication Errors

If MR creation fails:
- verify SSH access
- check token scopes
- confirm repository permissions

The push may succeed while MR creation fails.

---

### Target Branch Mismatch

If the MR targets the wrong branch:
- explicitly specify the target
- don’t rely on defaults unless standardized

Implicit defaults cause surprises.

---

### Over-automation

Automating MR creation is helpful—but not every branch needs an MR.

Avoid:
- auto-creating MRs for experiments
- flooding reviewers
- bypassing review intent

Automation should reduce friction, not noise.

---

## When the UI Is Still Better

Use the web UI when:
- crafting detailed descriptions
- attaching screenshots or artifacts
- adjusting reviewers dynamically
- reviewing pipeline results

CLI creation is a **starting point**, not a replacement for collaboration.

---

## Takeaways

- Creating merge requests from the CLI keeps workflow fast
- `git push` options are often all you need
- This approach integrates cleanly with CI/CD
- Automation should support intent, not replace it
- The terminal can be a first-class interface for collaboration

If your workflow starts in the terminal, there’s no reason your merge requests can’t start there too.
