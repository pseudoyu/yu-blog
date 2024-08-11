---
title: "Detailed Explanation of Ethereum MPT (Merkle Patricia Tries)"
date: 2021-08-16T12:12:17+08:00
draft: false
tags: ["blockchain", "ethereum"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I received a work assignment to change the data structure of the project's smart contract state tree from a red-black tree to a trie, and to compare the performance of the two data structures. The Trie mainly refers to Ethereum's official Java implementation [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie), while the red-black tree is implemented by myself. This article is a record of the theoretical and practical comparison of the two data structures.

## Data Structures

### Red-Black Tree

A red-black tree is an approximately balanced binary search tree containing red and black nodes, ensuring that the height difference between the left and right subtrees of any node is less than twice.

![red_black_tree_2](https://image.pseudoyu.com/images/red_black_tree_2.png)

#### Properties

It must satisfy the following five properties:

1. Nodes are either red or black
2. The root node is black
3. Leaf nodes (NIL) are black
4. Both children of every red node are black
5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes

Red-black trees are not perfectly balanced, but the number of layers in the left and right subtrees is equal, thus also known as black perfect balance. Because it is approximately balanced, the frequency of rotations is reduced, maintenance costs decrease, and time complexity remains at LogN.

#### Operations

Red-black trees mainly maintain self-balance through three operations:

- Left rotation
- Right rotation
- Color change

#### Comparison with AVL Trees

- AVL trees provide faster lookup operations (due to perfect balance)
- Red-black trees provide faster insertion and deletion operations
- AVL trees store more node information (balance factor and height), thus occupying more storage space
- AVL trees are more suitable when read operations are frequent and write operations are few, often used in databases; red-black trees are generally used when write operations are more frequent, being concise and easy to implement, often used in libraries of various high-level languages, such as map, set, etc.

#### Code Implementation

As red-black trees are relatively complex, the implementation code has been uploaded to GitHub for learning and reference.

[pseudoyu/RedBlackTree-Java](https://github.com/pseudoyu/RedBlackTree-java)

### Trie - Dictionary Tree

Trie, also known as a dictionary tree, prefix tree, or key tree, is commonly used for statistics and sorting of large amounts of strings, such as text disk statistics in search engines.

It can minimize unnecessary string comparisons, resulting in high query efficiency.

![trie_structure](https://image.pseudoyu.com/images/trie_structure.png)

#### Properties

1. Nodes do not store complete words
2. The string corresponding to a node is formed by connecting the characters passed through on the path from the root node to that node
3. The path characters represented by all child nodes of each node are different
4. Nodes can store additional information, such as word frequency

#### Internal Node Implementation

![trie_nodes](https://image.pseudoyu.com/images/trie_nodes.png)

The height of a trie is relatively low, but it occupies more storage space. The core idea is to trade space for time.

It uses the common prefixes of strings to reduce the cost of query time to achieve the purpose of improving efficiency, which can naturally solve business scenarios such as word association.

#### Code Implementation

```java
class Trie {
    private Trie[] children;
    private boolean isEnd;

    public Trie() {
        children = new Trie[26];
        isEnd = false;
    }

    public void insert(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            if (node.children[index] == null) {
                node.children[index] = new Trie();
            }
            node = node.children[index];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private Trie searchPrefix(String prefix) {
        Trie node = this;
        for (int i = 0; i < prefix.length(); i++) {
            char ch = prefix.charAt(i);
            int index = ch - 'a';
            if (node.children[index] == null) {
                return null;
            }
            node = node.children[index];
        }
        return node;
    }
}
```

### Modified Merkle Patricia Tries

#### Ethereum Account State Storage Method

1. Using a Key-Value hash table for storage is costly, as new transactions are packaged into blocks each time a block is produced, changing the Merkle tree, but in fact, only a small number of accounts change.
2. Directly using a Merkle tree to store accounts is not feasible, as it does not provide an efficient method for searching and updating.
3. Using a sorted Merkle tree is also not feasible, as new account addresses are randomly generated, requiring insertion and resorting.

#### MPT Structure

Utilizing the characteristics of the Trie structure:

1. The Trie structure remains unchanged after shuffling, naturally sorted, and unaffected even when inserting new values, suitable for Ethereum's account-based structure.
2. It has good update locality, not requiring traversal of the entire tree when updating.

However, the Trie structure wastes storage space and is inefficient when key-value pairs are sparsely distributed. Ethereum account addresses are 40-digit hexadecimal numbers, with approximately 2^160 possible addresses, which are extremely sparse (to prevent hash collisions).

Therefore, the Trie structure needs to be compressed, which is the Patricia Trie. After compression, the height of the tree is significantly reduced, improving both space and efficiency.

![pactricia_trie](https://image.pseudoyu.com/images/pactricia_trie.png)

#### Modified MPT Structure

The structure actually adopted by Ethereum is the Modified MPT structure, as shown below:

![modified_merkle_pactricia_trie](https://image.pseudoyu.com/images/modified_merkle_pactricia_trie.png)

When a new block is published, the values of the new nodes in the state tree change. Instead of modifying the original value, new branches are created, preserving the original state (thus enabling rollback).

In the Ethereum system, forks are common, and data in orphan blocks needs to be rolled back. Due to the presence of smart contracts in ETH, to support the rollback of smart contracts, previous states must be maintained.

#### Code Implementation

The code refers to Ethereum's Java implementation.

[ethereum/ethereumj - GitHub](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)

## Conclusion

The above is an analysis of the `Ethereum MPT` and red-black tree data structures. When struggling with LeetCode, I often thought that learning these would be useless, but I didn't expect to have an application scenario so soon. We still need to understand and practice well!

## References

> 1. [30 images to help you thoroughly understand red-black trees](https://www.jianshu.com/p/e136ec79235c)
> 2. [LeetCode Implementation of Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/)
> 3. [pseudoyu/RedBlackTree-Java](https://github.com/pseudoyu/RedBlackTree-java)
> 4. [Ethereum Source Code Analysis -- MPT Tree](https://segmentfault.com/a/1190000016050921)
> 5. [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)