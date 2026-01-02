---
layout: single
title: "VIM Cheatsheet"
date: 2022-04-02 20:56:19 -0800
categories: software-development system-administration tools
---

Everyone is already familiar with the basic stuff. If not, you can find it anywhere on the web. I'm going to list some of the hard-to-remember stuff that accomplishes really useful multi-line tasks.

Insert a character at the beginning of a range of lines in a file:

```vim
0i#
```

Then:

```vim
:<start-range>,<end-range>normal .
```

Delete some characters from the beginning of a range of lines in a file:

```vim
:<start-range>,<end-range>s/<char-to-be-deleted>//
```

Find and replace throughout an entire file:

```vim
:%s/foo/bar/g
```

More to come.