---
layout: single
title:  "Network Concepts"
date:   2023-12-6 23:45:00 +0000
categories: linux
---
- Layer 2 and 3 of the Open Systems Interconnection (OSI) Model. An explainer.
  - Data Link Layer (Layer 2):
    - Functionality: This layer is primarily concerned with the local delivery of frames between devices on the same network.
    - Devices: Switches operate at Layer 2.
    - Addressing: Devices on this layer are identified by MAC (Media Access Control) addresses.
    - Data Unit: The frame is the basic data unit at Layer 2.
  - Network Layer (Layer 3):
    - Functionality: This layer is responsible for logical addressing, routing, and forwarding of packets between devices on different networks.
    - Devices: Routers operate at Layer 3.
    - Addressing: Devices on this layer are identified by IP (Internet Protocol) addresses.
    - Data Unit: The packet is the basic data unit at Layer 3.
- VLAN Explainer
  - VLANs (Virtual Local Area Network):
    - Purpose: VLANs are used to logically segment a physical network into multiple broadcast domains. This segmentation helps improve network performance, security, and management.
    - Functionality: Devices in the same VLAN can communicate with each other as if they are in the same physical network, even if they are not physically connected to the same switch.
    - Implementation: VLANs are often implemented in switches, and devices within the same VLAN share the same VLAN ID.
    - Isolation: VLANs provide isolation at Layer 2, meaning devices in different VLANs cannot communicate directly at the Data Link Layer.
  - Subnets:
    - Purpose: Subnets are used to divide an IP network into smaller, more manageable segments. Each subnet has its own range of IP addresses.
    - Functionality: Devices within the same subnet can communicate with each other directly without the need for routing. Routing is required for communication between devices in different subnets.
    - Implementation: Subnets are implemented at the Network Layer (Layer 3) and are associated with IP addresses.
    - Isolation: Subnets provide isolation at Layer 3. Devices in different subnets require a route to communicate.
