---
layout: single
title: "Order ls command output by date"
date: 2022-02-17 20:29:02 -0800
categories: system-administration
---

The other day I needed to manipulate some files I'd just downloaded from an s3 bucket.  Listing the contents of the downloads directory revealed a huge challenge.  It was like trying to find a black cat in a coal cellar.  This is what I did:

`ls -lt`

That did it. Since I'd just downloaded the files, they were all right next to one another.  You know what, though?  They were in descending order, and the files in question were at the top of the list.  That's not exactly what I needed.  No problem, the reverse switch to the rescue.

`ls -ltr`

Now I was cooking with petrol.  The rest of the task was made much easier.