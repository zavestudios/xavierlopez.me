---
title: "Blog Posts"
layout: home
permalink: /posts/
author_profile: false
sidebar:
  - title: "Categories"
    text: >
      {% assign categories_sorted = site.categories | sort %}
      {% for category in categories_sorted %}
      <a href="/categories/#{{ category[0] | slugify }}">{{ category[0] }}</a> ({{ category[1].size }})<br/>
      {% endfor %}
  - title: "Tags"
    text: >
      {% assign tags_sorted = site.tags | sort %}
      {% for tag in tags_sorted %}
      <a href="/tags/#{{ tag[0] | slugify }}">{{ tag[0] }}</a> ({{ tag[1].size }})<br/>
      {% endfor %}
---