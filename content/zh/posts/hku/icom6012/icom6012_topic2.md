---
title: "ICOM6012 Topic 2 The Big Picture"
date: 2020-10-05T09:06:09+08:00
draft: false
tags: ["hku","internet","icom6012"]
categories: ["Notes"]
authors:
- "Arthur"
---

# ICOM6012 Internet Infrastructure Technologies

## Topic 2 The Big Picture

**The Internet: "nuts and bolts" view**
* Billions of connected computing devices
  * Host = end system
  * Running network apps
  * Internet of things (IoT)
* Packet switches
  * routers
  * switchers
* Communication links
  * Fiber, copper, radio, satellite
  * Transmission rate: bandwidth
* Networks
  * Collection of devices, routers, switches, links
  * Managed by an organization
* Internet: "network of networks"
  * Interconnected ISPs
* Protocols
  * Control sending, receiving of messages
* Internet standards
  * RFC: Requests for Comments
  * IETF: Internet Engineering Task Force
  * IEEE: Institute of Electronical & Electronic Engineering

**The Internet: a "service" view**
* Infrastructure
  * Web
  * Streaming video
  * Multimedia teleconferencing
  * Email
  * Games
  * E‐Commerce
  * Social media
  * Inter‐connected appliances
  * ...
* Programming interface
  * Sending/receiving apps
  * Service options

**Protocol**
* Activities in the Internet involving two or more remote entities are governed by a protocol
* Protocols are running everywhere in the Internet

***A protocol defines the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.***

**Network Standards**
* [IETF](https://ietf.org/standards/)
  * Application
  * Transport
  * Network
* [IEEE](https://ieeexplore.ieee.org/browse/standards/collection/ieee)
  * Data link
  * Physical

**Network Edge**
* Hosts
  * Clients
  * Servers (always in data centers)

**Access Networks, Physical Media**
* Residential access networks (cable-based)
  * Frequency Division Multiplexing (FDM)
    * Different channels transmitted in different frequency bands
    * Modem = Modulator + Demodulator
      * A device that converts data from digital format into one suitable for a transmission medium
  * HFC: hybrid fiber coax
    * Asymmetric: up to 40 Mbps – 1.2 Gbs downstream transmission rate, 30‐100 Mbps upstream transmission rate
  * Network of cable, fiber attaches homes to ISP router
    * Homes share access network to cable headend
* Residential access networks: digital subscriber line (DSL)
  * Use existing telephone line to central office DSLAM
    * Data over DSL phone line goes to Internet
    * Voice over DSL phone line goes to telephone network
* Wireless access networks
  * Wireless local area networks (WLANs)
    * Within or around building (~100ft)
    * 802.11b/g/n (WiFi) - 11,54,450 Mbps
  * Wide-area cellular access networks
    * Mobile (10km)
    * 4G/5G cellular networks - 10 Mbps
  * IoT
    * BLE
    * ZigBee
    * LoRa
  * Remote areas
    * Satellite network: Geosynchronous Equatorial Orbit (GEO)
      * 35,786 km above equator
      * Large RTT (Round trip time): 0.5s
      * Expensive
      * Slow
      * Examples
        * ["Project Loon" -- Google](https://www.youtube.com/watch?v=OFGW2sZsUiQ)
        * [Starlink ‐‐ SpaceX](https://www.youtube.com/watch?v=giQ8xEWjnBs&t=13s)
* Enterprise access networks (school, company)
  * Mix of wired, wireless link technologies
    * Ethernet
      * Wired access at 100Mbps, 1Gbps, 10Gbps
    * WiFi
      * Wireless access points at 11, 54, 450 Mbps

**History of IEEE 802.11 (Use CSMA/CA)**
* Unlicensed ISM - 1985
* 802.11 - 1997
  * 2.4GHz
  * DSSS & FHSS
  * 1,2Mbps
* 802.11b - 1999 (WiFi-1)
  * 2.4GHz
  * DSSS
  * 11Mbps
* 802.11a - 1999 (WiFi-2)
  * 5GHz
  * OFDM
  * 54Mbps
* WiFi Alliance - 1999
* 802.11g - 2003 (WiFi-3)
  * 2.4GHz
  * 54Mbps
* 802.11-2007 - 2007
  * Combined 802.11a/b/g
* 802.11n - 2009 (WiFi-4)
  * MIMO, 2.4 or 5GHz
  * 600Mbps
* 802.11-2012
  * Combined 802.11a/b/g/n
* 802.11ac - 2013 (WiFi-5)
  * 5GHz
  * 7Gbps
* 802.11ah - 2017
* 802.11ax - 2020 (WiFi-6)
  * 5GHz
  * OFDMA
  * 9.6Gbps

**Links: Physical Media**
* Twisted pair (TP)
  * Two insulated copper wires
    * Category 5: 100Mbos, 1Gbps Ethernet
    * Category 6: 10Gbps Ethernet
* Coaxial cable
  * Two concentric copper conductors
  * Bidiretional
  * Broadband
    * Multiple frequency channels on cable
    * 100 Mbps per channel
* [Fiber optic cable](https://youtu.be/jZOg39v73c4)
  * Glass fiber carrying light pulse a bit (each pulse a bit)
  * High-speed point-to-point transmission (10-100Gbps)
  * Low error rate
    * Repeaters spaced far apart
    * Immune to electromagnetic noise
* Wireless radio
  * Signal carried in electromagnetic spectrum
  * No physical "wire"
  * Propagation environment effects
    * Reflection
    * Obstruction by objects
    * Interference

**Network Core**

*Mesh of interconnected routers*

* Packet-switching (hosts break application-layer messages into packets)
  * Forward packets from one router to the next
  * Each packet transmitted a full link capacity

* Packet transmission delay

![packet_switch](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/packet_switch.png)

```sh
	Packet transmission delay = L (bits) / R (bits/sec)
```

* End-end delay

![store_and_forward](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/store_and_forward.png)

```sh
	End-end delay = 2L (bits) / R (bits/sec)
	(Assuming zero propagation delay)
```

* Store and forward: entire packet must arrive at router before it can be transmitted on next link

* Packet queuing and loss
  * If arrival rate > transmission rate, packets will queue
  * If memory fills up, packets can be dropped
  * Bigger buffer can bring lower packet loss but higher delay+buffer cost

* Two key network-core functios
  * Forwarding
    * Local action: input link -> output link
  * Routing
    * Global action: source -> destinatin
    * Routing algorithms

* Circuit switching
  * End-end resources allocated to, reserved for "call" between source&dest

![circuit_switching](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/circuit_switching.png)

* Frequency Division Multiplexing (FDM)

![fdm](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/fdm.png)

* Time Division Multiplexing (TDM)

![tdm](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/tdm.png)

**Packet Switching vs. Circuit Switching**
* Packet switching is great for bursty data
  * Resource sharing
  * Simpler, no call setup
* Packet switching can cause excessive congestion
* Combined: Virtual Circuit Packet Switching

**Internet Structure: Network of networks**
* Hosts connected to internet
* Access ISPs (Internet Service Providers)
  * To ensure every two hosts can send packets to each other, access ISPs must be interconnected

![isp_tiers](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/isp_tiers.png)

* Tier-1 ISP
  * Sprint, AT&T, NTT
  * National & international coverage
* Content provider network (private network)
  * Google
  * Facebook

**Delay and Loss**
* Nodal processing
* Queueing delay
* ![queueing_delay](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/queueing_delay.png)
  * R: link bandwidth (bps)
  * L: packet length (bits)
  * a: average packet arrival rate
  * Traffic intensity = La / R
  * E(x) = La/R / (1 - La/R)
* Transmission delay
  * L(packet length) / R (link bandwidth)
* Propagation delay
  * d (length of physical link) / s (propagation speed)

![packet_delay](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/packet_delay.png)

```sh
	d(nodal) = d(proc) + d(queue) + d(trans) + d(prop)
```

**Example**

```sh
	Number of hops = M
	Per-hop processing delay = d(proc)
	Link propagation delay = d(prop)
	Packet transmission delay = d(trans)
	Message size = N packets

	End-to-end Delay (ignoring queueing delay)
	= M * d(prop) + N * d(trans) + (M-1) * d(trans) + (M-1) * d(proc)
```

![timing_diagram](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/timing_diagram.png)

**"Real" Internet delays and routes: traceroute [YouTube](https://www.youtube.com) (macOS)**

```zsh
➜  ~ traceroute youtube.com
traceroute to youtube.com (216.58.197.110), 64 hops max, 52 byte packets
 1  172.24.172.1 (172.24.172.1)  14.211 ms  1.584 ms  1.635 ms
 2  118.140.125.65 (118.140.125.65)  13.122 ms  23.362 ms  7.402 ms
 3  10.30.31.17 (10.30.31.17)  7.024 ms  23.736 ms  54.474 ms
 4  10.28.21.37 (10.28.21.37)  5.924 ms  3.565 ms  2.954 ms
 5  * * *
 6  * 218.188.28.165 (218.188.28.165)  214.507 ms  3.344 ms
 7  108.170.241.65 (108.170.241.65)  3.595 ms
    72.14.222.9 (72.14.222.9)  10.840 ms  3.377 ms
 8  108.170.241.65 (108.170.241.65)  3.156 ms
    216.239.62.59 (216.239.62.59)  3.495 ms
    216.239.62.57 (216.239.62.57)  2.733 ms
 9  216.239.62.59 (216.239.62.59)  4.698 ms
    hkg12s01-in-f14.1e100.net (216.58.197.110)  3.252 ms  4.355 ms
```

**Packet Loss**
* Queen (buffer) preceding link in buffer has finite capcity
* Packet arriving to full queue dropped (lost)
* Lost packet may be retransmitted by previous node, end system or not at all

![packet_loss](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/packet_loss.png)

**Throughput**
* Rate (bits/time) at which bits transferred from sender to receiver
  * Instantaneous: rate at given point in time
  * Average: rate over longer period of time
* Bottleneck link
  * link on end-end path that constrains end-end throughput
  * ![throughput](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/throughput.png)
  * Per-connection end-end throughput
    * min(Rc, Rs, R/10)
    * In practice, Rc or Rs is often bottleneck

**Why Layering**
* Explicit structure allows identification, relationship of complex system's pieces
* Modularization eases maintenance, updating of system

**Internet Protocol Stack**
* Application - supporting network applications
  * FTP
  * SMTP
  * HTTP
* Transport - process data transfer
  * TCP
  * UDP
* Network - routing of datagrams from source to destination
  * IP
  * Routing protocol
* Link - data transfer between neighboring network elements
  * Ethernet
  * WiFi
  * PPP
* Physical - bits "on the wire"

**ISO/OSI Reference Model (Implemented in Application)**
* Presentation
  * Allow applications to interpret meaning of data
* Session
  * Synchronization, checkpoint, recovery of data exchange

**Encapsulation**

![encapsulation](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/encapsulation.png)

**Network Security**
* Fields of network security
  * How bad guys can attack computer networks
  * How we can defend networks against attacks
  * How to design architectures that are immune to attacks
* Internet not originally designed with much security in mind

**Bad Guys**
* Malware
  * From
    * Virus
    * Worm
  * Spyware malware
  * Usage
    * Botnet
    * Spam
    * DDos attacks
* Denial of service (DoS)
  * Make resources (server, bandwidth) unavailable to legitimate traffic by overwhelming resource with fake traffic
  * Procedures
    1. Select target
    2. Break into hosts around the network
    3. Send packets to target from compromised hosts 
* Packet interception
  * Packet "sniffing"
  * ![packet_sniffing](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/packet_sniffing.png)
    * Broadcast media (shared ethernet, wireless)
    * Promiscuous network interface reads/records all packets
* Fake identity
  * IP spoofing: send packet with false source address
  * ![ip_spoffing](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/ip_spoffing.png)

**Use's View Of Internet**
* Single large (global) network
  * Achieved through software that implements abstractions
* User's computers all attach directly
* No other structure visible

![user_view_internet](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/user_view_internet.png)
**Internet History**
* Early packet-switching principles (1961-1972)
* Internetworking, new and proprietary nets (1972-1980)
* New protocols, a proliferation of networks (1980-1990)
* Commercialization, the Web, new apps (1990's, 2000's)
* More new applications, Internet is "everywhere" (2005-Present)