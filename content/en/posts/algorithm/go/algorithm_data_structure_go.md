---
title: "LeetCode 刷题常用数据结构（Go 篇）"
date: 2021-05-29T00:12:17+08:00
draft: false
tags: ["go","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

最近重新开始用 Go 刷 LeetCode 算法题，针对工作需求的算法刷题其实主要是锻炼解决问题的思路和代码撰写能力，而不是像算法竞赛那样用复杂的数据结构，所以常用的数据结构和操作并不多，熟练使用也能很好地提升自己的代码质量，特此做一个整理，以便于查阅。

## 数据结构

### 数组

#### 初始化

```go
// 初始化一个大小为10，默认值为0的数组
nums := make([10]int)

// 初始化一个二位boolean数组
visited := make([5][10]int)
```

#### 常用方法

```go
for i := 0; i < len(nums); i++ {
    // 访问num[i]
}
```

### 字符串 String

#### 初始化

```go
s1 := "hello world"

// 创建多行字符串
s2 := `This is a
multiline
string.`
```

#### 访问字符串

```go
// 可直接用索引访问字节（非字符）
s1 := "hello world"
first := s[0]

s2 := []byte(s1)
first := s2[0]
```

#### 修改字符串

```go
// 字符串的值是不可变的，可以分配一个新字符串值
s := "hello"
t := s

// 将字符串转为[]byte或[]rune可以进行修改
s1 := "hello world"
s2 := []byte(s1)
s2[0] = 'H'
s3 := string(s2)
```

#### 查询字符是否属于特定字符集

```go
    // 判断字符串s的i索引位置字符是否是元音
    if strings.Contains("aeiouAEIOU", string(s[i])) {
        // ...
    }
```

#### 判断字符串大小

```go
if s1 == s2 {
    // 相等
} else {
    // 不相等
}

// Compare 函数可以用于比较，1大于，0相等，-1小于
// EqualFold 函数忽略大小写后比较
```

#### 拼接字符串

```go
// 支持直接用+进行连接，但是效率不高
s1 := "hello "
s2 := s1 + "world"
```

#### 高效拼接字符串

```go
// bytes.Buffer可以一次性连接
var b bytes.Buffer
b.WriteString("Hello ")
b.WriteString("World")
b1 := b.String()

// 多个字符串拼接
var strs []string
strings.Join(strs, "World")
```

#### 整型 (或任意数据类型) 转为字符串

```go
// Itoa转换
i := 123
t := strconv.Itoa(i)

// Sprintf转换
i := 123
t := fmt.Sprintf("%d", i)
```

### 切片 slice

#### 初始化

```go
// 初始化一个存储String类型的切片
slice := make([]string, 0)
slice := []string

// 初始化一个存储int类型的切片
slice := make([]int, 0)
slice := []int
```

#### 常用方法

```go
// 判断是否为空
if len(slice) == 0 {
    // 为空
}

// 返回元素个数
len()

// 访问索引元素
slice[i]

// 在尾部添加元素
slice = append(slice, 1)
```

### 通过切片模拟栈和队列

#### 栈

```go
// 创建栈
stack := make([]int, 0)
// push压入
stack = append(stack, 10)
// pop弹出
v := stack[len(stack) - 1]
stack = stack[:len(stack) - 1]
// 检查栈空
len(stack) == 0
```

#### 队列

```go
// 创建队列
queue := make([]int, 0)
// enqueue入队
queue = append(queue, 10)
// dequeue出队
v := queue[0]
queue = queue[1:]
// 长度0为空
len(queue) == 0
```

### Map

```go

// 创建
m := make(map[string]int)
// 设置kv
m["hello"] = 1
// 删除k
delete(m,"hello")
// 遍历
for k, v := range m{
    // 操作
}

// map键需要可比较，不能为slice、map、function
// map值都有默认值，可以直接操作默认值，如：m[age]++ 值由0变为1
// 比较两个map需要遍历，其中的kv是否相同，因为有默认值关系，所以需要检查val和ok两个值
```

### 标准库

#### sort

```go
// int排序
sort.Ints([]int{})
// 字符串排序
sort.Strings([]string{})
```

#### math

```go
// int32 最大最小值
math.MaxInt32
math.MinInt32
// int64 最大最小值（int默认是int64）
math.MaxInt64
math.MinInt64
```

#### copy

```go
// 删除a[i]，可以用 copy 将i+1到末尾的值覆盖到i,然后末尾-1
copy(a[i:], a[i+1:])
a = a[:len(a)-1]

// make创建长度，则通过索引赋值
a := make([]int, n)
a[n] = x

// make长度为0，则通过append()赋值
a := make([]int, 0)
a = append(a, x)
```

### 类型转换

```go
// byte转数字
s = "12345"  // s[0] 类型是byte
num := int(s[0] - '0') // 1
str := string(s[0]) // "1"
b := byte(num + '0') // '1'
fmt.Printf("%d%s%c\n", num, str, b) // 111

// 字符串转数字
num, _ := strconv.Atoi()
str := strconv.Itoa()
```

## 总结

刷题路漫漫...加油！

## 参考资料

> 1. [LeetCode 官网](https://leetcode.com)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)