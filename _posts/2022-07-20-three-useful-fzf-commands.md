---
layout: single
title: "Three Useful fzf Commands for Everyday Terminal Work"
date: 2022-07-20 09:10:00 +0000
last_modified_at: "2025-01-18"
categories:
  - cli
  - productivity
tags:
  - fzf
  - terminal
  - bash
  - zsh
  - developer-tools
excerpt: "Three practical fzf patterns that turn common terminal tasks—finding files, commands, and processes—into fast, interactive workflows."
toc: true
toc_sticky: true
---

## Context

If you live in a terminal, speed comes from **reducing friction**, not memorizing more commands.

`fzf` (fuzzy finder) earns its place because it:
- composes cleanly with Unix tools
- works interactively
- scales from tiny repos to massive systems

This post covers **three high-leverage fzf patterns** that are easy to adopt and immediately useful.

---

## 1) Fuzzy-Find and Open Files

Searching for files is a constant task—configs, logs, scripts, docs.

### Basic pattern

```bash
fzf
```

This lists files recursively from the current directory and lets you fuzzy-search interactively.

---

### Open the selected file in an editor

```bash
vim $(fzf)
```

or, for VS Code:

```bash
code $(fzf)
```

Why this works:
- no need to remember paths
- fast narrowing with a few keystrokes
- works anywhere, not just Git repos

This is often faster than `find` + copy/paste.

---

## 2) Search Command History

Shell history grows quickly. Finding the *right* command again is harder than retyping it.

### Fuzzy-search history

```bash
history | fzf
```

This lets you:
- scroll interactively
- search by fragments
- avoid exact matches

---

### Execute the selected command

```bash
history | fzf | sed 's/^[ ]*[0-9]\+[ ]*//' | bash
```

What this does:
- strips history line numbers
- executes the selected command

Use with care—but it’s incredibly effective for repeating complex commands.

---

## 3) Find and Act on Processes

Process management is another place where fuzzy selection shines.

### Select a process interactively

```bash
ps aux | fzf
```

This is useful when:
- multiple similar processes exist
- PIDs change frequently
- names are long or truncated

---

### Kill the selected process

```bash
ps aux | fzf | awk '{print $2}' | xargs kill
```

Why this is powerful:
- no manual PID copying
- visual confirmation before action
- composable with other commands

You can easily swap `kill` for `kill -9` or other signals when appropriate.

---

## Why These Patterns Work So Well

Each example follows the same idea:

- generate a list (`ps`, `history`, filesystem)
- filter interactively with `fzf`
- pass the result to the next command

This is the Unix philosophy—with a modern, interactive layer.

---

## Practical Tips

- Bind common fzf commands to shell aliases or keybindings
- Combine fzf with `ripgrep (rg)` for even faster searches
- Don’t over-automate destructive actions—keep the human in the loop

`fzf` is most powerful when it **augments judgment**, not replaces it.

---

## Takeaways

- `fzf` turns lists into interactive tools
- It composes cleanly with existing commands
- File navigation, history recall, and process management benefit immediately
- Small productivity gains add up quickly in terminal-heavy workflows

Once `fzf` is in your muscle memory, working without it feels unnecessarily slow.
