---
layout: single
title: "Run a Rails App Without a Database"
date: 2022-02-16 08:00:00 +0000
last_modified_at: "2025-01-06"
categories:
  - rails
  - development
  - configuration
tags:
  - rails
  - ruby
  - database
  - configuration
  - api
excerpt: "How to run a Rails application without a database, why you might want to, and what configuration changes are required to avoid unnecessary coupling."
toc: true
toc_sticky: true
---

## Context

Rails assumes a database by default.

That assumption is convenient for most applications—but not all of them. There are valid cases where you want a Rails app that:

- serves static or semi-static content
- acts as a proxy or API façade
- integrates with external services only
- defers persistence to another system

In these scenarios, forcing a database into the architecture adds friction without value.

---

## When Running Without a Database Makes Sense

Common use cases include:

- API gateways
- webhook receivers
- background job dispatchers
- service frontends backed by external APIs
- temporary or experimental applications

If your app doesn’t persist state locally, Rails doesn’t need a database.

---

## What Rails Uses the Database For

By default, Rails expects a database for:

- Active Record models
- schema loading
- migrations
- environment boot checks

If you remove the database without telling Rails, you’ll see errors during boot—even if your app never touches models.

---

## Disabling Active Record

The cleanest way to run Rails without a database is to disable Active Record entirely.

In `config/application.rb`:

```ruby
require_relative "boot"

require "rails"
# Pick the frameworks you want:
require "action_controller/railtie"
require "action_view/railtie"
require "action_mailer/railtie"
require "active_job/railtie"
# Skip active_record/railtie

module MyApp
  class Application < Rails::Application
    config.load_defaults 7.0
  end
end
```

By omitting `active_record/railtie`, Rails will no longer expect a database.

---

## Removing Database Configuration

You can safely remove or ignore:

- `config/database.yml`
- migration files
- schema files

Rails will not attempt to load them if Active Record is disabled.

---

## Generating a Rails App Without Active Record

You can also avoid Active Record from the beginning:

```bash
rails new myapp --skip-active-record
```

This produces:

- no database configuration
- no migration directory
- a lighter application footprint

This is ideal when you know upfront that persistence isn’t required.

---

## Working With Models (Without a Database)

You can still define **plain Ruby objects** or use:

- `ActiveModel`
- POROs (Plain Old Ruby Objects)
- value objects
- service objects

Example using `ActiveModel`:

```ruby
class HealthCheck
  include ActiveModel::Model

  attr_accessor :status
end
```

This allows validations and conventions without persistence.

---

## Controllers and Routes Work Normally

Everything else in Rails continues to function:

- routing
- controllers
- middleware
- rendering
- request lifecycle

From a request/response perspective, nothing changes.

---

## Testing Without a Database

If Active Record is disabled:

- database setup is skipped
- test boot time improves
- tests run faster and with fewer dependencies

Just ensure your test helpers don’t assume database availability.

---

## Common Pitfalls

- Leaving `active_record/railtie` enabled unintentionally
- Loading gems that assume Active Record is present
- Referencing migrations or schema files indirectly
- Assuming Rails *requires* a database (it doesn’t)

Most issues come from defaults, not limitations.

---

## Practical Tips

- Disable Active Record explicitly
- Remove unused configuration early
- Favor POROs and service objects
- Keep dependencies honest about what they require
- Reintroduce persistence only if it adds value

Rails is more flexible than its reputation suggests.

---

## Takeaways

- Rails does not require a database
- Active Record is optional, not mandatory
- Skipping the database simplifies architecture
- Lighter apps boot faster and fail less
- Explicit configuration prevents surprises

If your app doesn’t need persistence, don’t force it—Rails will happily run without it.
