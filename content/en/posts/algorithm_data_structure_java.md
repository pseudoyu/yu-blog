---
title: "LeetCode 刷题常用数据结构（Java 篇）"
date: 2021-01-01T00:12:17+08:00
draft: false
tags: ["java","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

最近开始刷 LeetCode 算法题，针对工作需求的算法刷题其实主要是锻炼解决问题的思路和代码撰写能力，而不是像算法竞赛那样用复杂的数据结构，所以常用的数据结构和操作并不多，熟练使用也能很好地提升自己的代码质量，特此做一个整理，以便于查阅。

## 数据结构

### 数组 []

#### 初始化

```java
// 初始化一个大小为10，默认值为0的数组
int[] nums = new int[10];

// 初始化一个二位boolean数组
boolean[][] visited = new boolean[5][10];
```

#### 常用方法

```java
// 函数开头一般要做一个非空检查，然后用索引下标访问元素
if (nums.length == 0) {
    return;
}

for (int i = 0; i < nums.length; i++) {
    // 访问num[i]
}
```

### 字符串 String

#### 初始化

```java
String s1 = "hello world";
```

#### 访问字符串

```java
// String不支持用[]直接访问字符
char c = s1.charAt(2);
```

#### 修改字符串

```java
// String不支持直接修改字符串，要转化为char[]类型才能修改
char[] chars = s1.toCharArray();
chars[1] = 'a';
String s2 = new String(chars);
```

#### 判断字符串是否相同

```java
// 一定要用equals方法进行判断，不能直接用==
if (s1.equals(s2)) {
    // 相等
} else {
    // 不相等
}
```

#### 拼接字符串

```java
// 支持直接用+进行连接，但是效率不高
String s3 = s1 + "!";
```

#### 通过 StringBuilder 进行频繁的字符串拼接以提高效率

```java
StringBuilder sb = new StringBuilder();

for (char c = 'a'; c <= 'f'; c++) {
    // append方法支持拼接字符、字符串、数字等类型
    sb.append(c);
    String result = sb.toString();
}
```

### 动态数组 ArrayList

#### 初始化

```java
// 初始化一个存储String类型的动态数组
ArrayList<String> strings = new ArrayList<>();

// 初始化一个存储int类型的动态数组
ArrayList<Integer> nums = new ArrayList<>();
```

#### 常用方法

```java
// 判断是否为空
boolean isEmpty()

// 返回元素个数
int size()

// 访问索引元素
E get(int index)

// 在尾部添加元素
boolean add(E e)
```

### 双链表 LinkedList

#### 初始化

```java
// 初始化一个存储String类型的双链表
LinkedList<String> strings = new LinkedList<>();

// 初始化一个存储int类型的双链表
LinkedList<Integer> nums = new LinkedList<>();
```

#### 常用方法

```java
// 判断是否为空
boolean isEmpty()

// 返回元素个数
int size()

// 在尾部添加元素
boolean add(E e)

// 删除尾部最后一个元素
E removeLast()

// 在头部添加元素
void addFirst(E e)

// 删除头部第一个元素
E removeFirst()
```

### 哈希表 HashMap

#### 初始化

```java
// 初始化一个整数映射到字符串的哈希表
HashMap<Integer, String> map = new HashMap<>();

// 初始化一个字符串映射到数组的哈希表
HashMap<String, int[]> map = new HashMap<>();
```

#### 常用方法

```java
// 判断是否存在Key
boolean containsKey(Object key)

// 获取Key的对应Value，如果不存在则返回null
V get(Object key)

// 获取Key的对应Value，如果不存在则返回null
V getOrDefault(Object key, V defaultValue)

// 将Key和Value存入哈希表
V put(K key, V value)

// 将Key和Value存入哈希表，如果存在，则什么都不做
V putIfAbsent(K key, V value)

// 删除键值对并返回值
V remove(Object key)

// 获取哈希表中所有Key
Set<K> keySet()
```

### 队列 Queue

#### 初始化

```java
// Java中的Queue是一个接口
// 初始化一个存储String的队列
Queue<String> q = new LinkedList<>();
```

#### 常用方法

```java
// 判断是否为空
boolean isEmpty()

// 返回元素个数
int size()

// 返回队头元素
E peek()

// 删除并返回队头元素
E poll()

// 在队尾插入元素
boolean offer(E e)
```

### 堆栈 Stack

#### 初始化

```java
// 初始化一个int类型的堆栈
Stack<Integer> s = new Stack<>();
```

#### 常用方法

```java
// 判断是否为空
boolean isEmpty()

// 返回元素个数
int size()

// 将元素压入栈顶
E push(E e)

// 返回栈顶元素
E peek()

// 删除并的返回栈顶元素
E pop()
```

## 总结

刷题路漫漫...加油！

## 参考资料

> 1. [LeetCode 官网](https://leetcode.com)
> 2. [labuladong 的算法小抄](https://github.com/labuladong/fucking-algorithm)