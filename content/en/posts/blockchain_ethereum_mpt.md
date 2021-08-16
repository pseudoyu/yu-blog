---
title: "Ethereum MPT(Merkle Patricia Tries) 解析"
date: 2021-08-16T12:12:17+08:00
draft: true 
tags: ["develop", "blockchain", "ethereum"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

最近接到了一个工作任务，将项目智能合约状态树中的数据结构从红黑树改为字典树，并对比一下两个数据结构的性能，Trie 主要参照的是 Ethereum 官方的 Java 实现[ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)，

## 总结

以上就是对`Ethereum MPT` 的解析。

## 参考资料

> 1. [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)
> 2. [以太坊源码分析 -- MPT 树](https://segmentfault.com/a/1190000016050921)