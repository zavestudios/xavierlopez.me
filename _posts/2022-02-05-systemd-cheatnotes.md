---
layout: single
title: "systemd Cheatnotes: Practical Service Management"
date: 2022-02-05 08:00:00 +0000
last_modified_at: "2025-01-01"
categories:
  - linux
  - systems
  - operations
tags:
  - systemd
  - systemctl
  - services
  - troubleshooting
excerpt: "Practical systemd commands and patterns for managing services, inspecting state, and troubleshooting issues on modern Linux systems."
toc: true
toc_sticky: true
---

## Context

On modern Linux systems, **systemd is the init system**.

Whether you’re managing servers, debugging CI runners, or operating production hosts, systemd is the layer that:
- starts services
- supervises them
- restarts them
- logs their output

These cheatnotes focus on **the commands you actually use**—not every systemd feature.

---

## Service Lifecycle

Start a service:
```
sudo systemctl start myservice
```

Stop a service:
```
sudo systemctl stop myservice
```

Restart a service:
```
sudo systemctl restart myservice
```

Reload configuration without restarting (if supported):
```
sudo systemctl reload myservice
```

Check status:
```
systemctl status myservice
```

`status` is often the fastest way to understand what’s wrong.

---

## Enable and Disable Services

Enable service at boot:
```
sudo systemctl enable myservice
```

Disable service at boot:
```
sudo systemctl disable myservice
```

Enable and start immediately:
```
sudo systemctl enable --now myservice
```

Disable and stop immediately:
```
sudo systemctl disable --now myservice
```

---

## Listing Services

List active services:
```
systemctl list-units --type=service
```

List all services (including inactive):
```
systemctl list-unit-files --type=service
```

Filter by state:
```
systemctl list-units --state=failed
```

Failed services are usually where attention is needed.

---

## Inspecting Logs (journalctl)

View logs for a service:
```
journalctl -u myservice
```

Follow logs in real time:
```
journalctl -u myservice -f
```

View logs since boot:
```
journalctl -u myservice -b
```

View logs since a time:
```
journalctl -u myservice --since "10 minutes ago"
```

systemd centralizes logs—use that to your advantage.

---

## Reloading systemd Configuration

After modifying unit files:
```
sudo systemctl daemon-reload
```

This tells systemd to re-read unit definitions.

Forgetting this step is a common mistake.

---

## Unit File Locations

Common unit file paths:
- `/etc/systemd/system/` (custom overrides)
- `/lib/systemd/system/` or `/usr/lib/systemd/system/` (distribution-managed)

Prefer overrides in `/etc` to avoid conflicts with package updates.

---

## Editing Units Safely

Edit a unit override:
```
sudo systemctl edit myservice
```

This creates a drop-in override without modifying the original file.

To edit the full unit:
```
sudo systemctl edit --full myservice
```

Overrides are safer and easier to maintain.

---

## Checking Dependencies

View dependencies:
```
systemctl list-dependencies myservice
```

Understanding dependencies helps diagnose startup ordering problems.

---

## Common Troubleshooting Patterns

Check service state:
```
systemctl status myservice
```

Inspect recent failures:
```
journalctl -u myservice --since "5 minutes ago"
```

Restart and watch logs:
```
systemctl restart myservice
journalctl -u myservice -f
```

Most issues reveal themselves quickly with this loop.

---

## Common Mistakes

- Forgetting `daemon-reload` after edits
- Editing vendor unit files directly
- Ignoring journal logs
- Confusing `reload` with `restart`
- Assuming a service is running because it’s enabled

systemd is explicit—trust what it tells you.

---

## Practical Tips

- Use `status` first, not guesswork
- Prefer drop-in overrides
- Read logs before restarting repeatedly
- Know whether your service supports reload
- Treat systemd as your process supervisor, not just a launcher

Clarity beats cargo-cult commands.

---

## Takeaways

- systemd controls service lifecycle on modern Linux
- `systemctl` manages state; `journalctl` explains behavior
- Overrides are safer than direct edits
- Logs are centralized and powerful
- A small command set covers most operational needs

Comfort with systemd turns service issues from mysterious to manageable.
