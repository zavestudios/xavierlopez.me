---
layout: single
author_profile: true
title: "Welcome"
---

Senior Platform Engineer specializing in Kubernetes, cloud infrastructure, and secure CI/CD pipelines. I build and support platforms that developers can be enthusiastic about.

[View My Resume →](/about/){: .btn .btn--primary}

## Recent Posts

{% for post in site.posts limit:3 %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more →]({{ post.url }}){: .btn .btn--inverse}
{% endfor %}

[View all posts →](/posts/){: .btn .btn--primary}