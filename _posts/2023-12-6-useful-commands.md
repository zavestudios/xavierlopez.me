---
layout: single
title:  "Useful Commands"
date:   2023-12-6 10:50:00 +0000
categories: linux administration,commands
---
- Top provides a dynamic real-time view of a running system.
  - PID (Process ID): The unique identifier for each process.
  - USER: The user or owner of the process.
  - PR (Priority): The priority of the process.
  - NI (Nice Value): The "niceness" of the process.
  - VIRT (Virtual Memory): The total virtual memory used by the process.
  - RES (Resident Memory): The non-swapped physical memory used by the process.
  - SHR (Shared Memory): The shared memory used by the process.
  - S (%CPU): The percentage of CPU usage by the process.
  - MEM (%MEM): The percentage of RAM usage by the process.
  - TIME+: The total CPU time the process has used since it started.
  - COMMAND: The command or program associated with the process
- A useful combo for redirecting the non-commented lines in a file, to another file:
  - `grep -Ev '^($|#)' <path-to-file> | wc -l > <path-to-new-file>`
- Getent displays entries from databases supported by the Name Service Switch libraries, which are configured in /etc/nsswitch.conf.
  - `getent hosts`
  - `getent group`
  - `getent passwd`
  - `getent shadow`
  - `getent services`
