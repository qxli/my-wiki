---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#uniq

### 去除重复行
```
$ cat 1.txt | sort | uniq
```
### 获得重复的数据
```
$ cat 1.txt | sort | uniq -d
```
### 获得没有重复的数据
```
$ cat 1.txt | sort | uniq -u
```
### 统计重复的数据个数
```
$ cat 1.txt | sort | uniq -c
```