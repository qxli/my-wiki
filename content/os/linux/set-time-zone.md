---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

## 设置时区

### 运行tzselect
```
$ sudo tzselect

选择亚洲 Asia，确认之后选择中国（China)，最后选择北京(Beijing)
```

### 复制文件到/etc目录下
```
$ sudo cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
```