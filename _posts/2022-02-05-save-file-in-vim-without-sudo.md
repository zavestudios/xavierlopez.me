---
layout: single
title: "Save file in VIM without sudo"
date: 2022-02-05 15:17:22 -0800
categories: system-administration
---

I cringe every time vim notifies me that I won't be able to save the file I've just edited, after I've already changed it in 10 different places.

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-05-at-3.20.44-PM.png)

Ouch!

We sometimes get caught up in the rhythm of a manual server change and forget we've opened a file without sudo. It's a frustrating server-administration mishap, but it's not without a remedy, so let's solve this problem.

Again, the trouble is that you've opened the file without sudo, which you can fix by closing the file and reopening with sudo, but then you'd lose your edits. We want to have our cake and eat it too. The following vim command makes amends for our earlier omission of sudo and saves the file:

```vim
:w !sudo tee %
```

This will require you to enter your password, so you must be a sudoer. Then, you'll receive a message that looks like this:

![](https://xavierlopez.me/wp-content/uploads/2020/02/Screen-Shot-2020-02-05-at-4.57.15-PM.png)

Your file name won't be the same as mine, of course.

It doesn't matter whether you choose [0]K or [L]oad. Choose one and keep editing, or, if you're done, exit like this:

```vim
:q!
```

That'll bring you back to your console.