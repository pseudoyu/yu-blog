---
title: "LeetCode #236 二叉树的最近公共祖先"
date: 2021-07-14T18:20:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：

![leetcode_236](https://raw.githubusercontent.com/pseudoyu/image_hosting/master/hugo_images/leetcode_236.png)

    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：

![leetcode_236](https://raw.githubusercontent.com/pseudoyu/image_hosting/master/hugo_images/leetcode_236.png)

    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出：5
    解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：

    输入：root = [1,2], p = 1, q = 2
    输出：1

## 题解

这道题最主要的就是搞清楚最近公共祖先这个概念，在几种情况下两个节点的最近公共祖先为root

1. p和root相等
2. q和root相等
3. p、q在不同的子树

```go
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
     if root == nil {
         return root
     }

     if p == root || q == root {
         return root
     }

     left := lowestCommonAncestor(root.Left, p, q) 
     right := lowestCommonAncestor(root.Right, p, q)

     if left != nil && right != nil {
         return root
     }

     if left != nil {
         return left
     }

     if right != nil {
         return right
     }
     return nil
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)，*GitHub*