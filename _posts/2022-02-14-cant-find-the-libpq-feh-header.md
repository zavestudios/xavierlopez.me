---
layout: single
title: "Can't find the libpq-fe.h header"
date: 2022-02-14 15:26:07 -0800
categories: software-development system-administration
---

This sometimes happens when you try to install the pg gem on a linux box.

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-14-at-3.16.03-PM.png)

In my experience, all distributions are susceptible to this, but this post is for centos 7.7. Earlier in this provisioning session, I'd installed postgres, like this:

`sudo yum install postgresql-server postgresql-contrib`

Do you see the problem there? Yeah, neither did I. All I had to do to solve this issue was install this package:

`sudo yum install postgresql-devel`

After that, bundler successfully installed the pg gem, and I was off and running. I'll refine this post for other linux distributions, as the opportunities present theirselves. Be assured, they will.