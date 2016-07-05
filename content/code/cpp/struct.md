---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#结构体

## struct和typedef struct
在c++里我们通常这么定义结构体
```cpp
struct Foo { ... };
Foo x;
```
但是在c中这样编译器会提示错误，必须这么定义：`struct Foo x;`，所以任何时候想用`Foo`都必须`struct Foo`，这样很麻烦，
所以可以按如下这么写
```cpp
struct Foo { ... };
typedef struct Foo Foo;
```
或者简写成
```cpp
typedef struct Foo { ... } Foo;
```
进一步缩写成
```cpp
typedef struct { ... } Foo;
```