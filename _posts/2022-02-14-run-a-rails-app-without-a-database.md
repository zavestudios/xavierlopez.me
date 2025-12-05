---
layout: single
title: "Run a Rails App Without a Database"
date: 2022-02-14 20:47:06 -0800
categories: database software-development
---

Haven't you ever wanted to create a Rails application without a database? Installing the default SQLite database, or choosing a different one, and installing that one, and [dealing with the potential difficulties](https://xavierlopez.me/2020/02/cant-find-the-libpq-fe-h-header/), are time consuming and unnecessary tasks, if you don't even need persistent data.  I've done it, though. A few times.  It's frustrating.  Let's not do that anymore.

I'll walk you through the creation of an app that would typically not use a database, and the appropriate configuration.  This post assumes you've already provisioned a Rails development box. Down the road, I'll post a Vagrantfile to help you with that.  

Step 1:  Create a new api-only Rails app -- a nice use case for our purpose.

`rails new <your_app_name> --api `

Step 2:  That rails sub-command creates an app template without many of the artifacts included in the web app template, but it still expects a database, until we reconfigure. 

Step 3:  Open up the Gemfile and remove any reference to the default database adapter gem.

Step 4: Open "config/application.rb".  Comment out all references to active_record. We should comment them out, instead of deleting them, because we're likely to need a database for this app, eventually, don't you think?  When the need arises, the comments will serve as a reminder of what we need to do.

Step 5:  Open "config/environments/development.rb", and comment this line ...

`config.active_record.migration_error = :page_load`

That's it. Have fun.