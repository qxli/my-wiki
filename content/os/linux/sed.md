---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#sed
##选定某行
```
# 查看文件某一行
$ sed -n 10p foo.txt

# 查看文件某几行  
$ sed -n 10,16p foo.txt
```

##替换某行
```
$ sed -i 's/[匹配字符串]/[替换字符串]/g' [文件名]

Mac系统需要设置备份文件也可以为空
$ sed -i '.bak' 's/Test String/New Test String/g' *.txt
```

##删除某行
```
# 删除文件某行
$ sed -i '1d' foo.txt

# 删除文件最后一行
$ sed -i '$d' foo.txt

# 删除文件包含某个关键词的所有行
$ sed -i '/hello/d' foo.txt
```