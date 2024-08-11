---
title: "Introduction and Architecture of Blockchain as a Service (BaaS) Platforms"
date: 2021-09-07T10:00:52+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "baas"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

In my current work, I am responsible for the chaincode management portion of a Blockchain as a Service (BaaS) platform for Hyperledger Fabric. I'm quite interested in the architecture and implementation of BaaS platforms. As a platform that provides developers with one-stop creation, management, and maintenance of blockchain applications, what does its architecture look like?

This article is a summary and analysis of the BaaS platform architecture.

## Introduction to BaaS

Blockchain is a complex distributed system, especially enterprise consortium chain platforms like Hyperledger Fabric, where deployment and operation are extremely intricate. As application developers, we need to handle many environmental issues (such as certificates, Docker environments, etc.), which brings numerous challenges.

Therefore, BaaS platforms have emerged. They are application platforms that help users create, manage, and maintain enterprise-level blockchains. Users can operate the blockchain through a user-friendly web interface. Through BaaS platforms, users can flexibly build blockchain networks, manage blockchain business and various module functions, develop and deploy smart contracts, and perform real-time monitoring and operation.

With BaaS platforms, developers can quickly conduct blockchain business development, greatly reducing overall costs, and helping to improve system stability, security, and usability.

![baas_framework](https://image.pseudoyu.com/images/baas_framework.png)

## Platform Architecture

As a one-stop application service, a BaaS platform is primarily divided into the following layers from bottom to top:

1. Resource Layer
2. Monitoring and Operations Layer
3. Blockchain Underlying Layer
4. Blockchain Service Layer
5. Application Layer

Depending on the business differences of each system, the architecture and functional modules of each layer will vary. Below, I will describe the hierarchical structures of several mainstream platforms.

### Hyperledger Cello

![hyperledger_cello_overview](https://image.pseudoyu.com/images/hyperledger_cello_overview.png)

[Hyperledger Cello](https://github.com/hyperledger/cello), as one of IBM Hyperledger's top-level projects, is an open-source blockchain management platform that supports deployment, runtime management, and data analysis functions.

Cello currently supports Hyperledger Fabric blockchain and can effectively manage the lifecycle of Fabric chains. It mainly includes the following modules:

![hyperledger_cello_architecture](https://image.pseudoyu.com/images/hyperledger_cello_architecture.png)

In addition to efficiently creating and deploying networks, Cello provides some management functions for blockchains:

- Blockchain lifecycle management
- Support for multiple underlying architectures such as Docker, Swarm, Kubernetes, etc.
- Support for multiple underlying blockchain platforms with customizable configurations
- Runtime monitoring and operations support
- Pluggable framework design, allowing extension of third-party functions through plugins, such as resource scheduling, driver agents, etc.

### Hyperchain BaaS

According to the official website, BlocFace is a blockchain service platform newly launched by Hyperchain Technology for enterprises and developers. It provides users with one-click deployment of consortium chains, visual monitoring and operations, and smart contract development, among other one-stop development services. Its platform architecture is as follows:

![hyperchain_baas](https://image.pseudoyu.com/images/hyperchain_baas.png)

## Conclusion

The above is an introduction and architectural analysis of Blockchain as a Service (BaaS) platforms. As my current leader is the project initiator and core developer of Hyperledger Cello, I am encouraged to actively participate in Cello's open-source development. Time to work hard!

## References

> 1. [Blockchain: Principles, Design and Applications](https://book.douban.com/subject/27127839/)
> 2. [Hyperledger Cello Project Repository](https://github.com/hyperledger/cello)
> 3. [BlocFace Official Website](https://www.hyperchain.cn/products/blocface)