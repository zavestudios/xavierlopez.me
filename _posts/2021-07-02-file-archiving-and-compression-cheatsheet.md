---
layout: single
title: "File Archiving and Compression Cheatsheet"
date: 2021-07-02 08:56:28 -0800
categories: system-administration tools
---

## TAR - Tape Archive Tool found in Linux / Unix 

- tar c - Create archive- tar r - Append to archive- tar t - List contents of archive- tar x - Extract archive- tar v - Verbose- tar f file - File to use

## Gzip - Classic compression in Linux

- d - decompress file

## Bzip2 - More compression than gzip but more time to compress

- d - decompress file

## Create tar from files

- tar cvf archive.tar file1 file2 dir1 dir2

## List contents of archive

- tar tvf archive.tar

## Append to file or dir to archive

- tar rvf archive.tar file3- tar rvf archive.tar dir3

## Extract file or directory

- tar xvf archive.tar file3- tar xvf archive.tar dir3/subdir3

## Extract archive

- tar xvf archive.tar

## Extract in a different directory

- tar xvf archive.tar -C /tmp/extracted

## Compress

- tar zcvf compressed.tar.gz file1 file2- tar jcvf compressed.tar.bz2 file1 file2

## List compressed files

- tar ztvf compressed.tar.gz- tar jtvf compressed.tar.bz2

## Extract compressed files

- tar zxvf compressed.tar.gz file1- tar jxvf compressed.tar.bz2 file1