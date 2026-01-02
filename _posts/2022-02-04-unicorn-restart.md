---
layout: single
title: "Unicorn Restart"
date: 2022-02-04 19:31:38 -0800
categories: system-administration
---

Every now and then you have to restart your Rails applications. Something happens somewhere along the chain and  you start getting screenshots from your colleagues of error logs and 501 Bad Gateway Errors. 

So you get on the server and crack your knuckles for the quick work you're about to make of those pesky old processes. Until you get that familiar, unsettling feeling. Is this Sys V Init? System D? Upstart? 

Those are important details. Let's document it all right here, so we can refer back to it when it happens again.

### Which init am I running?

First, let's discover which system we're running, so we don't have to cycle through every possibility. Making lots of mistakes is a great way to learn, but we're not in the mood for that right now, because we have people waiting on us. This trusty little companion will help with that:

```bash
ps -p1 | grep "init\|upstart\|systemd"
```

Now, depending on what the command above returns, you do the following:

### Sys V Init & Upstart

```bash
sudo service unicorn restart
```

### System D

```bash
sudo systemctl start unicorn
```

### Sometimes you need to do this...

...this might happen if your initialization script doesn't have a restart command:

```bash
/etc/init.d/unicorn restart
```