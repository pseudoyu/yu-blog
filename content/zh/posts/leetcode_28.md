---
title: "LeetCode #28 实现 strStr()"
date: 2021-07-13T22:30:17+08:00
draft: false
tags: ["leetcode", "algorithm", "go"]
categories: ["LeetCode"]
authors:
- "Arthur"
---

## 题目描述

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：

    输入：haystack = "hello", needle = "ll"
    输出：2

示例 2：

    输入：haystack = "aaaaa", needle = "bba"
    输出：-1

示例 3：

    输入：haystack = "", needle = ""
    输出：0

## 题解


### 两层遍历

通过两层遍历来确定字符串是否与目标字符串一致（通过比较长度），技巧是在第一层遍历的时候不用遍历整个字符串，只需要遍历原有字符串减去目标字符串的长度，实现效率不高

```go
func strStr(haystack string, needle string) int {
    var i, j int
    for i = 0; i < len(haystack) - len(needle) + 1; i++ {
        for j = 0; j < len(needle); j++ {
            if haystack[i + j] != needle[j] {
                break
            }
        }
        if len(needle) == j {
            return i
        }
    }
    return -1
}
```

## 参考资料

> 1. [LeetCode题目链接](https://leetcode-cn.com/problems/implement-strstr)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)，*GitHub*