---
title: "Go Error Handling Summary and Best Practices"
date: 2021-08-29T00:19:42+08:00
draft: false
tags: ["go", "error", "programming", "translation"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've been reviewing and summarizing the Go Advanced Training Camp by Mr. Mao Jian from GeekTime. This is a course that leans more towards engineering and principles, covering a wide range of knowledge points. Therefore, I've decided to start a series to record and summarize, which will also facilitate my own review and reference. This is the first article in the series, "Go Error Handling".

## Go Error Handling Mechanism

### Go Built-in Errors

In Go, an `error` is simply a regular interface representing a value:

```go
// http://golang.org/pkg/builtin/#error
// Definition of the error interface

type error interface {
    Error() string
}

// http://golang.org/pkg/errors/error.go
// errors construct error objects

type errorString struct {
    s string
}

func (e *errorString) Error() string {
    return e.s
}
```

There are numerous custom `error` types in the standard library, such as `Error: EOF`, and `errors.New()` returns a pointer to the internal `errorString` object.

### Error vs Exception

Unlike languages such as Java and C++, Go's approach to handling exceptions is not to introduce exceptions, but to use multiple return parameters. Therefore, an error interface object can be included in the function to be handled by the caller.

```go
func handle() (int, error) {
    return 1, nil
}

func main() {
    i, err := handle()
    if err != nil {
        return
    }
    // Other processing logic
}
```

It's worth noting that Go has a panic mechanism, which can be used in conjunction with recovery to achieve an effect similar to `try...exception...`. However, Go's panic is not equivalent to exceptions. Exceptions are generally handled by the caller, while Go's panic is for truly exceptional situations (such as index out of bounds, stack overflow, unrecoverable environmental issues, etc.), indicating that the code cannot continue to run and should not assume that the caller will resolve the panic.

Go's multi-return value approach to support error handling by the caller offers developers great flexibility, with the following advantages:

- Simplicity
- Plan for failure, not success
- No hidden control flow
- Complete control over error handling given to the developer
- Error is a value, thus providing great flexibility in handling

## Go Error Handling Best Practices

### Panic

Panic should only be used in truly exceptional situations, such as:

- When a critical service fails during program startup, panic and exit
- If configurations are clearly inappropriate during program startup, panic and exit (defensive programming)
- At program entry points, such as using recovery in gin middleware to prevent program exit due to panic

Since panic causes the program to exit directly, and using recovery for handling is neither performant nor controllable, panic should not be used directly in other situations unless the program error is unrecoverable. Instead, an error should be returned, leaving it to the developer to handle.

### Error

In development, we generally use `github.com/pkg/errors` to handle application errors, but it's important to note that we typically don't use this in public libraries.

When using multiple return values to check for errors, `error` should be the last return value of the function. When `error` is not `nil`, other return values should be in an unusable state and should not be processed further. When handling errors, we should check for errors first, returning immediately when `if err != nil` to avoid excessive code nesting.

```go

// Incorrect example

func f() error {
    ans, err := someFunc()
    if err == nil {
        // Other logic
    }

    return err
}

// Correct example

func f() error {
    ans, err := someFunc()
    if err != nil {
        return err
    }

    // Other logic
    return nil
}
```

When an error occurs in the program, generally use `errors.New` or `errors.Errorf` to return an error value:

```go
func someFunc() error {
    res := anotherFunc()
    if res != true {
        errors.Errorf("Result incorrect, attempted %d times", count)
    }
    // Other logic
    return nil
}
```

If a problem occurs when calling other functions, it should be returned directly. If additional information needs to be carried, use `errors.WithMessage`.

```go
func someFunc() error {
    res, err := anotherFunc()
    if err != nil {
        return errors.WithMessage(err, "other information")
    }
}
```

When obtaining errors from other libraries (standard libraries, enterprise public libraries, open-source third-party libraries, etc.), please use `errors.Wrap` to add stack information. This only needs to be used when the error first appears, and is generally not used when writing basic libraries and widely referenced third-party libraries to avoid duplicate stack information.

```go
func f() error {
    err := json.Unmashal(&a, data)
    if err != nil {
        return errors.Wrap(err, "other information")
    }

    // Other logic
    return nil
}
```

When errors need to be judged, `errors.Is` should be used for comparison:

```go
func f() error {
    err := A()
    if errors.Is(err, io.EOF){
    	return nil
    }

    // Other logic
    return nil
}
```

When judging error types, use `errors.As` for assignment:

```go
func f() error {
    err := A()

    var errA errorA
    if errors.As(err, &errA){
    	// ...
    }

    // Other logic
    return nil
}
```

For errors in business logic (such as input errors), it's best to establish your own error dictionary in a unified place, which should include error codes and can be printed as separate fields in logs. Clear documentation is also needed.

We often use logs to assist with error handling. Errors that don't need to be returned or are ignored must be logged, but it's forbidden to log at every error point. If the same place keeps reporting errors, it's best to print the error details once and print the number of occurrences.

## Conclusion

The above is a summary of Go error handling and best practices. In future, I will also summarize error types, error wrapping, and common pitfalls encountered in use.

## References

> 1. [Go Error Handling Best Practices](https://lailin.xyz/post/go-training-03.html)