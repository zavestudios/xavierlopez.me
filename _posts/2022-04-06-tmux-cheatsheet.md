---
layout: single
title: "tmux Cheatsheet: Practical Commands for Daily Use"
date: 2022-04-06 08:20:00 +0000
last_modified_at: "2025-01-16"
categories:
  - development
  - productivity
tags:
  - tmux
  - terminal
  - productivity
  - ssh
  - workflows
excerpt: "A practical tmux cheatsheet focused on the commands and patterns you actually use when living in terminals and remote systems."
toc: true
toc_sticky: true
---

## Context

`tmux` is one of those tools that quietly becomes indispensable.

If you:

- work over SSH
- manage multiple shells
- run long-lived processes
- juggle several environments at once

then `tmux` is less a convenience and more a survival tool.

This cheatsheet focuses on **high-signal commands** you’ll use repeatedly, not exhaustive coverage.

---

## Basic Concepts (Quick Refresher)

- **Session**: a collection of windows
- **Window**: similar to a terminal tab
- **Pane**: a split within a window
- **Prefix key**: default is `Ctrl-b`

Almost all commands start with the prefix.

---

## Sessions

Create a new session:

```bash
tmux new -s mysession
```

List sessions:

```bash
tmux ls
```

Attach to a session:

```bash
tmux attach -t mysession
```

Detach from session:

```bash
Ctrl-b d
```

Rename the current session:

```bash
Ctrl-b $
```

Sessions are what make `tmux` powerful over unreliable connections.

---

## Windows

Create a new window:

```bash
Ctrl-b c
```

List windows:

```bash
Ctrl-b w
```

Rename current window:

```bash
Ctrl-b ,
```

Switch to window by number:

```bash
Ctrl-b 0
Ctrl-b 1
```

Windows are best used to separate **tasks**, not layouts.

---

## Panes

Split horizontally:

```bash
Ctrl-b "
```

Split vertically:

```bash
Ctrl-b %
```

Move between panes:

```bash
Ctrl-b ← ↑ → ↓
```

Resize panes:

```bash
Ctrl-b Ctrl-←
Ctrl-b Ctrl-→
Ctrl-b Ctrl-↑
Ctrl-b Ctrl-↓
```

Close the current pane:

```bash
Ctrl-b x
```

Panes are ideal for **contextual work**, not permanent separation.

---

## Copy Mode (Scrolling and Selection)

Enter copy mode:

```bash
Ctrl-b [
```

Navigate using:

- arrow keys
- Page Up / Page Down
- Vim-style keys (if configured)

Start selection:

```bash
Space
```

Copy selection:

```bash
Enter
```

Paste buffer:

```bash
Ctrl-b ]
```

Copy mode is essential when reviewing logs or command output.

---

## Search in Output

Inside copy mode:

```bash
/
```

Then type your search string and press Enter.

Repeat search:

```bash
n
```

Searching output beats rerunning commands—especially in production.

---

## Pane and Window Management

Swap panes:

```bash
Ctrl-b {
Ctrl-b }
```

Break pane into a new window:

```bash
Ctrl-b !
```

Kill the current window:

```bash
Ctrl-b &
```

Reorganizing layouts quickly is one of tmux’s biggest strengths.

---

## Status and Information

Show time:

```bash
Ctrl-b t
```

Display pane numbers:

```bash
Ctrl-b q
```

Reload tmux config:

```bash
Ctrl-b :source-file ~/.tmux.conf
```

Useful when iterating on configuration.

---

## Working Over SSH

A common pattern:

- start tmux on the remote host
- attach once
- leave it running indefinitely

If your connection drops:

- reconnect
- reattach
- everything is still there

This alone justifies tmux for many engineers.

---

## Practical Tips

- Keep sessions named by purpose, not host
- Don’t overload a single window with too many panes
- Use tmux to preserve *context*, not just shells
- Learn a few commands deeply rather than many shallowly

Muscle memory matters more than completeness.

---

## Takeaways

- tmux is a session manager, not just a splitter
- Sessions protect work across disconnections
- Windows organize tasks; panes provide context
- Copy mode is essential for real-world use
- A small command set goes a long way

Once tmux becomes part of your workflow, working without it feels unnecessarily fragile.
