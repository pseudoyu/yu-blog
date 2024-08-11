---
title: "Cross-Chain Technology Principles and Practice"
date: 2021-09-06T15:34:40+08:00
draft: false
tags: ["blockchain", "crosschain"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Currently, blockchain platforms are becoming increasingly diverse, including established ones like Hyperledger Fabric and Ethereum, as well as domestic platforms such as Hyperchain and Z-ledger. As blockchain application ecosystems grow more complex, single-chain performance faces certain bottlenecks. Consequently, collaboration and interaction between chains (information synchronization, sharing, contract interoperability, etc.) have become crucial aspects of chain and application ecosystem development.

This article provides an overview of cross-chain technology concepts and mainstream solutions.

## Cross-Chain Technology Overview

Due to similarities in underlying chain design, consensus algorithms, and network structures, interaction between homogeneous blockchains is relatively straightforward. However, interaction between heterogeneous blockchains is more complex, often requiring auxiliary platforms or services for data format conversion between the two chains.

### Cross-Chain Mechanisms

Currently, there are several main solutions for cross-chain interactions:

1. Notary mechanism
2. Hash-locking
3. Distributed private key control
4. Sidechains/Relay chains

#### Notary Mechanism

The notary mechanism is a method that facilitates interaction between different chains through a third-party intermediary. Essentially, both parties trust a third party to verify and forward cross-chain data or interaction operations. This approach effectively supports heterogeneous blockchains but is centralized in nature.

Many digital currency exchanges use this method to conduct transactions and conversions between different digital currencies. Fundamentally, the exchange matches trades, offering high efficiency but posing certain security risks and only supporting asset exchange.

#### Hash-locking

Hash-locking first appeared in Bitcoin's Lightning Network. It uses hash locks and time locks to secure assets for both parties in a cross-chain transaction. Time locks restrict transactions to a specific timeframe, with the transaction becoming invalid if it exceeds the time limit, thus preventing losses. However, this method can only facilitate asset exchange, not asset transfer.

#### Sidechains

Sidechain technology involves two-way pegging, initially developed in relation to the Bitcoin main chain, such as BTC-Relay. These sidechains allow for new feature development and testing for Bitcoin, and can effectively expand network throughput when many users are transacting on the Bitcoin network. For example, asset transactions and value transfers can occur on the Ethereum main chain, while DApps requiring higher TPS can run on Ethereum sidechains.

Different sidechains of the same main chain can also interact through the main chain, which forms the basic principle of cross-chain interaction via sidechains.

#### Relay Chains

Relay chains represent a comprehensive application of the aforementioned sidechain and notary mechanisms. They achieve information sharing and interaction between heterogeneous chains by establishing cross-chain interaction mechanisms (such as Cosmos' IBC). Parallel chains requiring cross-chain functionality connect to a relay chain to assist with transaction verification and interaction.

## Cross-Chain Technology in Practice

### Development Implementation

I am currently working on a cross-chain functionality for a BaaS platform. Its basic architecture is as follows:

![cross_chain_framework](https://image.pseudoyu.com/images/cross_chain_framework.png)

Sub-chains primarily implement various businesses and applications. When a sub-chain needs to interact with other chains for cross-chain business, it executes a cross-chain contract. We provide a cross-chain gateway to monitor these cross-chain contracts. For heterogeneous blockchains like Hyperledger Fabric and Ethereum, we offer different adapters to facilitate interaction between the cross-chain SDK and the cross-chain gateway. These adapters provide cross-chain contract information query functionality. When the SDK of another business chain receives a cross-chain contract method, it directly calls the corresponding contract method if it involves contract inter-calling or data transfer.

My main focus is on the cross-chain adapter interface. The adapter, serving as a plugin for different chains, is embedded in the cross-chain gateway to adapt to various application chains, effectively assisting the cross-chain gateway in monitoring, synchronizing, and executing transactions.

In specific implementations, such as in a Fabric network, the sub-chain calls the cross-chain business contract, which in turn uniformly calls an adapter contract. Within this adapter contract, we implement transaction information input. Through Fabric's event mechanism, we achieve monitoring of cross-chain contracts (i.e., implementing the `SetEvent` method in the contract and registering corresponding events in the adapter).

For details on Fabric event monitoring and implementation, refer to "[Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/en/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)".

### Functional Extension

Currently, QulianTech's [BitXHub Cross-Chain Platform](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/) is one of the industry's more comprehensively implemented open-source cross-chain solutions. Its architecture is as follows:

![bitxhub_structure](https://image.pseudoyu.com/images/bitxhub_structure.png)

It primarily optimizes functionality, security, and flexibility in the cross-chain process through relay chains, gateways, and plugin mechanisms. It also designed the IBTP (Inter-Blockchain Transfer Protocol) to work with the "gateway + relay chain" architecture to address verification, routing, and other issues in cross-chain transactions.

## Conclusion

The above summarizes the concepts and practical implementation of cross-chain technology. To gain a deeper understanding of various aspects of cross-chain mechanisms, I will conduct more in-depth analysis and source code interpretation of the cross-chain service I am currently working on and the BitXHub platform in the future.

## References

> 1. [Analysis and Thoughts on Cross-Chain Technology](https://tech.hyperchain.cn/blockchain-interoperability/)
> 2. [A Brief Study of Cross-Chain: From Principles to Technology](https://zhuanlan.zhihu.com/p/92667917)
> 3. [Cross-Chain Technology Platform BitXHub](https://github.com/gocn/opentalk/tree/main/PhaseTen_BitXHub)
> 4. [Blockchain Cross-Chain Technology: Hash Time Locks](https://yuanxuxu.com/2020/08/05/区块链跨链技术之哈希时间锁/)
> 5. [Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/en/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)
> 6. [BitXHub Document](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/)
> 7. [Ten Questions about BitXHub: Discussing the Architectural Design of Cross-Chain Platforms](https://tech.hyperchain.cn/bitxhub-design-thinking/)