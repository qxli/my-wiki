---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#grep
##递归查找某字符串
```
$ grep -rn --include="*.log" "foobar" /var/log/
```
##问题
###Binary file a.log matches
```
  # -a, --text    equivalent to --binary-files=text
$ grep -a "xx" a.log
```