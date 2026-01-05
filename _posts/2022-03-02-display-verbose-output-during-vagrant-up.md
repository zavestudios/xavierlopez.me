---
layout: single
title: "Display Verbose Output During `vagrant up`"
date: 2022-03-02 08:00:00 +0000
last_modified_at: "2025-01-09"
categories:
  - virtualization
  - cli
  - troubleshooting
tags:
  - vagrant
  - virtualization
  - debugging
  - cli
excerpt: "How to enable verbose output during `vagrant up`, why it’s useful for debugging provisioning issues, and when increased verbosity is worth the noise."
toc: true
toc_sticky: true
---

## Context

When `vagrant up` fails, the default output often isn’t enough to explain *why*.

Provisioning issues, networking problems, provider misconfigurations, and plugin failures can all surface as vague errors. In those cases, **verbose output** becomes the fastest way to understand what Vagrant is actually doing under the hood.

This post shows how to enable verbose logging and how to use it effectively.

---

## Why Verbose Output Helps

Verbose output exposes:

- provider interactions (VirtualBox, VMware, libvirt)
- SSH connection attempts
- provisioning steps and hooks
- plugin execution
- internal decision paths

Without verbosity, many failures look identical—even when they’re not.

---

## Enabling Verbose Output

### Basic verbosity

Run `vagrant up` with the `--debug` flag:

```
vagrant up --debug
```

This enables detailed logging across Vagrant’s execution path.

---

### Redirecting Output to a File

Verbose output can be overwhelming. Redirecting it to a file makes it easier to inspect:

```
vagrant up --debug > vagrant-debug.log 2>&1
```

This captures:

- standard output
- error output
- debug logs

You can then search the log without rerunning the command.

---

## Increasing Log Detail with Environment Variables

Vagrant uses log levels internally.

You can explicitly control them:

```
VAGRANT_LOG=debug vagrant up
```

For even more detail:

```
VAGRANT_LOG=trace vagrant up
```

Use `trace` sparingly—it is extremely verbose.

---

## What to Look for in Debug Output

Key sections worth focusing on:

- provider initialization
- SSH key exchange and connection attempts
- provisioning scripts and exit codes
- network interface configuration
- plugin load errors

Search for:

- `ERROR`
- `WARN`
- `exit status`
- `timeout`

Noise is expected—patterns matter more than individual lines.

---

## Common Problems Revealed by Verbose Mode

Verbose output often surfaces:

- mismatched provider versions
- missing kernel modules
- SSH handshake failures
- provisioning scripts failing silently
- plugin compatibility issues

These problems are frequently invisible at default verbosity.

---

## When Verbose Output Is Especially Useful

Turn on verbosity when:

- `vagrant up` fails without explanation
- provisioning hangs indefinitely
- networking doesn’t behave as expected
- plugins behave inconsistently
- issues differ between hosts

Verbose logs make failures reproducible and diagnosable.

---

## When to Turn It Off

Verbose output is **not** ideal for:

- routine development workflows
- quick iteration loops
- normal provisioning

Use it as a diagnostic tool—not the default mode.

---

## Practical Tips

- Always capture logs when reporting issues
- Search logs instead of reading linearly
- Compare failing logs with known-good runs
- Remove secrets before sharing logs

Debug logs are powerful—and sensitive.

---

## Takeaways

- `--debug` reveals what Vagrant is actually doing
- Redirecting output makes logs manageable
- Environment variables allow finer control
- Verbose logs expose root causes, not guesses
- Use verbosity deliberately, not constantly

When Vagrant fails quietly, verbose output is usually where the truth lives.
