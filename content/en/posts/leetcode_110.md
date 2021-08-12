---
title: "LeetCode #110 平衡二叉树"
date: 2021-07-14T14:40:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：

    输入：root = [3,9,20,null,null,15,7]
    输出：true

示例 2：

    输入：root = [1,2,2,3,3,null,null,4,4]
    输出：false

示例 3：

    输入：root = []
    输出：true

## 题解

跟二叉树的最大高度一样，只是需要判断左右节点之间差值是否不超过1，按照模板写比较容易

```go
func isBalanced(root *TreeNode) bool {
	if maxDepth(root) == -1 {
		return false
	}
	return true
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	left := maxDepth(root.Left)
	right := maxDepth(root.Right)

	if left == -1 || right == -1 || left - right > 1 || right - left > 1 {
		return -1
	}

	return max(left, right) + 1
}

func max(a, b int) int{
	if a > b {
		return a
	}
	return b
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/balanced-binary-tree)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)，*GitHub*