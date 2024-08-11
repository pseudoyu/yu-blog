---
title: "Cosmos Blockchain Architecture and Tendermint Consensus Mechanism"
date: 2023-02-10T20:00:03+08:00
draft: false
tags: ["blockchain", "crosschain", "cosmos", "tendermint", "consensus"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

![cosmos_introduction_and_explaination_photo](https://image.pseudoyu.com/images/cosmos_introduction_and_explaination_photo.png)

In my work, I am primarily involved in the architectural design and implementation of cross-chain projects. As our company's existing solution is based on the Cosmos blockchain, I have spent over a year working on some underlying chain development modifications using the Cosmos SDK. This has given me some understanding of its technical implementation. However, due to the tight development schedule, I never had the opportunity to gain a systematic understanding of Cosmos' architectural design and the Tendermint consensus mechanism.

After the project concluded, I finally found time to read "Blockchain Architecture and Implementation: Cosmos Explained". This article represents my own understanding and summary of Cosmos and Tendermint.

## Blockchain Technology Development

Before delving into the specifics of the Cosmos blockchain, let's first review the history of blockchain development and the current mainstream blockchain technologies in the industry.

### Technical Limitations

The blockchain has been developing for over a decade now, from the initial Bitcoin to the once-popular EOS, and then to Ethereum, which has gradually become mainstream. Each has its own characteristics but also its limitations.

- Building on Bitcoin or Ethereum requires relatively high technical expertise due to the need to implement p2p networks, cryptography, consensus algorithms, etc.
- Underlying chains based on the PoW (Proof of Work) mechanism are increasingly consuming more computing power (and electricity), which is not friendly to resources and the environment.
- As the number and scale of on-chain applications continue to increase, the performance bottlenecks of chains are becoming more apparent.
- As business scenarios become more complex and demands increase, the consensus algorithms of chains also need to evolve according to specific scenarios.
- The underlying architectures of different chains vary greatly, and different chains are isolated, making it difficult to communicate with each other. The implementation of cross-chain technology solutions is also a challenge.

### Technological Advancements

To address these issues, the industry has developed numerous technical solutions.

- Due to the massive resource consumption of PoW, many chains have adopted the PoS (Proof of Stake) mechanism, such as EOS's DPoS and Ethereum's recently upgraded PoS, which are becoming increasingly mature.
- To overcome the limitations of underlying chains, the model has gradually evolved from building separate chains for single applications (like Bitcoin) to building ÐApps using smart contracts.
- To address performance limitations, Bitcoin Cash adopted a solution to increase block capacity, EOS adopted a solution to improve TPS (claiming millions of TPS), while Ethereum uses sharding to process on-chain transactions in parallel.
- In terms of cross-chain technology, hash locking has been applied in Bitcoin and Algorand projects. Besides this, there are also solutions like notaries and relay chains.

## Cosmos Blockchain Framework

### Overview

Cosmos is an open-source blockchain infrastructure project developed by Tendermint Inc. Its goal is to solve various problems encountered in the development of blockchain technology, providing a high-performance, highly scalable, and easy-to-develop blockchain framework. Its open-source address is as follows:

- [GitHub - cosmos/cosmos: Internet of Blockchains](https://github.com/cosmos/cosmos)

Cosmos can be seen as a multi-chain network, aiming to realize the vision of an "Internet of Blockchains", with Tendermint and Cosmos SDK being its technical means and implementation path.

To address resource consumption and transaction issues, Cosmos adopted a BFT (Byzantine Fault Tolerance) + PoS (Proof of Stake) approach. Meanwhile, to lower the threshold for blockchain construction and blockchain-based application development, Cosmos adopted a more general project construction method, making chain development based on Cosmos more modular and engineered. It mainly consists of three parts: Tendermint Core, IBC, and Cosmos SDK.

### Cosmos SDK Components

Although named "SDK", which can easily lead to some misunderstandings that it's merely a library/component for interacting with the chain, Cosmos SDK can actually be considered a complete architecture. Developers can use it to quickly build their own blockchain, making it an important part of the Cosmos ecosystem. Its open-source address is as follows:

- [GitHub - cosmos/cosmos-sdk: A Framework for Building High Value Public Blockchains](https://github.com/cosmos/cosmos-sdk)

Cosmos SDK mainly implements some common modules in blockchain, such as account systems, transactions, on-chain governance, etc. Developers can conveniently build new functional modules based on it.

Its main modules are as follows:

- Account and transaction-related modules
  - auth: System account management
  - bank: On-chain asset transfer
- Auxiliary function modules
  - genutil: Genesis block
  - supply: Total asset management
  - crisis: Invariant management for all modules
  - params: Parameter management for all modules
- On-chain governance module
  - gov: On-chain governance mechanism
  - upgrade: Chain upgrade
- PoS modules
  - staking: On-chain asset staking
  - slashing: Punishing validators for passive malicious behavior
  - evidence: Punishing validators for active malicious behavior
  - mint: On-chain asset minting
  - distribution: Block reward management
  - IBC protocol module
  - ibc/core: Cross-chain communication functionality

As we can see, the Cosmos SDK framework is highly modularized due to the Object-Capability Model security philosophy. Each module has its own storage space and only exposes necessary interfaces externally.

There is a specific Keeper role in Cosmos SDK, used to maintain and update states. Through this management method, modules hide specific implementation details from each other and only call each other through keepers. Moreover, each module's internal state is only updated by its keeper, effectively ensuring the consistency of on-chain states.

### Tendermint Component

Tendermint is the core component of Cosmos, a high-performance blockchain underlying consensus engine. Architecturally, it is mainly divided into three parts: peer-to-peer network communication layer, consensus protocol layer, and upper application layer, with the consensus protocol layer being its key part.

When reaching consensus, Tendermint does not care about the specific transaction details, but only packages transactions as bytes into blocks, and then reaches consensus through mechanisms between nodes. It requires the upper application state update to be a deterministic process, that is, starting from the same initial state, the transaction order is consistent across the network (i.e., all normal nodes will process a sequence of messages in the same order), and the state of the upper application should remain consistent across the network. The blockchain will include digital fingerprints of the upper application for verification.

Tendermint consensus can support second-level block production in blockchain networks with hundreds of nodes. It provides the feature of block-by-block finality, meaning that after a block is confirmed, it can guarantee that all previous blocks will not be modified, ensuring the security of the blockchain network.

After a block is submitted, the Tendermint consensus protocol layer interacts with the upper layer through ABCI (an interface abstracted for interaction between the application layer and the consensus layer) to complete transaction processing and return results. It divides the block execution process into multiple steps, and the upper application has the autonomy to define business interaction logic, developing and implementing through specific interfaces (such as implementing validator screening logic or reusing Tendermint Core's consensus protocol and peer-to-peer network communication to implement chain business requirements).

For a detailed understanding of the Tendermint consensus algorithm mechanism, you can read the following paper:

- [The latest gossip on BFT consensus - Tendermint](https://arxiv.org/pdf/1807.04938.pdf)

Its unique mechanisms bring significant advantages in the blockchain consensus process.

Firstly, Tendermint originates from the PBFT SMR (State Machine Replication) algorithm but simplifies its mechanism. Its consensus is mainly based on blocks rather than user requests, and mechanically unifies PBFT's regular process and view-change process, making it easier to understand and implement.

It provides solid infrastructure and good user experience, being one of the earliest underlying technologies capable of supporting second-level block production in blockchain networks with hundreds of nodes. At the same time, it ensures that all previous blocks will not be modified through block-by-block finality, guaranteeing the security of the blockchain network.

Nodes communicate with each other through the Gossip protocol, not requiring full connectivity between nodes, but communicating through a gossip peer-to-peer network. This can effectively reduce the communication cost between nodes while also effectively improving the fault tolerance of the network.

The implementation details and mechanisms of the Tendermint algorithm will be explained specifically in later series of articles.

### IBC Protocol Component

The IBC protocol is a special module in Cosmos SDK, mainly providing cross-chain capabilities between blockchains for Cosmos. Its main principle is to prove its own on-chain events to other chains through cryptographic technology. It can be understood that the cross-chain parties are light nodes (light clients) for each other, and the communication between the two chains is realized through relayers, thus achieving cross-chain communication/transactions.

This part involves many details and is closely related to cross-chain, so it will be explained in detail in a separate article.

## Conclusion

This article is the first in the Cosmos and Tendermint consensus series, mainly introducing the technological development of blockchain, core components such as Tendermint and Cosmos SDK in the Cosmos blockchain framework, and providing an overview of the principles and mechanisms of the Tendermint consensus protocol. Due to space limitations, it mainly focuses on concept explanation and process overview, without involving specific technical implementation details and code explanation. These will be supplemented in subsequent series of articles on the Tendermint consensus algorithm/mechanism and Cosmos SDK code implementation.

## References

1. > "Blockchain Architecture and Implementation: Cosmos Explained - Wen Long/Jia Yin"
2. > [Cosmos: The Internet of Blockchains](https://cosmos.network/)
3. > [Whitepaper - Resources - Cosmos Network](https://v1.cosmos.network/resources/whitepaper)
4. > [Distributed Systems and Blockchain Consensus Mechanisms · Pseudoyu](https://www.pseudoyu.com/en/2021/09/08/blockchain_consensus/)
5. > [Exploring Cosmos: Tendermint](https://tech.hyperchain.cn/cosmos-5/)
6. > [Exploring Cosmos: Cosmos SDK](https://tech.hyperchain.cn/cosmos-4/)