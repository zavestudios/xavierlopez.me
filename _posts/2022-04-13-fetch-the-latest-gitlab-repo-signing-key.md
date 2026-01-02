---
layout: single
title: "Fetch the latest Gitlab repo signing key"
date: 2022-04-13 14:43:02 -0800
categories: system-administration
---

This is something I had to track down recently. If you haven't seen it yet, you will. I know I'm going to need to refer back to it before all my servers are up-to-date. So, I'll put it here.

Download the new key:

```bash
curl https://packages.gitlab.com/gpg.key -o /tmp/omnibus_gitlab_gpg.key
```

Import the new key on a Debian system:

```bash
sudo apt-key add /tmp/omnibus_gitlab_gpg.key
```

Import the new key on a CentOS/OpenSUSE/SLES system:

```bash
sudo rpm --import /tmp/omnibus_gitlab_gpg.key
```