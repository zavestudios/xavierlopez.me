---
layout: single
author_profile: true
title: "Welcome"
---

## About Me

I'm a Senior Platform Engineer with over 10 years of experience in DevOps, site reliability engineering, cloud architecture, and platform development. I hold Security+ certification and an active TS/SCI clearance.

I create leverage for businesses by developing and operating platforms composed of carefully chosen OSS, COTS, and cloud services. My focus is on reinforcing developer productivity by insulating teams from operational complexity—providing platform usage telemetry, handling service dependencies, and executing software migrations—thereby freeing them to innovate at the application layer.

[View my full resume →](/about/){: .btn .btn--primary}

## Recent Posts

{% for post in site.posts limit:3 %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more →]({{ post.url }}){: .btn .btn--inverse}
{% endfor %}

[View all posts →](/posts/){: .btn .btn--primary}
