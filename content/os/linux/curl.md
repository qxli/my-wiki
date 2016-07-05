---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#curl

```
-d/--data <data>   HTTP POST方式传送数据
```

## 1. 向页面发送get请求
```
$ curl "www.baidu.com/s?wd=hello"
```

## 2. 向页面发送post请求
```
$ curl -d "wd=hello" "www.baidu.com/s"
```