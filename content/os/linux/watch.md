---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#watch
```
-n --interval  watch缺省每2秒运行一下程序，可以用-n或-interval来指定间隔的时间。
-d --differences  高亮显示变化的区域。
-t -no-title  会关闭在顶部的时间间隔,命令，当前时间的输出。
```

## 1. 监测一个命令的运行结果
```
// 每2秒查看文件行数变化
$ watch -n 2 -d "cat 1.txt | wc -l"
```