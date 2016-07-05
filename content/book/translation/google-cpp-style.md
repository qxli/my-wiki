---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#谷歌c++代码风格指南

##命名

- 类型命名  
所有类型的命名，包括类，结构体，类型定义和枚举值都有同样的命名习惯，类型命名以大写字母开始并且每个单词都是大写字母，不能有下划线，
例如：

```cpp
// classes and structs
class UrlTable { ...
class UrlTableTester { ...
struct UrlTableProperties { ...

// typedefs
typedef hash_map<UrlTableProperties *, string> PropertiesMap;

// enums
enum UrlTableErrors { ...
```