---
layout: single
title: "RVM Cheatsheet: Practical Ruby Version Management"
date: 2022-02-28 08:00:00 +0000
last_modified_at: "2025-01-08"
categories:
  - development
  - cli
  - productivity
tags:
  - rvm
  - development
  - version-management
  - development
excerpt: "A practical RVM cheatsheet covering the commands you actually use to install, switch, and manage Ruby versions and gemsets."
toc: true
toc_sticky: true
---

## Context

Ruby projects often depend on **specific Ruby versions and gem sets**.

RVM (Ruby Version Manager) helps isolate those dependencies so:

- projects don’t conflict
- upgrades are controlled
- development environments stay predictable

This cheatsheet focuses on **everyday RVM commands**, not edge cases.

---

## Installing and Listing Ruby Versions

List available Ruby versions:

```bash
rvm list known
```

Install a specific version:

```bash
rvm install 3.2.2
```

List installed versions:

```bash
rvm list
```

Set a default Ruby:

```bash
rvm --default use 3.2.2
```

---

## Switching Ruby Versions

Use a Ruby version for the current shell:

```bash
rvm use 3.2.2
```

Use a Ruby version temporarily:

```bash
rvm use 3.1.4 --temporary
```

Check the active Ruby:

```bash
ruby -v
```

Always confirm which Ruby you’re running before debugging issues.

---

## Gemsets

Gemsets isolate dependencies within a Ruby version.

Create a gemset:

```sql
rvm gemset create myapp
```

Use a gemset:

```bash
rvm gemset use myapp
```

List gemsets:

```bash
rvm gemset list
```

Delete a gemset:

```sql
rvm gemset delete myapp
```

Gemsets prevent dependency bleed between projects.

---

## Project-Level Ruby Configuration

Create a `.ruby-version` file:

```bash
echo "3.2.2" > .ruby-version
```

Create a `.ruby-gemset` file:

```bash
echo "myapp" > .ruby-gemset
```

When entering the directory, RVM will prompt to trust and switch automatically.

---

## Updating and Maintenance

Update RVM itself:

```bash
rvm get stable
```

Upgrade Ruby:

```bash
rvm upgrade 3.1.4 3.2.2
```

Remove an old Ruby version:

```bash
rvm remove 2.7.8
```

Cleaning unused versions reduces confusion.

---

## Bundler Integration

Install Bundler for the active Ruby:

```bash
gem install bundler
```

Install project dependencies:

```bash
bundle install
```

Bundler respects the active Ruby and gemset.

---

## Debugging Common Issues

Reload RVM environment:

```bash
source ~/.rvm/scripts/rvm
```

Check RVM requirements:

```bash
rvm requirements
```

Diagnose environment issues:

```bash
rvm doctor
```

Many Ruby issues trace back to mismatched versions or gemsets.

---

## Shell Integration Notes

RVM modifies shell behavior.

Common issues arise when:

- shells aren’t loading RVM scripts
- multiple version managers are installed
- PATH order is incorrect

Avoid mixing RVM with other Ruby managers unless you understand the interactions.

---

## Practical Tips

- Keep Ruby versions explicit per project
- Remove versions you no longer need
- Use gemsets sparingly but intentionally
- Trust `.ruby-version` files only from known sources
- Verify environment before debugging app errors

Environment clarity saves hours.

---

## Takeaways

- RVM manages Ruby versions and gem isolation
- A small command set covers most workflows
- Project-level files improve consistency
- Most Ruby issues start with environment drift
- Discipline beats memorization

A clean Ruby environment makes application problems much easier to reason about.
