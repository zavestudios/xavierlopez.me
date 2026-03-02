---
permalink: /systems/
title: "Systems"
layout: single
author_profile: true
---

Long-running platform initiatives demonstrating infrastructure-as-product principles.

Each system page provides architectural narrative and links to canonical implementation repositories.

---

## Current Systems

{% for system in site.systems %}
### [{{ system.title }}]({{ system.url }})

{{ system.excerpt }}

{% endfor %}

---

**Note:** System pages explain intent, problem space, and architectural philosophy. Implementation details, contracts, and configuration live in GitHub repositories.
