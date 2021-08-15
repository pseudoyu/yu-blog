---
title: "LeetCode #124 二叉树中的最大路径和"
date: 2021-07-14T17:40:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：

![leetcode_124_1](https://cdn.jsdelivr.net/gh/pseudoyu/image_hosting@master/hugo_images/leetcode_124_1.jpg)

	输入：root = [1,2,3]
	输出：6
	解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：

![leetcode_124_2](https://cdn.jsdelivr.net/gh/pseudoyu/image_hosting@master/hugo_images/leetcode_124_2.jpg)

	输入：root = [-10,9,20,null,null,15,7]
	输出：42
	解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


## 题解

这道题虽然是困难，但是远离上可以说是二叉树最大高度的引申，只是在返回的时候需要加上的是节点的值而不仅仅是高度。其中有几个需要特殊处理的细节，首先就是在递归左右节点的时候，因为要求的是最大值，所以为负数时则不取，用max(0, ...)进行处理；此外就是需要一个sum全局变量来存储最后的值，这里踩了一个坑，可能是leetcode对于全局变量多个case的复用，在全局声明后直接赋值会出问题，最后在maxPathSum进行初始化后才得以解决，记录一下。

```go
var sum int

func maxPathSum(root *TreeNode) int {
	sum = math.MinInt32
    maxGain(root)
    return sum
}

func maxGain(root *TreeNode) int {
    if root == nil {
        return 0
    }

    left := max(maxGain(root.Left), 0)
    right := max(maxGain(root.Right), 0)

    totalPath := left + right + root.Val
    sum = max(sum, totalPath)

    return max(left, right) + root.Val
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)，*GitHub*