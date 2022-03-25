---
title: "ICOM6012 Topic 3 Application Layer"
date: 2020-10-19T17:50:44+08:00
draft: false
tags: ["hku","internet","icom6012"]
categories: ["Notes"]
authors:
- "Arthur"
---

# ICOM6012 Internet Infrastructure Technologies

## Topic 3 Application Layer

**Creating a Network App**
* Run on different end systems
* Communication over network
* No need to write for network-core devices

**Client-Server Architecture (The Centralized Internet)**
* Server
  * Always-on host
  * Permanent IP address
  * Often in data centers (for scaling)
* Clients
  * Contact, communicate with server
  * May be intermittently connected
  * May have dynamic IP addresses
  * Don't communicate directly with each other

**Peer-to-Peer (P2P) Architecture**
* No always-on server
* Arbitrary end systems directly communicate
* Peers request service from other peers, providing service in return to other peers
  * Self scalability - new peers bring new service capacity, as well as new service demands
* Peers are intermittently connected with dynamic IP addresses
  * Complex management

**Processes Communicating**
* Process: program running within a host
  * Same host
    * Inter-process communication (defined by OS)
  * Different hosts
    * Exchanging messages
  * Client, servers
    * Client process: process that initiates communication
    * Server process: process that waits to be contacted
    * Applications with P2P architecture have both

**Sockets**
* Process sends/receives messages to/from its socket

![sockets](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sockets.png)

**Addressing Processes**
* To receive messages, process must have identifier
  * IP address
    * Host has unique 32-bits IP address
  * Port number
    * Port 0 - 1023: Well-known
      * HTTP server: 80
      * Mail server: 25
    * Port 1024 - 49151: Registered ports
    * Port > 49151: Dynamic/private ports

**An Application-Layer Protocol Defines**
* Types of messages exchanged
  * Request
  * Response
* Message syntax
  * What field
  * How fields are delineated
* Message semantics
  * Meaning of information in fields
* Rules
  * When and how process send & respond to messages
* Protocols
  * Open protocols
    * Defined in RFCs (by IETF)
    * Everyone has access to protocol definition
    * Allow for interoperability
    * Example
      * HTTP
      * SMTP
  * Proprietary protocols
    * Skype
    * Zoom

**Transport Service**
* Data integrity
* Timing
* Throughput
* Security

![transport_service](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/transport_service.png)

**Internet Transport Protocols Services**
* TCP service
  * Connection-oriented
  * Reliable transport
  * Flow control
  * Congestion control
  * Doesn't provide
    * Timing
    * Minimum throughput guarantee
    * Security
* UDP service
  * Unreliable data transfer
  * Doesn't provide
    * Reliability
    * Flow control
    * Congestion control
    * Timing
    * Throughput guarantee
    * Security
    * Connection setup

![transport_protocols](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/transport_protocols.png)

**Securing TCP**
* TCP & UDP
  * No encryption
  * Cleartext passwords sent into socket traverse Internet in cleartext
* SSL (Secure Socket Layer) / TLS (Transport Layer Security)
  * Provides encrypted TCP connection
  * Data integrity
  * End-point authentication
* SSL/TLS is at Application Layer
  * Apps use SSL/TLS libraries, which "talk" to TCP
  * Cleartext passwords sent into socket traverse Internet encrypted

![ssl_tls](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/ssl_tls.png)

**The IP Hourglass**

![ip_hourglass](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/ip_hourglass.png)

**HTTP Overview**
* HTTP: Hypertext Transfer Protocol
* Web's application-layer protocol
* Client/Server model
  * Client - browser that requests, receives and "display" web objects
  * Server - Web server sends objects in response to requests
* Development
  * HTTP/1.0: RFC 1945 (1996)
  * HTTP/1.1: RFC 2616 (1997)
  * HTTP/2: RFC 7540 (2015)
  * HTTP/3: Internet-Draft (2020)
* Uses TCP
  * Client initiates TCP connection (create sockets) to server, port 80
  * Server accepts TCP connection from client
  * HTTP messages exchanged between browser and web server
  * TCP connection closed
* HTTP is stateless
  * Server maintains no information about past client requests

**HTTP Connections**
* Non-persistent HTTP
  * Downloading multiple objects required multiple connections
    * Sequential
    * Parallel
  * Procedures
    * TCP connection opened
    * At most one object sent over TCP connection
    * TCP connection closed
  * OS must work and allocate host resources for each TCP connection
  * Browser often open parallel TCP connections to fetch referenced objects
  * HTTP response time (2RTT+)
    * RTT: Time for a small packet to travel from client to server and back
    * 1RTT to initiate TCP connection
    * 1RTT for HTTP request and first few bytes of HTTP response to return
    * File transmission time
* Persistent HTTP
  * Procedures
    * TCP connection opened to a server
    * Multiple objects can be sent over single TCP connection between clients and that server
    * TCP connection closed
  * Server leaves connection open after sending response
  * Subsequent HTTP messages between same client/server are sent over connection
* Persistent HTTP without pipelining
  * Client issues new request only when previous response has been received
  * 1RTT for each referenced object
  * Head-of-line (HoL) blocking
* Persistent HTTP with pipelining
  * Client sends requests as soon as it encounters a referenced object
  * As little as 1RTT for all the referenced objects
  * *Not activated in practice*

**HTTP Message**
* Request
  * In ASCII (human readable format)
  * ![http_request](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/http_request.png)
  * Methods
    * POST
    * GET
    * HEAD
    * PUT
* Response
  * ![http_response](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/http_response.png)
  * Statu Code
    * Informational, 1XX
    * Successful, 2XX, (200 OK)
    * Redirection, 3XX, (301 Moved Permanently)
    * Client Error, 4XX, (400 Bad Request, 404 Not Found)
    * Server Error, 5XX, (505 HTTP Version Not Support)

**Cookies**
* Components
  * Cookie header line of HTTP response message
  * Cookie header line in next HTTP request message
  * Cookie file kept on user's host, managed by user's browser
  * Back-end database at website
* Example
  * ![cookie_example](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cookie_example.png)
* 3rd-party cookies
  * Many sites use third party advertisements
  * The third party can set a cookie that identifies the user
  * This cookie is sent to the third party each time an ad is downloaded by the user’s browser along with the address of the page that contains the link to the ad
  * ![3_party_cookies](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/3_party_cookies.png)

**Web Caches (Proxy Servers)**
* Goal
  * Satisfy client request without involving origin server
* User configures browser to point to a web cache
* Browser sends all HTTP requsets to cache
    * If object in cache: cache returns object
    * Else: cache requests object from origin server, then returns object to client

**Conditional GET**
* Goal
  * Don't send object if cache has up-to-date cached version
    * No object transmission delay
    * Lower link utilization
* Cache: specify date of cached copy in HTTP request
* Server: response contains no object if cached copy is up-to-date

![conditional_get](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/conditional_get.png)

**HTTP/2**
* Goals
  * Backward compatible with HTTP 1.1
  * Improve page load speed
    * Data compression of HTTP headers
    * HTTP/2 Server Push
    * Pipelining of requests
    * Fixing the head-of-line blocking problem in HTTP 1.1
    * Multiplexing multiple requests over a single TCP connection
  * Mitigating HOL blocking
    * Objects divided into frames, frame transmission interleaved

**HTTP/2 to HTTP/3**
* Goal
  * To further decrease delay in multi-object HTTP requests
* HTTP/2 over single TCP connection means
  * Recovery from packet loss still stalls all object transmissions => Head-of-line blocking!
* HTTP/3 over UDP (to address the HoL blocking)
  * Adds security, per object error and congestion-control

**Email**
* Components
  * User agents
    * Composing, editing, reading mail messages
    * Outgoing, incoming messages stored on server
  * Mail server
    * Mailbox
    * Message queue
  * SMTP (Simple Mail Transfer Protocol)
    * Client: Sending mail server
    * Server: Receiving mail server

**SMTP [RFC 5321]**
* Uses TCP to reliably transfer email message from client to server, port 25 (or 587)
* Direct transfer: sending server to receiving server
* Three phases of transfer
  * Handshaking (greeting)
  * Transfer of messages
  * Closure
* Command/response interaction (like HTTP, FTP)
  * Commands: ASCII text
  * Response: status code and phrase
* Messages must be in 7-bit ASCII
* Uses persistent connections
* use *CRLF.CRLF* to determine end of message
* Example
  * ![smtp_example](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/smtp_example.png)

**Mail Message Format**
* RFC 822: standard for text message format
  * Header lines (different from SMTP MAIL FROM, RCPT TO commands)
    * To
    * From
    * Subject
  * Body (the message)
    * ASCII characters only

**Message Format: multimedia extensions**
* MIME (multipurpose internet mail extension): multimedia mail extension (to RFC 822), RFC 2045, 2056
* Additional lines in msg header declare MIME content type
* ![mail_mime](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mail_mime.png)

**Mail Access Protocols**

![mail_access_protocols](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mail_access_protocols.png)

* SMTP
  * Delivery/storage to receiver's server
* Mail access protocol: retrieval from server
  * POP
    * Post Office Protocol [RFC 1939]: authorization, download
  * IMAP
    * Internet Mail Access Protocol [RFC 1730]: more features, including manipulation of stored msgs on server
* HTTP
  * Provides web-based interface on top of STMP (to send), IMAP (or POP) to retrieve e-mail messages
  * Gmail, Hotmail, etc.

**DNS (Domain Name System)**
* Why not a single centralized DNS server
  * Single point of failure
  * Traffic jam due to huge number of requests/queries
  * Long distance => slow response
  * Maintenance issue
* DNS services
  * Hostname to IP address translation
  * Host aliasing
  * Mail server aliasing
  * Load distribution
* ![dns_services](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/dns_services.png)
* Root Name Servers
  * ![root_name_servers](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/root_name_servers.png)
  * 13 LOGICAL root name servers, but 1086(or more) PHYICAL servers
  * Reply with a referral to the DNS servers for a TLD, or indicating no such TLD exists.
* TLD & authoritative servers
  * Top-level domain (TLD) servers
    * gTLD (originally 7): com, net, biz, edu, org, int, mil, ...
    * ccTLD (249): uk, cn, hk, ...
    * IDN (internationalized top-level domains): .中国, .香港 and .台灣
  * Authoritative DNS servers
    * Organization's own DNS server(s), providing authoritative hostname to IP mappings for organization’s named hosts
    * Can be maintained by organization or service provider

**Local/Default DNS Server**
* Does not strictly belong to hierarchy
* When host makes DNS query, query is sent to its local DNS server
  * Has local cache of recent name-to-address translation
  * Acts as proxy, forwards query into hierarchy
* Each ISP (residential ISP, company, university) has one
* Public DNS server
  * Google public DNS (with IP address 8.8.8.8)
* Your home WiFi router may act as your local DNS server

**DNS: Caching, Updating Records**
* Once (any) name server learns mapping, it caches mapping
  * Cache entries timeout (disappear) after some time (TTL)
  * TLD servers typically cached in local name servers
    * Root name servers not often visited
* Cached entries may be out-of-date
  * If name host changes IP address, may not be known Internet-wide until all TTLs expire
* Update/notify mechanisms proposed IETF standard
  * RFC 2136

**DNS Records**
* DNS: distributed db storing resource records (RR)
  * RR format
    * (name, value, type, ttl)
* type = A
* type = CNAME
* type = NS
* type = MX

**DNS Protocol, Messages**
* DNS query and reply messages, both with same message format
  * Message header
    * Identification
      * 16 bit
      * For query, reply to query uses same
    * Flags
      * Query or reply
      * Recursion desired
      * Recursion available
      * Reply is authoritative
  * ![dns_message](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/dns_message.png)

**Attacking DNS**
* DDoS attacks
  * Bombard root servers with traffic
    * Not successful to date
    * Traffic Filtering
    * Local DNS servers cache IPs of TLD servers, allowing root server bypass
  * Bombard TLD servers
    * Potentially more dangerous
* Redirect attacks
  * Man-in-middle
    * Intercept queries
  * DNS poisoning
    * Send bogus replies to DNS server, which caches

**Peer-to-peer File Distribution**
* P2P architecture
  * No always-on server 
  * Arbitrary end systems directly communicate
  * Self scalibility
  * Peers are intermittently connected and change IP address
  * Example
    * File distribution - BitTorrent
    * Streaming - KanKan
    * Volp - Skype

**File Distribution (Client-Server)**

![client_server_file](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/client_server_file.png)

* Server transmission
  * Must send/upload N file copies
  * Time: NF/U(s)
* Client
  * Each client must download one file copy
  * Slowest time: F/d(min)
* Time to distribute F to N
  * D(c-s) >= max {NF/U(s), F/d(min)}

**File Distribution (P2P)**
* Server transmission
  * Must upload at least one copy
  * Time: F/U(s)
* Client
  * Each client must download one file copy
  * Slowest time: F/d(min)
* All clients
  * As aggregate must download NF bits
  * Max upload rate: U(s)+NU(i)
* Time to distribute F to N
  * D(P2P) >= max {F/U(s), F/d(min), NF/(U(s)+Sum(U(i)))}

**Client-Server vs. P2P**

![p2p_cs](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/p2p_cs.png)

**P2P File Distribution: BitTorrent**
* Procedure
  * File divided into 256KB chunks
  * Peers in torrent send/receive file chucks
* Roles
  * Tracker
    * Track peers participating in torrent
  * Torrent
    * Group of peers exchanging chucks of a file
* Actions
  * Requesting chunks
    * Ask each peer for chunks they have
    * Request missing chunks (rarest piece first)
  * Sending chunks (tit-for-tat)
    * Send chunks to peers who currently sending her chunks at highest rate
    * Randomly select another peers and send chunks (for new peers)