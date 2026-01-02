---
layout: single
title: "File Archiving and Compression Cheatsheet"
date: 2021-07-02 08:56:28 -0800
categories: system-administration tools
---

## TAR - Tape Archive Tool found in Linux / Unix

- `c` - Create archive
- `r` - Append to archive
- `t` - List contents of archive
- `x` - Extract archive
- `v` - Verbose
- `f file` - File to use

## Gzip - Classic compression in Linux

- `d` - decompress file

## Bzip2 - More compression than gzip but more time to compress

- `d` - decompress file

## Create tar from files

```bash
tar cvf archive.tar file1 file2 dir1 dir2
```

## List contents of archive

```bash
tar tvf archive.tar
```

## Append file or dir to archive

```bash
tar rvf archive.tar file3
tar rvf archive.tar dir3
```

## Extract file or directory

```bash
tar xvf archive.tar file3
tar xvf archive.tar dir3/subdir3
```

## Extract archive

```bash
tar xvf archive.tar
```

## Extract in a different directory

```bash
tar xvf archive.tar -C /tmp/extracted
```

## Compress

```bash
tar zcvf compressed.tar.gz file1 file2
tar jcvf compressed.tar.bz2 file1 file2
```

## List compressed files

```bash
tar ztvf compressed.tar.gz
tar jtvf compressed.tar.bz2
```

## Extract compressed files

```bash
tar zxvf compressed.tar.gz file1
tar jxvf compressed.tar.bz2 file1
```