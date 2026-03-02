---
permalink: /writing/
title: "Writing"
layout: single
author_profile: true
---

Technical thinking archive organized by theme.

Articles focus on mental models, implementation analysis, and field notes from building and operating platforms.

---

## Browse by Category

{% if site.writing.size > 0 %}

### Platform Engineering
{% assign platform_posts = site.writing | where: "category", "Platform Engineering" | sort: 'date' | reverse %}
{% for post in platform_posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-type">{{ post.type }}</span>
{% endfor %}
{% if platform_posts.size > 5 %}
[View all Platform Engineering posts →](/writing/platform-engineering/)
{% endif %}

### Infrastructure as Product
{% assign infra_posts = site.writing | where: "category", "Infrastructure as Product" | sort: 'date' | reverse %}
{% for post in infra_posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-type">{{ post.type }}</span>
{% endfor %}
{% if infra_posts.size > 5 %}
[View all Infrastructure as Product posts →](/writing/infrastructure-as-product/)
{% endif %}

### System Design
{% assign design_posts = site.writing | where: "category", "System Design" | sort: 'date' | reverse %}
{% for post in design_posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-type">{{ post.type }}</span>
{% endfor %}
{% if design_posts.size > 5 %}
[View all System Design posts →](/writing/system-design/)
{% endif %}

### Operating Models
{% assign ops_posts = site.writing | where: "category", "Operating Models" | sort: 'date' | reverse %}
{% for post in ops_posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-type">{{ post.type }}</span>
{% endfor %}
{% if ops_posts.size > 5 %}
[View all Operating Models posts →](/writing/operating-models/)
{% endif %}

### Data Systems
{% assign data_posts = site.writing | where: "category", "Data Systems" | sort: 'date' | reverse %}
{% for post in data_posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-type">{{ post.type }}</span>
{% endfor %}
{% if data_posts.size > 5 %}
[View all Data Systems posts →](/writing/data-systems/)
{% endif %}

{% else %}
*Writing archive is being migrated. Check back soon.*
{% endif %}

---

## All Posts

{% if site.writing.size > 0 %}
[View all posts chronologically →](/writing/all/)
{% else %}
*Content migration in progress.*
{% endif %}
