---
permalink: /work/
title: "Work"
layout: single
author_profile: true
---

Platform Engineer specializing in Infrastructure as Product and Executable Architecture.

10+ years building secure, reliable, cloud-native platforms that increase developer velocity and reduce operational load.

---

## Professional Experience

{% assign work_sorted = site.work | sort: 'order' %}
{% for role in work_sorted %}
  <h3><a href="{{ role.url }}">{{ role.company }}</a></h3>
  <p><strong>{{ role.title }}</strong> | {{ role.period }}</p>
  <p>{{ role.excerpt }}</p>
{% endfor %}

---

## Certifications

- **Security+** (CompTIA)
- **TS/SCI Clearance** (Active)
