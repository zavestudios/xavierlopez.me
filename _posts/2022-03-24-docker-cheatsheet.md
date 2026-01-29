---
layout: single
title: "Docker Cheatsheet: Practical Commands for Daily Use"
date: 2022-03-24 08:05:00 +0000
last_modified_at: "2025-01-12"
categories:
  - devops
  - development
  - productivity
excerpt: "A practical Docker cheatsheet focused on the commands and patterns you actually use when building, running, and debugging containers."
toc: true
toc_sticky: true
---

## Context

Docker is simple until it isn’t.

Most day-to-day work boils down to a **small, reliable set of commands** for:

- building images
- running containers
- inspecting state
- cleaning up safely

This cheatsheet focuses on **high-signal commands** that cover the majority of real-world Docker usage.

---

## Images

Build an image:

```bash
docker build -t my-image:latest .
```

List local images:

```bash
docker images
```

Remove an image:

```bash
docker rmi my-image:latest
```

Remove unused images:

```bash
docker image prune
```

Tag an image:

```bash
docker tag my-image:latest my-image:v1
```

---

## Containers

Run a container:

```bash
docker run my-image
```

Run interactively with a shell:

```bash
docker run -it my-image /bin/bash
```

Run in detached mode:

```bash
docker run -d my-image
```

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Stop a container:

```bash
docker stop <container_id>
```

Remove a container:

```bash
docker rm <container_id>
```

---

## Inspecting and Debugging

View container logs:

```bash
docker logs <container_id>
```

Follow logs:

```bash
docker logs -f <container_id>
```

Inspect container details:

```bash
docker inspect <container_id>
```

Execute a command in a running container:

```bash
docker exec -it <container_id> /bin/bash
```

Check resource usage:

```bash
docker stats
```

---

## Networking

List networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect <network_name>
```

Run a container on a specific network:

```bash
docker run --network my-network my-image
```

Expose ports:

```bash
docker run -p 8080:80 my-image
```

Networking issues are often configuration issues—inspect before guessing.

---

## Volumes and Data

List volumes:

```bash
docker volume ls
```

Inspect a volume:

```bash
docker volume inspect <volume_name>
```

Create a volume:

```sql
docker volume create my-volume
```

Mount a volume:

```bash
docker run -v my-volume:/data my-image
```

Mount a host directory:

```bash
docker run -v $(pwd):/app my-image
```

Understand whether your data is **ephemeral or persistent**.

---

## Cleanup (Use With Care)

Remove stopped containers:

```bash
docker container prune
```

Remove unused networks:

```bash
docker network prune
```

Remove unused volumes:

```bash
docker volume prune
```

Remove everything unused:

```bash
docker system prune
```

Prune commands are powerful—review what will be removed before confirming.

---

## Common Patterns

Rebuild and run:

```bash
docker build -t my-image . && docker run my-image
```

Stop and remove all containers:

```bash
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

Remove dangling images:

```bash
docker rmi $(docker images -f "dangling=true" -q)
```

These patterns save time but require awareness.

---

## Common Mistakes

- Forgetting to clean up unused resources
- Confusing image names and container IDs
- Running everything as root unnecessarily
- Baking secrets into images
- Treating containers as long-lived pets

Docker works best with **stateless, reproducible containers**.

---

## Practical Tips

- Name containers intentionally
- Keep Dockerfiles small and readable
- Use `.dockerignore` aggressively
- Inspect before deleting
- Prefer rebuilding over modifying running containers

Consistency beats cleverness.

---

## Takeaways

- A small command set covers most Docker usage
- Inspecting state is more useful than guessing
- Cleanup prevents resource creep
- Volumes define persistence boundaries
- Docker rewards simple, repeatable workflows

Once these commands are muscle memory, Docker becomes a quiet, reliable tool instead of a source of friction.
