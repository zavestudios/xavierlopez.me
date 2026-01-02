---
layout: single
title: "How to delete a local and remote Git branch"
date: 2022-02-03 14:14:11 -0800
categories: software-development
---

I need to do this often, but not often enough to memorize the process. So I'll document it here, where I can easily find it.

First, force-delete the local branch, using the capital 'D' switch. If you're not sure whether you want to delete it yet, use the lower case 'd' switch. That will give you some feedback, in case you have some content that you need to deal with:

```bash
git branch -D branch_name
```

Now let us delete it remotely, too:

```bash
git push <remote_name> :<branch_name>
```

Sometimes you need to update your view of git remote branches. This might be necessary if someone else has deleted a branch, but you still see it when you run:

```bash
git branch --all
```

This will fix that issue:

```bash
git remote update origin --prune
```