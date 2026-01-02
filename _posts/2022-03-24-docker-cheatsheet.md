---
layout: single
title: "Docker Cheatsheet"
date: 2022-03-24 12:33:19 -0800
categories: software-development
---

Yet another cheatsheet! This is coming in handy, isn't it?  Let's start this off with one that is relatively new to me, and wonderfully useful.

Inspect a Docker image to see environment variables and other metadata:

```bash
docker image inspect <image-id>
```

That one will tell you, among other things, which environment variables you were able to successfully stick inside the image. Speaking of which, here's a way to build, tag, and put environment variables inside the image at build time:

```bash
docker build -t reponame/image_name --build-arg ENV_VAR_NAME=value .
```

Remove all images where the name contains a pattern:

```bash
docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi
```

Remove all stopped containers, all dangling images, and all unused networks:

```bash
docker system prune
```

Run a docker image, overriding the ENTRYPOINT:

```bash
docker run -it --rm --entrypoint='' example/example:example-v1.2.3 sh
```