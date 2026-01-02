---
layout: single
title:  "Virtualization - CPU"
date:   2023-12-6 10:51:00 +0000
categories: virtualization
---
- Device mapper: A virtual block device driver framework provided by the Linux kernel, which provides an infrastructure to filter I/O for block devices (BIO). It provides a platform for filter drivers also known as targets to map to BIO to multiple block devices, or to modify the BIO while it is in transit in kernel.
  - Logical volume manager (LVM)
  - Software RAIDs
  - Dm-crypt disk encryption
  - File system snapshots

- Listing storage:
  - List block devices and logical volumes.
  - `lsblk`
  - List Device mapper devices
  - `sudo dmsetup ls`
- LVM2 Storage Layers from top to bottom:
  - Logical Volumes
    - Dev-mapper devices which are formatted and presented to the consumer as a block device.
  - Volume Groups
    - Act as storage pools, aggregating storage from the physical layer together and overcoming the limitations of physical storage size.
  - Physical
    - Disks, partitions and raw files.

  




- VDA: virtual disk
- CPU (Central Processing Unit):
  - Physical Hardware: The CPU is the physical hardware component of a computer that performs the actual processing of instructions. It executes instructions from programs, performs calculations, and manages data.

- vCPU (Virtual CPU):
  - Virtualized Instance: In a virtualized environment (such as virtual machines), a vCPU is a virtualized or emulated representation of a physical CPU core. It's a portion of the physical CPU resources allocated to a virtual machine.
  Abstraction Layer: The hypervisor (virtualization layer) creates and manages vCPUs. Each vCPU represents a share of the physical CPU's processing power.

- Relationship:

  - A vCPU is a virtual abstraction of a physical CPU core. Multiple vCPUs can be created and assigned to different virtual machines running on the same physical server.
- Key Points:

  - Allocation: The number of vCPUs assigned to a virtual machine determines the virtual machine's processing capacity. For example, a virtual machine with 2 vCPUs has access to the processing power of two physical CPU cores.


- Example:

  - If you have a physical server with a quad-core CPU (4 cores) and you create three virtual machines, each configured with 2 vCPUs, you are overcommitting the CPU resources. The hypervisor manages the allocation of physical CPU time to each vCPU based on demand.

- Note:

  - While vCPUs provide flexibility and resource isolation in virtualized environments, it's important to consider the physical CPU capabilities and avoid overcommitting resources to prevent performance degradation. The performance of virtual machines depends on the available physical CPU resources and the efficiency of the hypervisor's scheduling algorithms. You can run into performance and capacity issues

- Why virtualization?
- Complexities introduced by Virtualization: 
  - Over-committment can become a problem if performance monitoring is not done.
  - Blended storage IO: "The IO Blender Effect". Underlying memory users are all vying for the same storage, with each having distinct requirements, which can make it a challenge to properly allocate.
  - Troubleshooting becomes more complex.


  
  - Virtual Desktop
  - IO
    - Virtual ethernet, fiber, hardware connections (IO pathways)
  - Application
    - The application and all necessary dependencies.

