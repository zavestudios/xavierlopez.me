---
layout: single
title: "Display verbose output during 'vagrant up'"
date: 2022-03-02 16:37:09 -0800
categories: software-development
---

Today, I was running the 'curl' command, as part of the provisioning of a Vagrant vm. It was failing, and I couldn't tell why, because there wasn't enough information in the output.  So here's what I did:

`VAGRANT_LOG=info vagrant up`

You can also do this:

`vagrant up --debug`

This outputs much more information than the default.