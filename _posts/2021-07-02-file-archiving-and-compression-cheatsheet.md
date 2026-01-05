---
layout: single
title: "File Archiving and Compression Cheatsheet"
date: 2021-07-02 08:00:00 +0000
last_modified_at: "2024-12-18"
categories:
  - linux
  - cli
  - productivity
tags:
  - tar
  - gzip
  - zip
  - compression
  - archives
excerpt: "A practical cheatsheet for creating, extracting, and inspecting compressed archives using common Unix tools."
toc: true
toc_sticky: true
---

## Context

Archiving and compression show up everywhere:

- packaging releases
- shipping logs
- backing up data
- moving artifacts between systems

Most workflows rely on a **small set of commands**, but the flags are easy to forget. This cheatsheet focuses on the combinations you actually use.

---

## tar (Tape Archive)

### Create an archive

Create an uncompressed archive:

```bash
tar -cvf archive.tar directory/
```

Create a gzip-compressed archive:

```bash
tar -czvf archive.tar.gz directory/
```

Create a bzip2-compressed archive:

```bash
tar -cjvf archive.tar.bz2 directory/
```

Create an xz-compressed archive:

```bash
tar -cJvf archive.tar.xz directory/
```

---

### Extract an archive

Extract a tar archive:

```bash
tar -xvf archive.tar
```

Extract a gzip archive:

```bash
tar -xzvf archive.tar.gz
```

Extract a bzip2 archive:

```bash
tar -xjvf archive.tar.bz2
```

Extract an xz archive:

```bash
tar -xJvf archive.tar.xz
```

---

### Inspect an archive

List contents without extracting:

```bash
tar -tvf archive.tar.gz
```

---

## gzip / gunzip

Compress a file:

```bash
gzip file.txt
```

Decompress:

```bash
gunzip file.txt.gz
```

Keep original file:

```bash
gzip -k file.txt
```

Use higher compression:

```bash
gzip -9 file.txt
```

---

## zip / unzip

Create a zip archive:

```bash
zip -r archive.zip directory/
```

Extract a zip archive:

```bash
unzip archive.zip
```

List zip contents:

```bash
unzip -l archive.zip
```

Exclude files:

```bash
zip -r archive.zip directory/ -x "*.log"
```

---

## xz

Compress a file:

```bash
xz file.txt
```

Decompress:

```bash
unxz file.txt.xz
```

Use maximum compression:

```bash
xz -9 file.txt
```

xz provides excellent compression but is slower than gzip.

---

## Choosing the Right Tool

General guidance:
- **gzip** → speed, wide compatibility
- **bzip2** → better compression, slower
- **xz** → best compression, slowest
- **zip** → cross-platform compatibility

Compression choice is usually a tradeoff between speed and size.

---

## Common Patterns

Archive logs with a timestamp:

```bash
tar -czvf logs-$(date +%F).tar.gz /var/log
```

Extract to a specific directory:

```bash
tar -xzvf archive.tar.gz -C /tmp
```

Compress everything except one file type:

```bash
tar --exclude="*.tmp" -czvf archive.tar.gz directory/
```

---

## Common Mistakes

- Forgetting `-z`, `-j`, or `-J` for compression
- Extracting archives in the wrong directory
- Overusing maximum compression unnecessarily
- Assuming zip preserves permissions like tar

Understanding defaults prevents surprises.

---

## Practical Tips

- Always inspect before extracting unknown archives
- Use `-v` when learning; drop it for scripts
- Prefer tar for Linux-native workflows
- Use zip when sharing with non-Unix systems
- Name archives clearly and consistently

Archives are operational tools—clarity matters.

---

## Takeaways

- `tar` is the foundation of most Unix archiving
- Compression flags determine format
- Inspecting archives avoids mistakes
- Tool choice depends on speed vs size
- A few patterns cover most real-world use cases

With these commands in muscle memory, archiving becomes routine instead of frustrating.
