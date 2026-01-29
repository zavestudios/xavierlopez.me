---
layout: single
title: "Can't Find the libpq-fe.h Header?"
date: 2022-02-14 08:00:00 +0000
last_modified_at: "2025-01-04"
categories:
  - linux
  - development
  - development
excerpt: "How to resolve errors related to missing libpq-fe.h headers when compiling PostgreSQL clients or native extensions, and why this issue occurs."
toc: true
toc_sticky: true
---

## Context

If you’ve ever seen an error like:

```text
fatal error: libpq-fe.h: No such file or directory
```

you were likely trying to compile something that depends on **PostgreSQL’s client libraries**—often a native extension, language binding, or database adapter.

This is a common setup issue, especially on fresh systems or minimal environments.

---

## What Is `libpq-fe.h`?

`libpq-fe.h` is a header file provided by **libpq**, PostgreSQL’s C client library.

It’s required when compiling:

- PostgreSQL client applications
- language bindings (Ruby, Python, Node.js, etc.)
- native database adapters
- tools that link against PostgreSQL

If the header is missing, compilation cannot proceed.

---

## Why This Error Happens

Most systems separate:

- **runtime libraries** (needed to *run* software)
- **development headers** (needed to *build* software)

You may have PostgreSQL installed and running—but **not** the development package that provides headers like `libpq-fe.h`.

---

## Fix on Debian / Ubuntu

Install the PostgreSQL development package:

```sql
sudo apt update
sudo apt install libpq-dev
```

This installs:

- `libpq-fe.h`
- required client libraries
- supporting build files

After installation, retry your build.

---

## Fix on Red Hat / CentOS / Rocky / Alma

Install the development package:

```bash
sudo dnf install postgresql-devel
```

Or on older systems:

```bash
sudo yum install postgresql-devel
```

Package names differ slightly by distribution, but the intent is the same.

---

## Fix on macOS (Homebrew)

If you’re using Homebrew:

```bash
brew install postgresql
```

Ensure headers are discoverable:

```bash
brew info postgresql
```

If compilation still fails, confirm include paths are correct or exported.

---

## Verifying the Header Exists

After installation, confirm the file is present:

```bash
find /usr -name libpq-fe.h
```

Typical locations include:

- `/usr/include/postgresql/libpq-fe.h`
- `/usr/local/include/postgresql/libpq-fe.h`

The exact path matters for some build systems.

---

## When Build Tools Still Can’t Find It

If the header exists but compilation still fails:

- verify compiler include paths
- check environment variables like `CPPFLAGS` or `CFLAGS`
- ensure the correct PostgreSQL version is being referenced

Some build systems require explicit paths.

---

## Common Scenarios Where This Appears

This error frequently occurs when:

- installing Ruby gems like `pg`
- building Python packages like `psycopg2`
- compiling Node.js native modules
- setting up CI runners on minimal images
- provisioning fresh development machines

The fix is usually the same: install the dev package.

---

## Practical Tips

- Runtime success does not imply build readiness
- Always install `*-dev` or `*-devel` packages for native builds
- CI images often omit headers by default
- Document build dependencies explicitly

Missing headers are a **setup issue**, not a PostgreSQL problem.

---

## Takeaways

- `libpq-fe.h` is part of PostgreSQL’s client development headers
- You need the *development* package, not just PostgreSQL itself
- Package names vary by OS, but intent is consistent
- Verifying header paths helps diagnose edge cases
- Most failures are resolved by installing one package

When native extensions fail to compile, missing headers are often the quiet culprit.
