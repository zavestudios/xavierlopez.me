---
layout: single
title: "Tmux Cheatsheet"
date: 2022-04-06 07:55:43 -0800
categories: software-development system-administration tools
---

List tmux sessions:

```bash
tmux ls
```

Start two new tmux sessions, detached, both running vim:

```bash
tmux new -s first -d vim
tmux new -s second -d vim
```

Attach to the first new session:

```bash
tmux attach -t first
```

Detach from the first session:

```
PREFIX d
```

Attach to the second session:

```bash
tmux attach -t second
```

Switch to the second session, from the first, in one move:

```
PREFIX (
```

Switch back:

```
PREFIX )
```

Rename running session:

```
Ctrl + b:
rename-session -t [current-name] [new-name]
```

Kill a session:

```bash
tmux kill-session -t [session-name]
```

More to come.