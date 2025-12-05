---
layout: single
title: "systemd cheatnotes"
date: 2022-02-05 15:25:32 -0800
categories: system-administration
---

systemd is a system and service manager that's on its way to becoming the default initialization program across linux distributions. The command line starts with 'systemctl' and is followed by sub-commands like 'list', 'status', 'start', 'restart', 'stop'.   

Let's see which programs have been set up as services and are currently loaded: 

`systemctl  list-units --type=service`

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-05-at-2.27.24-PM-1.png)

List currently running services:

`systemctl list-units --type=service --state=running`

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-05-at-2.36.37-PM-1.png)

Enable a service to run on boot. Afterward, check its status, to be sure it's enabled:

`systemctl enable <service-name>.service` 

`systemctl status <service-name>.service`

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-11-at-11.56.51-AM.png)Behold. It's enabled.