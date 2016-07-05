---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#find

###按扩展名查找
```
$ find . -name "*.log" | xargs ls -hlrt
```

###按时间查找
```
-atime (accessed) 访问
-ctime (change) 状态改变
-mtime (modify) 文件修改


# 查找第3天修改的文件
$ find . -mtime 3 

# 查找第3天以外修改的文件
$ find . -mtime +3 

# 查找第3天以内修改的文件
$ find . -mtime -3 
```

###按大小查找
```
$ find . -size -3G
$ find . -size -3M
$ find . -size -3K
```