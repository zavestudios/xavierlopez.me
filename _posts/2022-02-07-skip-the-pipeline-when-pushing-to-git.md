---
layout: single
title: "Skip the Pipeline When Pushing to Git"
date: 2022-02-07 08:00:00 +0000
last_modified_at: "2025-01-02"
categories:
  - git
  - ci-cd
  - productivity
tags:
  - git
  - ci-cd
  - pipelines
  - gitlab
  - github
excerpt: "How to intentionally skip CI/CD pipelines when pushing to Git, when it’s appropriate to do so, and how to avoid accidental misuse."
toc: true
toc_sticky: true
---

## Context

CI/CD pipelines are essential—but not every push needs one.

There are legitimate cases where triggering a pipeline adds cost, noise, or delay without providing value. Knowing **how to skip a pipeline intentionally** gives engineers finer control over their workflows—especially in automation-heavy environments.

This post explains how pipeline skipping works and when it should (and shouldn’t) be used.

---

## When Skipping a Pipeline Makes Sense

Reasonable cases include:

- documentation-only changes
- formatting or comment updates
- experimental or temporary commits
- work-in-progress pushes
- branch housekeeping

Skipping pipelines is about **intent**, not avoidance.

---

## GitLab: Skip Pipeline via Commit Message

GitLab supports pipeline skipping through commit message directives.

Add one of the following to your commit message:

```
[skip ci]
```

or

```
[ci skip]
```

Example:

```
git commit -m "Fix typo in README [skip ci]"
```

When GitLab detects this token, it will not create a pipeline for the commit.

---

## GitHub Actions: Skip via Commit Message

GitHub Actions does **not** support skipping workflows via commit message by default.

However, many workflows include conditional logic such as:

```yaml
if: "!contains(github.event.head_commit.message, '[skip ci]')"
```

If your workflow is configured this way, adding `[skip ci]` to the commit message will prevent execution.

Always verify your repository’s workflow logic before relying on this behavior.

---

## Skipping Pipelines via Push Options (GitLab)

GitLab also supports push options:

```
git push -o ci.skip
```

This skips pipeline creation for that push without modifying commit messages.

This is especially useful when:

- commits are already created
- rewriting history is undesirable
- automation is involved

---

## Branch and Path-Based Skipping

Some pipelines are configured to skip runs based on:

- branch names
- changed file paths
- merge request context

Examples:

- only run pipelines on `main`
- ignore changes under `/docs`
- skip on tags

These approaches reduce the need for manual skipping.

---

## Risks and Pitfalls

Skipping pipelines can be dangerous if misused.

Common mistakes:

- skipping pipelines for functional changes
- bypassing required checks
- masking failing tests
- forgetting skip directives before merge

Pipelines exist to protect the system—don’t undermine them casually.

---

## Best Practices

- Use skipping sparingly and intentionally
- Prefer automated path-based rules where possible
- Avoid skipping on shared or protected branches
- Document expected usage for your team
- Treat skipped pipelines as an exception, not a norm

Good defaults reduce the need for manual intervention.

---

## CI Visibility and Auditing

Even when skipped:

- the commit is still recorded
- the skip directive is visible
- intent can be reviewed later

This transparency is important for audits and retrospectives.

---

## Practical Tips

- Use `[skip ci]` consistently if your platform supports it
- Prefer push options when available
- Don’t rely on undocumented behavior
- Test skip behavior in non-production repos
- Remember that merges may trigger pipelines even if commits didn’t

Understanding your CI platform’s behavior matters.

---

## Takeaways

- Not every commit needs a pipeline
- GitLab supports explicit skip directives
- GitHub requires workflow-level conditions
- Skipping should be intentional and limited
- Automation should reduce noise, not trust

Used thoughtfully, skipping pipelines can make CI/CD faster and quieter—without compromising safety.
