---
layout: single
title: "Docker Cheatsheet: Practical Commands for Daily Use"
date: 2022-03-24 08:05:00 +0000
last_modified_at: "2025-01-12"
categories:
  - containers
  - cli
  - productivity
tags:
  - docker
  - containers
  - images
  - networking
  - troubleshooting
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
```
docker build -t my-image:latest .
```

List local images:
```
docker images
```

Remove an image:
```
docker rmi my-image:latest
```

Remove unused images:
```
docker image prune
```

Tag an image:
```
docker tag my-image:latest my-image:v1
```

---

## Containers

Run a container:
```
docker run my-image
```

Run interactively with a shell:
```
docker run -it my-image /bin/bash
```

Run in detached mode:
```
docker run -d my-image
```

List running containers:
```
docker ps
```

List all containers:
```
docker ps -a
```

Stop a container:
```
docker stop <container_id>
```

Remove a container:
```
docker rm <container_id>
```

---

## Inspecting and Debugging

View container logs:
```
docker logs <container_id>
```

Follow logs:
```
docker logs -f <container_id>
```

Inspect container details:
```
docker inspect <container_id>
```

Execute a command in a running container:
```
docker exec -it <container_id> /bin/bash
```

Check resource usage:
```
docker stats
```

---

## Networking

List networks:
```
docker network ls
```

Inspect a network:
```
docker network inspect <network_name>
```

Run a container on a specific network:
```
docker run --network my-network my-image
```

Expose ports:
```
docker run -p 8080:80 my-image
```

Networking issues are often configuration issues—inspect before guessing.

---

## Volumes and Data

List volumes:
```
docker volume ls
```

Inspect a volume:
```
docker volume inspect <volume_name>
```

Create a volume:
```
docker volume create my-volume
```

Mount a volume:
```
docker run -v my-volume:/data my-image
```

Mount a host directory:
```
docker run -v $(pwd):/app my-image
```

Understand whether your data is **ephemeral or persistent**.

---

## Cleanup (Use With Care)

Remove stopped containers:
```
docker container prune
```

Remove unused networks:
```
docker network prune
```

Remove unused volumes:
```
docker volume prune
```

Remove everything unused:
```
docker system prune
```

Prune commands are powerful—review what will be removed before confirming.

---

## Common Patterns

Rebuild and run:
```
docker build -t my-image . && docker run my-image
```

Stop and remove all containers:
```
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

Remove dangling images:
```
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
