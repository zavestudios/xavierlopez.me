---
layout: single
title: "Shrink SQL DB log file"
date: 2022-02-11 16:31:05 -0800
categories: database
---

Before copying a database to another server, it's a good idea to shrink the log file for transport. Open SQL Server Management Studio and run the following commands in the query window:

-- tell SSMS which database to work on
`USE <table_name>
`
-- truncate the log file`
ALTER DATABASE <table_name> SET RECOVERY SIMPLE
`
-- Shrink the log file that you just truncated, to 1 MB
`DBCC SHRINKFILE('<table_name>', 1)
`
-- Reset the recovery model back to full
`ALTER DATABASE <table_name> SET RECOVERY FULL`

Duplicate the above, changing <table_name> on all the lines, that way you can do multiple databases in one execution.