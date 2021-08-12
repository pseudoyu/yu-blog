---
title: "LeetCode #1 两数之和"
date: 2021-07-13T17:50:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：

    输入：nums = [3,2,4], target = 6
    输出：[1,2]

示例 3：

    输入：nums = [3,3], target = 6
    输出：[0,1]

## 题解

### 暴力解法

首先能想到的就是暴力解法，也就是两层循环嵌套遍历所有的i，j，用一个int切片存储返回结果，如果找到相等的则返回两个索引值，如没找到则返回初始化值0

```go
func twoSum(nums []int, target int) []int {
    ans := make([]int, 0)
    for i := 0; i < len(nums) - 1; i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                ans = []int{i, j}
            }
        }
    }
    return ans
}
```

### map结构

暴力解法虽然容易想到，但是两层循环的时间复杂度很高，因此，可以采取以空间换时间的方式来进行优化，以map结构来找键值对复杂度为O(1)，哈希

```go
func twoSum(nums []int, target int) []int {
    ans := make([]int, 0)
    numsMap := make(map[int]int, 0)

    for i := 0; i < len(nums); i++ {
        if j, ok := numsMap[target - nums[i]]; ok {
            ans = []int {i, j}
        }
        numsMap[nums[i]] = i
    }
    return ans
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/two-sum/)