---
layout: single
title: "AWS CLI Notes: Inspecting IAM Accounts, Users, Groups, and Roles"
date: 2023-08-22 08:00:00 +0000
last_modified_at: "2024-12-14"
categories:
  - aws
  - iam
  - cli
tags:
  - aws-cli
  - iam
  - security
  - cloud
  - operations
excerpt: "Practical AWS CLI commands for inspecting IAM account state, users, groups, roles, and attached policies without relying on the AWS console."
toc: true
toc_sticky: true
---

## Context

When auditing or troubleshooting IAM in an AWS account, the web console is often **too slow and too abstract**. The AWS CLI provides a faster, more precise way to understand:
- who exists in the account
- what roles and groups are defined
- how policies are attached
- whether you’re approaching IAM limits

These notes capture a small but effective set of AWS CLI commands I’ve relied on when inspecting IAM state directly.

All examples assume a **fictional named CLI profile** is in use.

---

## Account-Level IAM Summary

To get a high-level view of IAM usage and limits for the current account:

```
aws iam get-account-summary --profile demo-admin
```

This returns counts and usage metrics for:
- users
- groups
- roles
- policies
- MFA devices
- access keys

This is often the fastest way to answer:
> “How big is this IAM footprint, really?”

---

## Full IAM Authorization Details

To retrieve detailed IAM configuration across the entire account:

```
aws iam get-account-authorization-details --profile demo-admin
```

This includes:
- users
- groups
- roles
- inline policies
- attached managed policies

It’s verbose, but useful when:
- auditing permissions
- exporting IAM state
- diffing environments
- feeding data into analysis tools

Expect a large JSON response.

---

## Listing IAM Users

To list all IAM users in the account:

```
aws iam list-users --profile demo-admin
```

This is helpful for:
- confirming legacy users still exist
- identifying service accounts
- verifying cleanup after migrations to roles or SSO

In mature environments, this list is often smaller than expected.

---

## Listing Groups for a Specific User

To see which groups a user belongs to:

```
aws iam list-groups-for-user \
  --user-name example-user \
  --profile demo-admin
```

Group membership often explains **effective permissions** more clearly than individual policies.

This is especially useful when:
- debugging unexpected access
- validating least-privilege changes
- tracing permission inheritance

---

## Listing Managed Policies Attached to a Group

To list managed policies attached to a specific IAM group:

```
aws iam list-attached-group-policies \
  --group-name PlatformAdmins \
  --profile demo-admin
```

This shows **only managed policies**, not inline policies.

If permissions feel broader than expected, this command usually reveals why.

---

## Listing IAM Roles

To list all IAM roles in the account:

```
aws iam list-roles --profile demo-admin
```

IAM roles typically outnumber users and are central to:
- EC2 instance permissions
- CI/CD pipelines
- cross-account access
- Kubernetes (IRSA)
- service integrations

This list grows quickly in active environments.

---

## Why the CLI Is Often Better Than the Console

For IAM inspection, the CLI provides:
- scriptability
- reproducibility
- auditability
- faster iteration
- clearer raw data

The console is useful for discovery, but the CLI is better for **understanding reality**.

---

## Practical Tips

- Always use named profiles to avoid account confusion
- Pipe output to `jq` for clarity when needed
- Save authorization details before making IAM changes
- Prefer inspection before modification
- Treat IAM state as code—even when exploring manually

IAM mistakes are rarely subtle. Visibility matters.

---

## Takeaways

- The AWS CLI is a powerful IAM inspection tool
- Account summaries reveal scale and limits quickly
- Group and role inspection explains most access paths
- CLI-based workflows scale better than console-only usage
- Clear visibility reduces security and operational risk

These commands form a solid baseline for understanding IAM state in any AWS account.
