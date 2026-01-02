---
layout: single
title: "Three useful FZF commands"
date: 2022-07-20 13:19:10 -0800
categories: configuration software-development system-administration tools
---

If you haven't yet discovered fzf, you should take a few minutes of each day to get it under your control. It's a tool that could add substantial time savings to your workflow if you spend a lot of time working in a terminal.

Installing it and a deep explanation of how it works can be found [elsewhere](https://github.com/junegunn/fzf#installation), so I'll just place a little cheatsheet here, starting with the 3 easiest-to-learn commands. I found this tutorial here, but good luck trying to go there. It's dreadfully slow. Before these commands will work properly, you'll need to export 3 environment variables, thusly:

```bash
export FZF_DEFAULT_COMMAND="fd . $HOME"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="fd -t d . $HOME"
```

Once you've done that, the following will be available to you:

**CTRL-T** - search for a directory or file in your home directory, then paste the path in the command line.

**OPTION-C** - find a directory in your home directory, then CD to it.

**CTRL-R** - search through command history.

This post is for MacOS. I'm really just getting started with this tool, so check back occasionally for more.