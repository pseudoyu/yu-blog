---
title: "Go 错误处理总结与实践"
date: 2021-08-29T00:19:42+08:00
draft: false
tags: ["go", "error", "programming"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

最近在对极客时间毛剑老师的 Go 进阶训练营进行重温和学习汇总，这是一门比较偏向于工程化以及原理层面的的课程，涵盖的知识点非常多，因此决定开一个系列来进行记录，也便于自己总结查阅。这是系列第一篇《Go 错误处理》。

## Go 错误处理机制

### Go 内置 errors

Go 语言中的 `error` 就是普通的一个接口，表示值

```go
// http://golang.org/pkg/builtin/#error
// error 接口的定义

type error interface {
    Error() string
}

// http://golang.org/pkg/errors/error.go
// errors 构建 error 对象

type errorString struct {
    s string
}

func (e *errorString) Error() string {
    return e.s
}
```

基础库中有大量自定义的 `error`，如 `Error: EOF`，而 `errors.New()` 返回的是内部 `errorString` 对象的指针。

### Error 与 Exception

不同于 Java、C++ 等语言，Go 处理异常的逻辑是不引入 exception，而是采取多参数返回，因此可以在函数中带入 error interface 对象来交给调用者来进行处理。

```go
func handle() (int, error) {
    return 1, nil
}

func main() {
    i, err := handle()
    if err != nil {
        return
    }
    // 其他处理逻辑
}
```

需要注意的是，Go 中有 panic 的机制，可以和 recovery 搭配实现类似于 `try...exception...` 的效果，但是 Go 中的 panic 并不等同于 exception，exception 一般是交由调用者来进行处理，而 Go panic 则是针对真正异常的情况（如索引越界、栈溢出、不可恢复的环境问题等），意味着代码不能继续运行，而不能假设调用者会来解决 panic。

Go 的多返回值来支持调用者进行错误处理的方式给予了开发者很大的灵活性，有如下优势

- 简单
- Plan for failure, not success
- 没有隐藏的控制流
- 完全交给开发者来控制 error
- error 是值，因此有很大的灵活性进行处理

## Go 错误处理最佳实践

### panic

panic 只用于真正异常的情况，如

- 在程序启动的时候，如果有强依赖的服务出现故障时 panic 退出
- 在程序启动的时候，如果发现有配置明显不符合要求， 可以 panic 退出（防御编程）
- 在程序入口处，例如 gin 中间件需要使用 recovery 预防 panic 程序退出

因为 panic 会导致程序直接退出，而如果使用 recovery 进行处理的话性能不好且不可控。因此，其他情况下只要不是不可恢复的程序错误，都不应该直接 panic 应该返回 error，从而交给开发者。


### error

一般我们在开发中会使用 `github.com/pkg/errors` 处理应用错误，但需要注意的是，在公共库当中，我们一般不使用。

在通过多返回值来判断错误时，`error` 应该是函数的最后一个返回值，而当 `error` 不是 `nil` 时，其他返回值均应该为不可用状态，不应该对它们进行额外处理，错误处理的时候也应该先判断错误，当 `if err != nil` 时及时返回错误，从而避免过多的代码嵌套。

```go

// 错误示例

func f() error {
    ans, err := someFunc()
    if err == nil {
        // 其他逻辑
    }

    return err
}

// 正确示例

func f() error {
    ans, err := someFunc()
    if err != nil {
        return err
    }

    // 其他逻辑
    return nil
}
```

当程序出现错误时，一般使用 `errors.New` 或 `errors.Errorf` 返回错误值

```go
func someFunc() error {
    res := anotherFunc()
    if res != true {
        errors.Errorf("结果错误，已尝试 %d 次", count)
    }
    // 其他逻辑
    return nil
}
```

而如果是调用其他函数出现问题，则应该直接返回，如果需要携带额外信息，则使用 `errors.WithMessage`。

```go
func someFunc() error {
    res, err := anotherFunc()
    if err != nil {
        return errors.WithMessage(err, "other information")
    }
}
```

如果是调用其他库（标准库、企业公共库、开源第三方库等）获取到错误时，请使用 `errors.Wrap` 添加堆栈信息。只需要在错误第一次出现时使用，且在基础库和被大量引用的第三方库编写时一般不使用，避免堆栈信息重复。

```go
func f() error {
    err := json.Unmashal(&a, data)
    if err != nil {
        return errors.Wrap(err, "other information")
    }

    // 其他逻辑
    return nil
}
```

当需要对错误进行判断时，需要采用 `errors.Is` 进行比较

```go
func f() error {
    err := A()
    if errors.Is(err, io.EOF){
    	return nil
    }

    // 其他逻辑
    return nil
}
```

而对错误类型进行判断时则使用 `errors.As` 进行赋值

```go
func f() error {
    err := A()

    var errA errorA
    if errors.As(err, &errA){
    	// ...
    }

    // 其他逻辑
    return nil
}
```

对于业务中的错误（如输入错误等），最好在统一的一个地方建立自己的错误字典，其中应该包含错误代码并且可以在日志中作为独立字段打印，也需要有清晰的文档。

我们常常用日志来辅助我们进行错误处理，不需要进行返回、被忽略的错误必须输出日志，但禁止每个出错的地方都打日志。而如果同一个地方不停地报错，最好是打印一次错误详情并打印出现次数。

## 总结

以上就是对 Go 错误处理和最佳实践的一些总结，后续也会对错误类型、错误包装以及常见的使用中遇到的坑等进行总结。

## 参考资料

> 1. [Go 错误处理最佳实践](https://lailin.xyz/post/go-training-03.html)