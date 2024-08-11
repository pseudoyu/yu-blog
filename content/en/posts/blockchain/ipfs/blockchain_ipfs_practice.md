---
title: "Setting Up an IPFS Local Node (Command Line)"
date: 2021-03-27T18:46:17+08:00
draft: false
tags: ["blockchain", "ipfs", "storage"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

In the previous article, "[IPFS Distributed File Storage Principles](https://www.pseudoyu.com/en/2021/03/25/blockchain_ipfs_structure/)", we provided a detailed introduction to the design concepts, functions, working principles, and IPNS of the IPFS system. So, how do we set up an IPFS node locally?

This article demonstrates the setup of an IPFS node (command-line version) on the `macOS 11.2.3` system, and performs actual operations on file uploading, downloading, network synchronization, `pin`, `GC`, `IPNS`, etc., to deepen the understanding of IPFS working principles.

## Code Practice

### Installation

```sh
wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_darwin-amd64.tar.gz
tar -xvzf go-ipfs_v0.8.0_darwin-amd64.tar.gz
cd go-ipfs
./install.sh
ipfs --version
```

### Startup

```sh
# Start the node
ipfs init

# Upload a file
ipfs add ipfs_init_readme.png

# Upload a file and only output the hash value
ipfs add -q ipfs_init_readme.png

# Upload a directory
ipfs add -r [Dir]

# View file
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/readme
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/quick-start

# View your uploaded file
ipfs cat QmaP3QS6ZfBoEaUJZ3ZfRKoBm3GGuhQSnUWtkVCNc8ZLTj

# View image and output to file
ipfs cat QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH > ipfsTest.png

# Download file
ipfs get QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH -o ipfsTest.png

# Compress and download file
ipfs get QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH -Cao ipfsTest.png
```

![ipfs_init_readme](https://image.pseudoyu.com/images/ipfs_init_readme.png)

### Start/Join Service

```sh
# View current node information
ipfs id

# View IPFS configuration information
ipfs config show

# Start node server
ipfs daemon
```

API service, default on port 5001, can be accessed through http://localhost:5001/webui

![ipfs_webui](https://image.pseudoyu.com/images/ipfs_webui.png)

Gateway service, default on port 8080. To access files in the browser, you need to use the gateway service provided by IPFS. The browser first accesses the gateway, and the gateway retrieves the files from the IPFS network. Access files uploaded to IPFS through http://localhost:8080/ipfs/[File Hash]

### File Operations

```sh
# List files
ipfs files ls

# Create directory
ipfs files mkdir

# Delete file
ipfs files rm

# Copy file
ipfs files cp [File Hash] /[Dest Dir]

# Move file
ipfs files mv [File Hash] /[Dest Dir]

# Status
ipfs files stat

# Read
ipfs files read
```

### Using IPNS to Solve File Update Issues

```sh
# Use IPNS to publish content for automatic updates
ipfs name publish [File Hash]

# Query the Hash pointed to by the node id
ipfs name resolve

# If multiple sites need to be updated, you can generate a new key pair and publish using the new key
ipfs key gen --type=rsa --size=2048 mykey
ipfs name publish --key=mykey  [File Hash]
```

### Pinning

When we request files from the IPFS network, IPFS synchronizes the content locally to provide services, using a Cache mechanism to handle files to prevent storage space from continuously growing. If a file is not used for a period of time, it will be "recycled". The purpose of Pinning is to ensure that files are not "recycled" locally.

```sh
# Pin a file
ipfs pin add [File Hash]

# Query whether a Hash is pinned
ipfs pin ls [File Hash]

# Remove pin status
ipfs pin rm -r [File Hash]

# GC operation
ipfs repo gc
```

## Conclusion

This article mainly deployed the IPFS file system locally and attempted basic operations, based on `macOS 11.2.3` and `go-ipfs_v0.8.0_darwin-amd64` version. Operations on different systems may vary due to version or dependency issues. If there are any errors or omissions, please feel free to communicate and correct.

## References

> 1. [IPFS Official Website](https://ipfs.io)