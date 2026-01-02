---
layout: single
title: "RVM Cheatsheet"
date: 2022-02-28 10:27:06 -0800
categories: software-development system-administration
---

Let's create a handy little list of my most commonly used rvm commands. RVM, for those who might be wondering, is a ruby version manager. It does a great job of downloading and making rubies, but it also manages gems into 'gemsets'.  There is another ruby version manager, [RBENV](https://github.com/rbenv/rbenv), which is also a great tool.  I use them both, depending on the situation.  Look out for a post on RBENV, in the future.

Tell RVM to show us all the rubies in the world:

```bash
rvm list known
```

Install one:

```bash
rvm install 2.5.1
```

In order to use that ruby, do this:

```bash
rvm 2.5.1
```

Rubies are one thing, and gems are another. Let's create a new gemset, then we'll match up a ruby with a gemset:

```bash
rvm gemset create namedgemset
```

Output:
```
Gemset 'namedgemset' created.
```

To use our new gemset:

```bash
rvm gemset use namedgemset
```

Why not create a new gemset and use it, in one command? This is the one I use the most:

```bash
rvm use 2.5.1@namedgemset --create
```

RVM does so much more than what I'm showing you here. I'll add more functionality to this post in the future, as the opportunities present themselves. If you're interested, go and take a look at the rvm homepage.

Here's something that has always confused me...let's list all our gemsets.

```bash
rvm gemset list
```

I've seen the output from that a hundred times and have always had a nagging suspicion that I wasn't seeing all the gemsets I want to see, until one day it occurred to me that when you run that, it only shows you the gemsets for the ruby interpreter you happen to be running, at that moment.  To demonstrate, let's do this:

```bash
ruby -v && rvm gemset list
```

If you're running ruby 2.5.1, on a MAC, here's what you're likely to see:

```
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86-64-darwin18]
gemsets for ruby-2.5.1 (found in /Users/you/.rvm/gems/ruby-2.5.1)
=> (default)
     gemset_1
     gemset_2
     gemset_3
     gemset_n
```

So how can you see all the gemsets you have, for all the interpreters, without having to switch from one ruby to another?

```bash
rvm gemset list_all
```

That's how.