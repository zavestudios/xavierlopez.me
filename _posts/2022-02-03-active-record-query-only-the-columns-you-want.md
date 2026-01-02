---
layout: single
title: "Active Record - Query Only the Columns You Want"
date: 2022-02-03 16:20:44 -0800
categories: software-development
---

Here's another bit of command line usefulness that I repeatedly need, but never remember. It does a great job of making the query result readable and uncluttered by data you don't need. Let's get users, but only their firstnames, lastnames and emails. Also, let's use the table_print gem to prettify the results:

```ruby
tp User.all, :first_name, :last_name, :email
```

That'll do it. If you're not using table_print, then just omit it from the query. You'll love the result, either way.