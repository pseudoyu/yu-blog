---
title: "LeetCode #104 二叉树的最大深度"
date: 2021-07-14T14:00:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：

给定二叉树 [3,9,20,null,null,15,7]

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。

## 题解

### 分治法

这类二叉树的题目比较模板化，主要就是采用递归，通过分治法遍历二叉树，然后合并结果，可以记住这样的模板化写法，很多二叉树遍历的题都很类似

```go
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    left := maxDepth(root.Left)
    right := maxDepth(root.Right)

    return max(left, right) + 1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)，*GitHub*