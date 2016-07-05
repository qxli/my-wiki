---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#awk

##按字符串分割
```
$ awk -F'uid=' '{print $2}' /tmp/test.txt
```

##按列对某行进行相加
```
$ awk 'BEGIN{sum=0} {sum +=$1} END{print sum}' sorce.txt
```