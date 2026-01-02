---
layout: single
title: "Skip the pipeline when pushing to Git"
date: 2022-02-03 15:25:13 -0800
categories: software-development
---

Sometimes you don't want to trigger an entire pipeline run, right? Maybe you've only changed the name of some files in the repo, or perhaps you deleted some files from the repo. Whatever your motivation for not following your CI/CD sequence, here's how to push to git without triggering a build:

```bash
git push <remote_name> <branch_name> -o ci.skip
```

Here's how it looks in your pipeline view:

![](https://xavierlopez.me/wp-content/uploads/2020/02/crop-0-0-522-286-0-Screen-Shot-2020-02-03-at-3.26.33-PM.png)

It's been skipped, just like we wanted.