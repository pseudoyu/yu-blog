---
title: "Analysis and Reflections on IPFS Distributed Storage Protocol"
date: 2021-03-25T16:30:17+08:00
draft: false
tags: ["blockchain", "ipfs", "storage"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've been working on a school Case Study project, which is a music copyright management project based on the `Ethereum` platform. It uses IPFS distributed file storage technology for uploading music works and copyright proof documents, mainly utilizing its deduplication feature to detect infringement. I became interested in the IPFS system and read the [IPFS series articles](https://tech.hyperchain.cn/tag/ipfs/) on the [QTech platform](https://tech.hyperchain.cn). I also consulted some related materials and will summarize them in this article. If there are any errors or omissions, please feel free to discuss and correct them.

## Overview

When we use cloud storage or other services in our daily lives, we mostly access files on specific servers (IP addresses), request files, and download them locally through the HTTP protocol. This is essentially based on location addressing, accessing URLs to find specific files layer by layer. While this method is convenient, it has some problems. Files rely on specific servers, so if the centralized server goes down or the file is deleted, the content will be permanently lost. Additionally, if the server is far away or many people are accessing the file simultaneously, the access speed will be slow. Moreover, the same file may be stored repeatedly on different servers, causing a waste of resources. Furthermore, there are serious security risks, as attacks such as DDoS, XSS, and CSRF may threaten file security.

> Is there a better solution?

Imagine if we stored files in a distributed network where each node could store files, and users could request files from the nearest node through a directory index-like approach. This is the solution approach of the IPFS (InterPlanetary File System), which is a peer-to-peer hypermedia file storage, indexing, and exchange protocol initiated by Juan Benet in May 2014.

### Features

IPFS aims to connect all computing devices with the same file system worldwide, building a distributed network to replace the traditional centralized server model. Each node can store files, and users can obtain files through a `DHT (Distributed Hash Table)`, making it faster, more secure, and with stronger network security.

Because files stored through IPFS have their content stored as addresses by calculating Hash values in blocks, it is essentially a decentralized but content-addressed method. By encrypting the data itself, a unique Hash is generated for lookup. In this way, even a tiny change will result in a completely different Hash, making it easy to detect content tampering from the Hash without accessing the file itself.

Unlike traditional server models, IPFS is a unified network. Therefore, files with the same content that have already been uploaded will not be stored repeatedly (verifiable through Hash values), greatly saving overall network resources and improving efficiency. Theoretically, as long as the number of nodes reaches a certain scale, files will be permanently preserved, and the same file can be downloaded from multiple (and closer) nodes, improving communication efficiency.

Moreover, due to distributed network storage, it can naturally avoid traditional attacks such as DDoS.

### Functions

In addition to file storage, IPFS also has functions like DHT networking and Bitswap file exchange, which will be explained in separate blog posts later.

## Working Principle

As a file storage system, uploading and downloading files are the two most basic operations. Let's explain the principles of each.

### IPFS add Command

> In the IPFS system, executing the add operation completes the upload operation. How is it uploaded?

In the IPFS file storage system, whenever a new file is uploaded, the system divides the single file into several 256KB blocks. Each block has a unique CID for identification, which will be explained in detail later. Then, it calculates the Hash value of each block and stores it in an array. Finally, it calculates the Hash of this array to get the final Hash value of the file. Then, it creates an object consisting of the file's Hash and the array of all block Hashes, forming an index structure. Lastly, it uploads all file blocks and this index structure to the IPFS node, synchronizing with the IPFS network.

There are two noteworthy situations when uploading files: 1. If the file is particularly small, less than 1KB, it won't waste a block and will be uploaded directly with the Hash to IPFS. 2. If the file is particularly large, for example, if a 1GB video was uploaded before and then a few KB of subtitle file was added, in this case, the unchanged 1GB part will not be reallocated new space, but only the added subtitle file part will be allocated new blocks, and the Hash will be re-uploaded.

Therefore, it's easy to understand that even the same parts of different files will only be stored once, and the indexes of many files will point to the same block, forming a MerkleDAG data structure.

It's worth noting that when a node executes the add operation, it will be kept in the local blockstore, but it won't be actively uploaded to the IPFS network immediately. In other words, the nodes connected to it will not store this file unless a certain node has requested that block data! Therefore, it is not an automatic backup distributed database. IPFS designed it this way considering network bandwidth, reliability, and other aspects.

Another detail is that when a node executes the `add` command, it will also broadcast its block information and maintain a list of all block requests sent to this node. Once the add command adds data that satisfies this list, it will actively send data to the corresponding nodes and update the list.

### IPFS get Command

> After the file is uploaded, how to search and access it?

This relates to the IPFS index structure mentioned above, which is `DHT` (Distributed Hash Table). By accessing `DHT`, data can be accessed quickly.

![ipfs_dht](https://image.pseudoyu.com/images/ipfs_dht.png)

> What if you want to find data that is not locally available?

![ipfs_get](https://image.pseudoyu.com/images/ipfs_get.gif)

In the IPFS system, all nodes connected to the current node form a swarm network. When a node sends a file request (i.e., `get`), it first searches for the requested data in the local blockstore. If not found, it will send a request to the swarm network and find the node that has the data through the `DHT Routing` in the network.

> How do you know which node(s) in the network have this requested file?

As mentioned in the `add` command above, when a node joins the IPFS network, it tells other nodes what content it has stored (by broadcasting `DHT`). This way, whenever a user wants to retrieve content that happens to be on this node, other nodes will tell the user to get the content they want from this node.

Once the node with this data is found, the requested data will be fed back, and the local node will cache a copy of the received block data in the local blockstore. This way, the entire network has an additional copy of the original data, making it easier to find when more nodes request the data. Therefore, the non-loss of data is based on this principle. As long as one node keeps this data, it can be obtained by the entire network.

> In the project, uploaded files can be directly accessed through the `ipfs.io` gateway, similar to website addresses like `https://ipfs.io/ipfs/Qm.....`. What's the principle behind this?

![ipfs_io_get](https://image.pseudoyu.com/images/ipfs_io_get.gif)

The `ipfs.io` gateway is actually an IPFS node. When we open the above web link, we are actually sending a request to this node. Therefore, the `ipfs.io` gateway will help us request this block from the node that has this data (if this file was just added to the local node through the `add` command, it will be uploaded to the IPFS network in this way). After obtaining the data through `DHT Routing` in the `swarm` network, the gateway will cache a copy itself and then send the data to us via HTTP protocol. Thus, we can see this file directly in the browser!

When any other machine accesses this link through a browser, since the `ipfs.io` gateway has already cached this file, when requesting again, it doesn't need to request data from the original node but can directly return data from the cache to the browser.

### Content Identifier CID

Now consider another question: we are familiar with image formats like `.jpg`, `.png`, and common video formats like `.mp4`, which can be directly judged by the file extension. Files uploaded through IPFS can also be of multiple types and contain a lot of information. How to distinguish them?

In the early stages of IPFS, it mainly used `base58btc` to encode `multihash`, but in the process of developing IPLD (mainly used to define data and model data), many format-related issues were encountered. Therefore, a file addressing format called `CID` was used to manage data of different formats. The official definition is:

> `CID` is a self-describing content-addressed identifier that must use a cryptographic hash function to obtain the address of the content

In simple terms, `CID` uses some mechanisms to self-describe the content contained in the file, including version information, format, etc.

#### CID Structure

Currently, there are two versions of `CID`: `v0` and `v1`. The `v1` version of `CID` is generated by `V1Builder`

```sh
<cidv1> ::= <mb><version><mcp><mh>
# or, expanded:
<cidv1> ::= <multibase-prefix><cid-version><multicodec-packed-content-type><multihash-content-address>
```

As shown in the code listed above, the mechanism used is called `multipleformats`, mainly including: `multibase-prefix` indicates that `CID` is encoded into a string, `cid-version` indicates the version variable, `multicodec-packed-content-type` indicates the type and format of the content (similar to the suffix, but as part of the identifier, the supported formats are limited, and users cannot modify them arbitrarily), `multihash-content-address` indicates the hash value (allowing `CID` to use different hash functions).

Currently, the `multicodec-packed` encodings supported by `CID` include native `protobuf` format, `IPLD CBOR` format, `git`, Bitcoin and Ethereum objects, etc., and support for more formats is being gradually developed.

Detailed explanation of `CID` code:

```go
type Cid struct {str string}
type V0Builder struct {}
type V1Builder struct {}

Codec uint64
MhType uint64
MhLength int // Default: -1
```

`Codec` represents the encoding type of the content, such as `DagProtobuf`, `DagCBOR`, etc. `MhType` represents the hash algorithm, such as `SHA2_256`, `SHA2_512`, `SHA3_256`, `SHA3_512`, etc. `MhLength` represents the length of the generated hash.

The `v0` version of `CID` is generated by `V0Builder`, starting with the string `Qm`, backward compatible, with `multibase` always being `base58btc`, `multicodec` always being `protobuf-mdag`, `cid-version` always being `cidv0`, and `multihash` represented as `cidv0 ::= <multihash-content-address>`.

#### Design Philosophy

Through the binary nature of `CID`, the compression efficiency of file hashes is greatly improved, so it can be directly used as part of the URL for access; the encoding form of `multibase` (such as `base58btc`) shortens the length of `CID`, making it easier to transmit; it can represent the results of any format and any hash function, which is very flexible; it can upgrade the encoding version through the `cid-version` parameter in the structure; it is not limited by historical content.

### IPNS

As mentioned above, changes in file content in IPFS will cause changes in its hash value. In practical applications, if applications that need version updates and iterations, such as websites hosted through IPFS, are accessed through updated hashes each time, it is very inconvenient. Therefore, a mapping scheme is needed to ensure user experience, so that users only need to access a fixed address when accessing.

`IPNS (Inter-Planetary Naming System)` provides such a service. It provides a hash ID (usually PeerID) limited by a private key to point to specific IPFS files. After the file is updated, the hash ID's pointer will be automatically updated.

Even though the hash value can remain fixed, it is still not easy to remember and input. Therefore, there is a further solution.

IPNS is also compatible with DNS. You can use the `DNS TXT` record to record the IPNS hash ID corresponding to the domain name, so you can use the domain name to replace the IPNS hash ID for access, making it easier to read, write, and remember.

## Conclusion

The above is a summary of the principles of IPFS distributed storage. Its components, storage process details, GC mechanism, data exchange module Bitswap, network, and practical application scenarios all have many aspects worth exploring in depth.

> Recommended reading: QTech Platform of Hyperchain Technology《[IPFS Series Articles](https://tech.hyperchain.cn/tag/ipfs/)》

## References

> 1. [IPFS Official Website](https://ipfs.io)
> 2. [This is How IPFS Stores Files](https://tech.hyperchain.cn/ipfs/), *QTech, Hyperchain Technology*
> 3. [How Does IPFS Actually Work?](https://cloud.tencent.com/developer/news/277198), *Zhihui*
> 4. [Understanding What IPFS is from Web3.0 Perspective](https://learnblockchain.cn/2018/12/12/what-is-ipfs), *Tiny Bear, Dengchain Community*
> 5. [IPFS CID Research](https://medium.com/@kidinamoto/ipfs-cid-研究-717c4ceb14a0), *Sophie Huang*