---
title: "ICOM6012 Topic 4 Transport Layer"
date: 2020-10-20T09:37:44+08:00
draft: false
tags: ["hku","internet","icom6012"]
categories: ["Notes"]
authors:
- "Arthur"
---

# ICOM6012 Internet Infrastructure Technologies

## Topic 4 Transport Layer

## Actions

### Sender
- Get application layer message
- Determine segment header fields values
- Create segment
- Pass segment to IP

### Receiver

- Receive segment from IP
- Check header values
- Extract application layer message
- Demultiplexes message up to application via socket

## Services

### Provide logical communication between processes

### Run in end system

- Send side
	- Break app messages into segment
	- Pass to network layer
- Receive side
	- Reassembles segments into messages
	- Pass to application layer

## Protocols

### TCP
- Features
	- Point-to-point
		- One sender, one receiver
	- Reliable, in-order byte system
		- No message boundaries
	- Full duplex data
		- Bi-directional data flow in same connection
		- MSS: maximum segment size (excluding header)
	- Cumulative ACKs
	- Pipelining
		- TCP congestion and flow control set window size
	- Flow Control
		- Sender will not overwhelm receiver
	- Congestion control
- Concepts
	- Segment structure
	- Sequence numbers
		- Byte stream "number" of first byte in segment's data 
	- Acknowledgements (ACKs)
		- Seq # of next byte expected from other side
		- Cumulative ACKs
- Procedure
	- Connection-oriented
		- Handshaking initializes sender, receiver state before data exchange
		- TCP socket identified by 4-tuple
			- Source IP
			- Source Port #
			- Dest IP
			- Dest Port #
		- Server host may support many simultaneous TCP sockets
		- Web servers have different sockets for each connecting client
(Non-persistent HTTP will have different socket for each request)
		- Demux
			- Receiver uses all four values to direct segment to appropriate socket
	- 3-way handshake
		- Connection setup
	- Connection management
		- Handshake
			- Agree to establish connection
			- Agree on connection parameters
	- Retransmission
	- Closing a connection
- Events
	- Data received from application
		- Create segment with seq # (a byte-stream number of first data byte in segment)
		- Start timer if not already running
			- Think of timer as for oldest unACKed segment
			- Expiration interval: TimeOutInterval
	- Timeout
		- Retransmit segment that caused timeout
		- Restart timer
	- ACK received
		- Update what is known to ACKed
		- Start timer if there are still unACKed segment
- Shortcomings
	- SYN DoS Attack
		- Half-open TCP connections consume all the TCP connection resources
		- SYN packet with a spoofed source address

### UDP
- Features
	- No frills
	- Bare bones
	- "Best effort"
		- Lost 
		- Delivered out-of-order to app
	- No handshaking
	- Handle independently
	- Services not available
		- Delay guarantee
		- Bandwidth guarantee

- Concepts
	- Segment format
		- Source port #
		- Dest port #
		- Length
		- Checksum
			- Detect errors
				- Sender
					- Treat segement contents
					- Checksum: 1's complement sum
					- Put checksum into UDP field value
				- Receiver
					- Compute checksum of received segment
					- Check equality
						- No: error detected
						- Yes: no error detected (not sure)
			- Checksum calculation may be disabled in order to speed up the processing
- Procedure
	- Connectionless demux
		- Create socket with unique local port #
		- Sender side: create datagram to send into UDP socket
			- Dest IP
			- Dest port #
		- Receive side: receive UDP segment
(IP datagrams with same dest port #, but different source will be directed to same socket)
			- Check dest port #
			- Direct UDP segment to socket with that port #
- Utilization
	- Streaming multimedia apps
		- Loss tolerant
		- Rate sensitive
	- DNS
	- SNMP
	- HTTP/3
- Shortcomings
	- Need reliability at application layer
	- Congestion control

### SCTP

### DCCP

## Multiplexing and Demultiplexing

### Multiplexing at sender
- Handle data from multiple sockets, add transport header

### Demultiplexing at receiver
- Handle data info to deliver received segments to correct socket

### Host receivers IP datagram (Host uses IP & port # to redirect segment)
- Source IP
- Dest IP
- One transport layer segment
	- Source port #
	- Dest port #

## Congestion Control

### Cause
- Too many sources sending too much data too fast for network to handle

### Manifestations
- Long delay
	- Queueing in router buffers
- Packet loss
	- Buffer overflow at network

### Approaches
- End-end congestion control
	- Features
		- No explicit feedback from network
		- Congestion inferred from observed loss, delay
- Network-assisted congestion control
	- Features
		- Routers provide direct feedback to hosts with flow passing through congested router
		- May indicate congestion level or explicit set sending rate
		- TCP ECN ATM DECbit protocols

### TCP Congestion Control
- AIMD
	- Sender can increase sending rate until packet loss occurs, then decrease
	- Additive increase
		-  1 MSS (maximum segment size) until loss detected
	- Multiplicative decrease
		- Cut sending rate in half at each loss event
- Detecting, reacting to loss
	- ACKs problem
		- cwnd is cut in half
		- Window grow linearly
	- Timeout event
		- cwnd is set to 1 MSS
		- Window grow exponentially to threshold, then linearly
- TCP slow start
	- Initially cwnd = 1 MSS
	- Double cwnd every RTT
	- Done by incrementing cwnd for every ACK received