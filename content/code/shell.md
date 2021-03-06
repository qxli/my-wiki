---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#shell

## if...else...
###语法

- if与[之间要有空格
- []与判断条件之间也必须有空格
- ]与;之间不能有空格

```sh
#!/bin/sh

input=$1
if [ "$input" == "1" ] || [ "$input" == "2" ]; then
    echo "foobar1"
elif [ "$input" == "3" ]; then
    echo "foobar2"
else
    echo "foorbar3"
fi
```
### 数字判断

- -eq(equal)   等于
- -ne(no equal)   不等于
- -gt(greater than)   大于
- -lt(less than)   小于
- -le(less than or equal)   小于等于
- -ge(greater than or equal)   大于等于

### 字符串判断

- ==/=  两个字符相等
- !=    两个字符不等
- -n    非空串
- -z    空串

### 文件判断

- -r file #用户可读为真
- -w file #用户可写为真
- -x file #用户可执行为真
- -f file #文件存在且为正规文件为真
- -d file #如果是存在目录为真
- -c file #文件存在且为字符设备文件
- -b file #文件存在且为块设备文件
- -s file #文件大小为非0为真，可以判断文件是否为空
- -e file #如果文件存在为真

### 逻辑判断

- && / -a 与
- || / -o 或
- ! 非

##加减乘除
### 1. expr
```
a=8
b=2
c=`expr $a + $b`
d=`expr $a - $b`
e=`expr $a / $b`
f=`expr $a % $b`
g=`expr $a * $b`
echo c=$c,d=$d,e=$e,f=$f,g=$g

#c=10,d=6,e=4,f=0,g=16

```
### 2. $(())
```
a=8
b=2
c=$(($a*$b - $a/$b))
echo $c
```

### 3. bc
```
a=5.01
b=2.0
c=$(echo "$a-4*$b"|bc)
echo $c
```

##/dev/null
```
/dev/null 代表空设备文件 
>/dev/null 等同于 1>/dev/null
```
```
1>/dev/null 2>&1
所有输出（包括错误）都重定向到空设备文件
1  ：表示stdout标准输出，系统默认值是1
2  ：表示stderr标准错误
&  ：表示等同于的意思，2>&1，表示2的输出重定向等同于1
```

## 文件操作
### 按行读文件
```sh
while read line
do
    echo $line
done < phn.txt
```

## 路径操作
### 获取文件名
```
# 获取文件名含后缀
$ basename /tmp/main.cpp

# 获取文件名 去掉后缀
$ basename /tmp/main.cpp .cpp
```

## 字符串处理
### 删除字符串最后一个字符
```
$ ${var%?}
```
### 删除字符串第一个字符
```
$ ${var#?}
```
### 字符串切割

```
${var:offset} #获取var中offset开始的字串
${var:offset:length} #获取var中offset开始长为length的字串。
```
```
cut -c start-end /tmp/test.txt #获取test.txt中每行start到end之间的字符串
echo $var | cut -c pos #获取var中pos字符
echo $var | cut -c start- #获取var中start之后的字符
echo $var | cut -c -end #获取var中end之前的字符
```


### 字符串替换
```
$ ${var/pattern/string}
# 使用string替换pattern的最大匹配部分。如果pattern以/开头则进行全部替换，否则只替换第一个匹配的位置。
如果pattern以#开始，则起始部分必须匹配，如果以%开始则结尾部分必须匹配
```

### for..in..循环
```
arr="element1 element2 element3"
for i in $arr
do
    echo $i
done
```