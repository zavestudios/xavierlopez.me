---
permalink: /glossary/
title: "Glossary"
layout: glossary
author_profile: false
---

<p class="page-intro">Terms I use when describing platform work. These may or may not be formal industry definitions. In either case, they are the working meanings behind this site and the ZaveStudios platform practice.</p>

{% for entry in site.data.glossary %}
<section class="glossary-entry" id="{{ entry.slug }}">
  <h3>{{ entry.term }}</h3>
  <div class="glossary-definition">{{ entry.definition | markdownify }}</div>

  {% if entry.why_it_matters %}
  <p><strong>Why it matters:</strong> {{ entry.why_it_matters }}</p>
  {% endif %}

  {% if entry.examples %}
  <p><strong>Examples:</strong></p>
  <ul>
    {% for example in entry.examples %}
    <li>{{ example }}</li>
    {% endfor %}
  </ul>
  {% endif %}

  {% if entry.references %}
  <p><strong>References:</strong></p>
  <ul>
    {% for reference in entry.references %}
    <li><a href="{{ reference.url }}">{{ reference.label }}</a></li>
    {% endfor %}
  </ul>
  {% endif %}
</section>
{% endfor %}
