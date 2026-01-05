---
layout: single
title: "Docker CLI Aliases for Day-to-Day Work"
date: 2024-02-12 08:00:00 +0000
last_modified_at: "2025-01-04"
categories:
  - containers
  - productivity
  - tooling
tags:
  - docker
  - aliases
  - cli
  - developer-productivity
excerpt: "A curated set of Docker CLI aliases that reduce friction during day-to-day container work, with context on how and when to use them."
toc: true
toc_sticky: true
---

## Context

The Docker CLI is powerful, but it’s also verbose. When you’re iterating quickly—building images, inspecting containers, cleaning up state—the friction adds up.

Over time, many engineers accumulate small aliases to make common operations faster and more predictable. The set documented here is one I’ve used for years, with only minor adjustments to suit my workflow.

---

## Attribution

The Docker alias set below is based on a script originally created and shared publicly by **Jean-Guy Grodziski** as a GitHub Gist.

I did not invent these aliases.  
My contribution here is:

- curating the set I actually use
- preserving the original intent
- adding context around *why* these aliases are useful
- documenting how they fit into a day-to-day workflow

Original source: https://gist.github.com/jgrodziski/9ed4a17709baad10dbcd4530b60dfcbb

---

## Why Aliases Matter for Docker

Docker commands tend to fall into a few repeated patterns:

- listing objects
- inspecting state
- cleaning up resources
- attaching to running containers

Aliases don’t make Docker “simpler” — they make it **faster to think** by reducing keystrokes and visual noise.

That matters when Docker is part of a larger workflow (CI/CD, Kubernetes, local debugging), not the focus itself.

---

## The Alias Set

Below is the alias set, unchanged in spirit from the original source.

These aliases assume:

- comfort with Docker fundamentals
- awareness of what commands like `rm`, `rmi`, and `prune` actually do
- intentional use (not blind copy-paste in production environments)

```
# Containers
alias dps='docker ps'
alias dpsa='docker ps -a'
alias dstart='docker start'
alias dstop='docker stop'
alias drm='docker rm'

# Images
alias di='docker images'
alias drmi='docker rmi'

# Logs and exec
alias dlog='docker logs'
alias dlogf='docker logs -f'
alias dexec='docker exec -it'

# Cleanup
alias dprune='docker system prune'
alias dprunea='docker system prune -a'
```

Keep these in a shell config file you already source (`.bashrc`, `.zshrc`, etc.).

---

## How I Use These in Practice

These aliases shine when:

- iterating on Dockerfiles
- debugging container startup issues
- cleaning up local environments after experiments
- pairing Docker usage with Kubernetes or Helm work

They are intentionally small and composable. I don’t alias *everything*—only the commands I run multiple times per session.

---

## Caveats and Safety Notes

A few reminders worth stating explicitly:

- `docker rm` and `docker rmi` are destructive
- `docker system prune -a` removes **unused images**
- aliases make commands faster, not safer
- always understand what’s running before cleaning up

Aliases reduce friction, but they also remove hesitation. Use them deliberately.

---

## When Aliases Stop Being Enough

At a certain scale:

- Docker becomes a build tool, not a runtime
- Kubernetes replaces local container orchestration
- CI pipelines own image lifecycle

That’s fine. These aliases are for **local, human-driven work**, not automation.

They’re a productivity aid, not an abstraction layer.

---

## Closing Thoughts

Good tooling disappears. The best aliases are the ones you stop thinking about.

If a command feels tedious more than twice a day, it’s probably worth shortening.
