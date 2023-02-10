---
title: "Cosmos 区块链架构与 Tendermint 共识机制"
date: 2023-02-10T20:00:03+08:00
draft: false
tags: ["blockchain", "crosschain", "cosmos", "tendermint", "consensus"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## 前言

![cosmos_introduction_and_explaination_photo](https://image.pseudoyu.com/images/cosmos_introduction_and_explaination_photo.png)

工作中我主要参与的是跨链项目的方案架构设计与实现，因为公司既有方案是基于 Cosmos 区块链的，我在一年多的项目中基于 Cosmos SDK 作了一些底层链开发改造，对其技术实现有了一些了解，但由于开发周期比较赶，一直没能对 Cosmos 的架构设计与 Tendermint 共识机制有一个系统的了解。

项目结束后，终于得闲读了一下《区块链架构与实现：Cosmos 详解》，本文则是我自己对 Cosmos、Tendermint 的理解和总结。

## 区块链技术发展

在讲具体的 Cosmos 区块链之前，我们先梳理一下区块链发展的历程，以及目前业界主流的区块链技术。

### 技术限制

区块链发展至今已经有十几年的历程，从最开始的比特币，到红极一时的 EOS，再到后来渐渐成为主流的以太坊，各有特色却也都有其限制之处。

- 基于比特币或以太坊的方式由于需要实现 p2p 网络、密码学、共识算法等，需要相对比较高的技术门槛；
- 基于 PoW（工作量证明）机制的底层链对于算力（电力）消耗也越来越大，对于资源与环境并不友好；
- 随着链上应用数量与规模的不断增加，链的性能瓶颈越来越明显；
- 随着业务场景复杂度提升与需求不断增加，链的共识算法也需要根据具体场景而变化；
- 不同链的底层架构差异较大，不同链之间也是孤岛，难以互相通信，跨链技术方案落地也是一个难题。

### 技术发展

为了解决上述问题，业界也有不少的技术方案。

- 由于 PoW 对于资源的大量消耗，许多链采用了 PoS（权益证明）机制，如 EOS 的 DPoS 与以太坊刚升级不久的 PoS，发展也日益成熟；
- 为了解决底层链限制问题，从类似比特币这样为单个应用构建单独链的模式也渐渐发展到了利用智能合约构建 ÐApp；
- 对于性能限制问题，比特现金采用了增加区块容量的方案，EOS 采用提升 TPS 的方案（号称百万 TPS），而以太坊则通过分片（Sharding）的方式对链上交易进行并行处理；
- 跨链技术方面，哈希锁定（散列锁）的方式在比特币与 Algorand 项目中有应用，除此之外还有公证人、中继链等方案。

## Cosmos 区块链框架

### 概述

Cosmos 是一个由 Tendermint 公司开发构建的开源区块链底层框架项目，其目标是为了解决区块链技术发展过程中遇到的各类问题，提供一个高性能、高可扩展、易于开发的区块链框架，其开源地址如下：

- [GitHub - cosmos/cosmos: Internet of Blockchains](https://github.com/cosmos/cosmos)

Cosmos 可以看作一种多链网络，旨在实现“互链网”远景，而 Tendermint 和 Cosmos SDK 则是其技术手段与实现路径。

对于资源消耗与交易问题，Cosmos 采用了 BFT（拜占庭容错） + PoS（权益证明）的方式来解决；同时，为了降低区块链搭建与基于区块链的应用开发门槛，Cosmos 采用了较为通用的项目构建方式，使基于 Cosmos 进行链开发更加模块化与工程化，其主要由 Tendermint Core、IBC、Cosmos SDK 三部分组成。

### Cosmos SDK 组件

虽然名称叫作“SDK”，容易引起一些误解，认为其仅仅是与链交互的一个库/组件，但其实 Cosmos SDK 可以说是一个完整的架构，开发者可以通过其来快速搭建自己的区块链，是 Cosmos 生态体系中的重要组成部分的。其开源地址如下：

- [GitHub - cosmos/cosmos-sdk: A Framework for Building High Value Public Blockchains](https://github.com/cosmos/cosmos-sdk)

Cosmos SDK 主要实现了区块链中的一些通用模块，如账户体系、交易、链上治理等，开发者又可以便捷地基于其快速构建新的功能模块。

其主要模块如下：

- 账户与交易相关模块
  - auth：系统账户管理
  - bank：链上资产转移
- 辅助功能模块
  - genutil：创世区块
  - supply：资产总量管理
  - crisis：所有模块不变量管理
  - params：所有模块的参数管理
- 链上治理模块
  - gov：链上治理机制
  - upgrade：链升级
- PoS 模块
  - staking：链上资产抵押
  - slashing：对验证者的被动作恶进行惩罚
  - evidence：对验证者的主动作恶进行惩罚
  - mint：链上资产铸造
  - distribution：区块奖励管理
  - IBC 协议模块
  - ibc/core：跨链通信功能

可以看到，Cosmos SDK 框架设计出于 Object-Capability Model 安全理念的考量，设计高度模块化，每个模块都有自己的存储空间且对外仅暴露必要接口。

Cosmos SDK 中有一个特定的 Keeper 角色，用于维护更新状态。通过这种管理方式，模块之间彼此隐藏了具体实现细节，而仅仅通过 keeper 来互相调用，且每个模块内部也都只会被 keeper 进行更新，有效保障了链上状态的一致性。

### Tendermint 组件

Tendermint 是 Cosmos 的核心组件，是一个高性能的区块链底层共识引擎，从架构上来说，其主要分为对等网络通讯层、共识协议层与上层应用层三大部分，其中共识协议层是其关键部分。

Tendermint 在共识时并不关心具体交易细节，而只是将交易当作字节打包成区块，然后通过各节点之间的的机制达成共识。其要求上层应用状态更新为确定性过程，即从相同初始状态开始，在全网环境下交易顺序达成一致（即对于一个序列的消息所有的正常节点都会以相同的顺序进行处理），上层应用的状态在全网之间也应保持一致，区块链会包含上层应用的数字指纹来进行验证。

Tendermint 共识可以支持在上百个节点规模的区块链网络中实现秒级出块，其提供了逐块最终化（Finality）的特性，即一个块确认后可以保障其之前的所有块都不会被修改，保障了区块链网络安全性。

区块提交后，Tendermint 共识协议层通过 ABCI（应用层与共识层交互所抽象出来的接口）与上层进行互动，完成交易处理并返回结果。其将区块执行过程划分为多个步骤，上层应用拥有自主权来定义业务交互逻辑，通过特定接口进行开发与实现（如可以实现筛选验证者逻辑或复用 Tendermint Core 的共识协议与对等网络通信来实现链业务需求）。

关于 Tendermint 共识算法具体机制可以阅读以下论文进行了解：

- [The latest gossip on BFT consensus - Tendermint](https://arxiv.org/pdf/1807.04938.pdf)

其特有的一些机制带来了区块链共识过程中的显著优势。

首先，Tendermint 源于 PBFT SMR（State Machine Replication）算法，但对其机制进行了简化，其共识主要基于区块而不是用户请求，并且在机制上将 PBFT 常规流程与视图切换流程进行了统一，使其更容易理解与实现。

它提供了坚实的基础设施与良好的用户体验，是较早能够支持在上百个节点规模的区块链网络中支持秒级出块的底层，同时也通过逐块最终化（Finality）的方式确保之前的所有块都不会被修改，保障区块链网络安全性。

其节点之间通过 Gossip 协议进行通讯交互，不要求节点之间的全连接，而是通过 gossip 对等网络进行通信，这样可以有效降低节点之间的通讯成本，同时也可以有效提高网络的容错性。

Tendermint 算法实现细节与机制将在之后的系列文章中具体讲解。

### IBC 协议组件

IBC 协议属于 Cosmos SDK 中一个特殊的模块，其主要为 Cosmos 提供了区块链之间的跨链能力，其主要原理是通过密码学技术来向其他链证明自己的链上事件，可以理解为跨链双方彼此为对方的一个轻节点（轻客户端），而两条链的通讯则是通过 relayer 实现，从而实现跨链通讯/交易。

这一部分细节较多，且与跨链较为相关，会单独出文章进行详细讲解。

## 总结

本文为 Cosmos 及 Tendermint 共识系列第一篇，主要介绍了区块链的技术发展、Cosmos 区块链框架中的 Tendermint 和 Cosmos SDK 等核心组件，并对 Tendermint 共识协议的原理和各机制进行了一些概述。受限于篇幅，主要以概念讲解与流程梳理为主，未涉及具体的技术实现细节与代码讲解，将会在后续的系列文章中对 Tendermint 共识算法/机制及 Cosmos SDK 代码实现进行补充。

## 参考资料

1. > 《[区块链架构与实现：Cosmos 详解 - 温隆/贾音](https://book.douban.com/subject/35571980/)》
2. > [Cosmos: The Internet of Blockchains](https://cosmos.network/)
3. > [Whitepaper - Resources - Cosmos Network](https://v1.cosmos.network/resources/whitepaper)
4. > [分布式系统与区块链共识机制 · Pseudoyu](https://www.pseudoyu.com/en/2021/09/08/blockchain_consensus/)
5. > [走进 Cosmos 之 Tendermint](https://tech.hyperchain.cn/cosmos-5/)
6. > [走进 Cosmos 之 Cosmos SDK](https://tech.hyperchain.cn/cosmos-4/)
