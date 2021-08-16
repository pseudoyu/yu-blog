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

最近接到了一个工作任务，将项目智能合约状态树中的数据结构从红黑树改为字典树，并对比一下两个数据结构的性能，Trie 主要参照的是 Ethereum 官方的 Java 实现 [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)，而红黑树则是自己实现，本文则是对两个数据结构的理论和实际表现对比的记录。

## 数据结构

### Red-Black Tree - 红黑树

### Trie - 字典树

### MPT - Merkle Patricia Tries

## 总结

以上就是对`Ethereum MPT` 与红黑树数据结构的解析，在刷 LeetCode 痛苦的时候想过很多次这些学了也用不到，没想到那么快就有了应用场景，还是要好好理解和实践呀！

## 参考资料

> 1. [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)
> 2. [以太坊源码分析 -- MPT 树](https://segmentfault.com/a/1190000016050921)