---
layout: single
title: "See Git Log in Glorious Detail"
date: 2022-02-15 11:45:12 -0800
categories: software-development
---

The Git subcommand that I'm about to share with you is so esoteric and its output so detailed, that it inspires developers to build entire user interfaces.  The primary reason for me writing this blog was to have a repository to place snippets and procedures that I frequently need, but have a hard time remembering. This is a perfect example of that.  I got this from Slipp D. Thompson.  I found it in his Stack Overflow answer to a question about how to visualize the git log.  As you'll see in his answer, he sets it up as an alias.  I'll record it here, and cut and paste it, whenever I need it.

`git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed: %cD)%C(reset) %C(auto)%d%C(reset)%n''          %C(white)%s%C(reset)%n''          %C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'`

Just run that monster in your terminal and be amazed. Enjoy. Thanks,  Slipp!