---
title: "Common Data Structures for LeetCode Problem Solving (Go Edition)"
date: 2021-05-29T00:12:17+08:00
draft: false
tags: ["go","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've resumed solving LeetCode algorithm problems using Go. For work-related algorithm practice, the main focus is on honing problem-solving approaches and coding skills, rather than employing complex data structures as in algorithmic competitions. The commonly used data structures and operations are relatively few, but mastering them can significantly improve one's code quality. I've compiled this summary for easy reference.

## Data Structures

### Arrays

#### Initialization

```go
// Initialize an array of size 10 with default value 0
nums := make([10]int)

// Initialize a two-dimensional boolean array
visited := make([5][10]int)
```

#### Common Methods

```go
for i := 0; i < len(nums); i++ {
    // Access num[i]
}
```

### Strings

#### Initialization

```go
s1 := "hello world"

// Create a multi-line string
s2 := `This is a
multiline
string.`
```

#### Accessing Strings

```go
// Directly access bytes (not characters) using index
s1 := "hello world"
first := s[0]

s2 := []byte(s1)
first := s2[0]
```

#### Modifying Strings

```go
// String values are immutable, can assign a new string value
s := "hello"
t := s

// Convert string to []byte or []rune for modification
s1 := "hello world"
s2 := []byte(s1)
s2[0] = 'H'
s3 := string(s2)
```

#### Check if Character Belongs to Specific Character Set

```go
    // Check if the character at index i of string s is a vowel
    if strings.Contains("aeiouAEIOU", string(s[i])) {
        // ...
    }
```

#### Compare Strings

```go
if s1 == s2 {
    // Equal
} else {
    // Not equal
}

// Compare function can be used for comparison, 1 greater, 0 equal, -1 less
// EqualFold function compares ignoring case
```

#### Concatenate Strings

```go
// Directly use + for concatenation, but not efficient
s1 := "hello "
s2 := s1 + "world"
```

#### Efficient String Concatenation

```go
// bytes.Buffer can concatenate at once
var b bytes.Buffer
b.WriteString("Hello ")
b.WriteString("World")
b1 := b.String()

// Concatenate multiple strings
var strs []string
strings.Join(strs, "World")
```

#### Convert Integer (or Any Data Type) to String

```go
// Itoa conversion
i := 123
t := strconv.Itoa(i)

// Sprintf conversion
i := 123
t := fmt.Sprintf("%d", i)
```

### Slices

#### Initialization

```go
// Initialize a slice storing String type
slice := make([]string, 0)
slice := []string

// Initialize a slice storing int type
slice := make([]int, 0)
slice := []int
```

#### Common Methods

```go
// Check if empty
if len(slice) == 0 {
    // Empty
}

// Return number of elements
len()

// Access element by index
slice[i]

// Append element at the end
slice = append(slice, 1)
```

### Simulating Stack and Queue with Slices

#### Stack

```go
// Create stack
stack := make([]int, 0)
// Push
stack = append(stack, 10)
// Pop
v := stack[len(stack) - 1]
stack = stack[:len(stack) - 1]
// Check if stack is empty
len(stack) == 0
```

#### Queue

```go
// Create queue
queue := make([]int, 0)
// Enqueue
queue = append(queue, 10)
// Dequeue
v := queue[0]
queue = queue[1:]
// Length 0 is empty
len(queue) == 0
```

### Map

```go
// Create
m := make(map[string]int)
// Set key-value
m["hello"] = 1
// Delete key
delete(m,"hello")
// Iterate
for k, v := range m{
    // Operation
}

// Map keys need to be comparable, cannot be slice, map, function
// Map values have default values, can operate directly on default values, e.g., m[age]++ value changes from 0 to 1
// To compare two maps, need to iterate and check if kv are the same, due to default value relationship, need to check both val and ok
```

### Standard Library

#### sort

```go
// Sort integers
sort.Ints([]int{})
// Sort strings
sort.Strings([]string{})
```

#### math

```go
// int32 max and min values
math.MaxInt32
math.MinInt32
// int64 max and min values (int defaults to int64)
math.MaxInt64
math.MinInt64
```

#### copy

```go
// To delete a[i], can use copy to overwrite i to end values to i, then end -1
copy(a[i:], a[i+1:])
a = a[:len(a)-1]

// make creates length, then assign value by index
a := make([]int, n)
a[n] = x

// make length 0, then assign value using append()
a := make([]int, 0)
a = append(a, x)
```

### Type Conversion

```go
// byte to number
s = "12345"  // s[0] is of type byte
num := int(s[0] - '0') // 1
str := string(s[0]) // "1"
b := byte(num + '0') // '1'
fmt.Printf("%d%s%c\n", num, str, b) // 111

// string to number
num, _ := strconv.Atoi()
str := strconv.Itoa()
```

## Conclusion

The journey of problem-solving is long... Keep going!

## References

> 1. [LeetCode Official Website](https://leetcode.com)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)