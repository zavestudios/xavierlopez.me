---
layout: single
title: "Vim Cheatsheet: Practical Commands You Actually Use"
date: 2022-04-02 08:15:00 +0000
last_modified_at: "2025-01-15"
categories:
  - development
  - productivity
tags:
  - vim
  - editor
  - terminal
  - productivity
  - workflows
excerpt: "A practical Vim cheatsheet focused on the commands and patterns most useful for everyday editing in terminal-based workflows."
toc: true
toc_sticky: true
---

## Context

Vim rewards depth over breadth.

You don’t need to know every command—just a **small, reliable core** that lets you move, edit, and refactor text efficiently without leaving the keyboard.

This cheatsheet focuses on **high-value commands** that cover the majority of real-world editing tasks.

---

## Modes (The Mental Model)

Vim is modal. Understanding this matters more than memorizing commands.

- **Normal mode**: navigation and commands
- **Insert mode**: text entry
- **Visual mode**: selection
- **Command mode**: file and editor commands

If Vim feels confusing, it’s usually a mode issue.

---

## Basic Navigation

Move the cursor:

```vim
h  j  k  l
```

Word movement:

```vim
w   next word
b   previous word
e   end of word
```

Line movement:

```vim
0   start of line
^   first non-blank character
$   end of line
```

File movement:

```vim
gg  top of file
G   bottom of file
```

---

## Insert Mode

Enter insert mode:

```vim
i   insert before cursor
a   insert after cursor
o   open new line below
O   open new line above
```

Exit insert mode:

```vim
Esc
```

Returning to Normal mode quickly is essential.

---

## Editing Text

Delete:

```vim
x       delete character
dd      delete line
dw      delete word
d$      delete to end of line
```

Change:

```vim
cw      change word
cc      change line
c$      change to end of line
```

Undo and redo:

```vim
u       undo
Ctrl-r  redo
```

---

## Copy, Cut, and Paste

Yank (copy):

```vim
yy      yank line
yw      yank word
```

Delete (cut):

```vim
dd
```

Paste:

```vim
p       paste after cursor
P       paste before cursor
```

Vim treats delete as a form of cut.

---

## Visual Mode (Selecting Text)

Enter visual mode:

```vim
v       character-wise
V       line-wise
Ctrl-v  block-wise
```

After selecting:

```vim
y       yank
d       delete
>       indent
<       unindent
```

Visual mode makes structural edits safer.

---

## Searching

Search forward:

```vim
/pattern
```

Search backward:

```vim
?pattern
```

Navigate results:

```vim
n       next match
N       previous match
```

Clear search highlighting:

```vim
:noh
```

---

## Replace

Replace in the current line:

```vim
:s/old/new/
```

Replace globally in file:

```vim
:%s/old/new/g
```

Confirm each replacement:

```vim
:%s/old/new/gc
```

Search and replace is one of Vim’s strongest features.

---

## Working with Files

Save file:

```vim
:w
```

Quit:

```vim
:q
```

Save and quit:

```vim
:wq
```

Quit without saving:

```vim
:q!
```

Open a file:

```vim
:e filename
```

---

## Splits and Windows

Horizontal split:

```vim
:split
```

Vertical split:

```vim
:vsplit
```

Move between splits:

```vim
Ctrl-w h
Ctrl-w j
Ctrl-w k
Ctrl-w l
```

Close a split:

```vim
:close
```

Splits work well for side-by-side comparisons.

---

## Useful Quality-of-Life Commands

Repeat last command:

```vim
.
```

Indent selection:

```vim
>>
<<
```

Auto-indent file:

```vim
gg=G
```

Repeatability is where Vim speed comes from.

---

## Common Mistakes

- Staying in Insert mode too long
- Using arrow keys instead of motions
- Avoiding Normal mode commands
- Trying to memorize everything at once

Vim improves with gradual adoption.

---

## Practical Tips

- Learn motions before plugins
- Optimize for editing, not aesthetics
- Use Vim where latency matters (SSH, servers)
- Let muscle memory build slowly

Mastery comes from repetition, not shortcuts.

---

## Takeaways

- Vim is modal by design—embrace it
- A small command set covers most tasks
- Motions + operators unlock power
- Search and replace are first-class tools
- Efficiency comes from staying on the keyboard

You don’t need to know Vim—you need to **be comfortable** in it.
