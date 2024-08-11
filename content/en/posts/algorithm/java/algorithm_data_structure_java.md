---
title: "Common Data Structures for LeetCode Problem Solving (Java Edition)"
date: 2021-01-01T00:12:17+08:00
draft: false
tags: ["java","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've started solving algorithm problems on LeetCode. For job-related algorithm practice, the main focus is on honing problem-solving approaches and coding skills, rather than using complex data structures as in algorithm competitions. Therefore, the commonly used data structures and operations are not numerous. Proficient use of these can significantly improve one's code quality. I've compiled this summary for easy reference.

## Data Structures

### Array []

#### Initialization

```java
// Initialize an array of size 10 with default value 0
int[] nums = new int[10];

// Initialize a 2D boolean array
boolean[][] visited = new boolean[5][10];
```

#### Common Methods

```java
// Generally, a non-empty check is performed at the beginning of a function, then elements are accessed using index
if (nums.length == 0) {
    return;
}

for (int i = 0; i < nums.length; i++) {
    // Access num[i]
}
```

### String

#### Initialization

```java
String s1 = "hello world";
```

#### Accessing String

```java
// String doesn't support direct access to characters using []
char c = s1.charAt(2);
```

#### Modifying String

```java
// String doesn't support direct modification, it needs to be converted to char[] for modification
char[] chars = s1.toCharArray();
chars[1] = 'a';
String s2 = new String(chars);
```

#### Comparing Strings

```java
// Always use the equals method for comparison, not ==
if (s1.equals(s2)) {
    // Equal
} else {
    // Not equal
}
```

#### Concatenating Strings

```java
// Direct concatenation with + is supported, but not efficient
String s3 = s1 + "!";
```

#### Using StringBuilder for Frequent String Concatenation to Improve Efficiency

```java
StringBuilder sb = new StringBuilder();

for (char c = 'a'; c <= 'f'; c++) {
    // The append method supports concatenating characters, strings, numbers, etc.
    sb.append(c);
    String result = sb.toString();
}
```

### ArrayList

#### Initialization

```java
// Initialize a dynamic array storing String type
ArrayList<String> strings = new ArrayList<>();

// Initialize a dynamic array storing int type
ArrayList<Integer> nums = new ArrayList<>();
```

#### Common Methods

```java
// Check if empty
boolean isEmpty()

// Return number of elements
int size()

// Access element by index
E get(int index)

// Add element at the end
boolean add(E e)
```

### LinkedList

#### Initialization

```java
// Initialize a doubly linked list storing String type
LinkedList<String> strings = new LinkedList<>();

// Initialize a doubly linked list storing int type
LinkedList<Integer> nums = new LinkedList<>();
```

#### Common Methods

```java
// Check if empty
boolean isEmpty()

// Return number of elements
int size()

// Add element at the end
boolean add(E e)

// Remove and return the last element
E removeLast()

// Add element at the beginning
void addFirst(E e)

// Remove and return the first element
E removeFirst()
```

### HashMap

#### Initialization

```java
// Initialize a hash map mapping integers to strings
HashMap<Integer, String> map = new HashMap<>();

// Initialize a hash map mapping strings to integer arrays
HashMap<String, int[]> map = new HashMap<>();
```

#### Common Methods

```java
// Check if a key exists
boolean containsKey(Object key)

// Get the value corresponding to the key, return null if not exists
V get(Object key)

// Get the value corresponding to the key, return defaultValue if not exists
V getOrDefault(Object key, V defaultValue)

// Store key-value pair in the hash map
V put(K key, V value)

// Store key-value pair in the hash map if not exists
V putIfAbsent(K key, V value)

// Remove key-value pair and return the value
V remove(Object key)

// Get all keys in the hash map
Set<K> keySet()
```

### Queue

#### Initialization

```java
// Queue is an interface in Java
// Initialize a queue storing String
Queue<String> q = new LinkedList<>();
```

#### Common Methods

```java
// Check if empty
boolean isEmpty()

// Return number of elements
int size()

// Return the element at the front of the queue
E peek()

// Remove and return the element at the front of the queue
E poll()

// Insert element at the end of the queue
boolean offer(E e)
```

### Stack

#### Initialization

```java
// Initialize a stack of int type
Stack<Integer> s = new Stack<>();
```

#### Common Methods

```java
// Check if empty
boolean isEmpty()

// Return number of elements
int size()

// Push element onto the top of the stack
E push(E e)

// Return the element at the top of the stack
E peek()

// Remove and return the element at the top of the stack
E pop()
```

## Conclusion

The journey of problem-solving is long... Keep going!

## References

> 1. [LeetCode Official Website](https://leetcode.com)
> 2. [labuladong's Algorithm Cheat Sheet](https://github.com/labuladong/fucking-algorithm)