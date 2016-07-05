title: "Getting Started"
layout: page
date: 2099-06-02 00:00

#gdb
## 启动gdb
对C/C++程序的调试，需要在编译前就加上-g选项，
### 调试可执行文件:
```
$ gdb <program>
```
### 调试core文件
```
$ gdb <program> <core dump file>
```
### 调试服务程序
```
$ gdb <program> <PID>
```
## 调试命令
### 运行

- c，coutinue，继续执行，到下一个断点处（或运行结束）
- r，run，运行程序
- n，next，单步调试，当遇到函数调用时，也不进入此函数体；
- s，step，单步调试如果有函数调用，则进入函数；
- finish，运行程序，直到当前函数完成返回

### 设置断点

- b，break，在第n行处设置断点（可以带上代码路径和代码名称： b foo.cpp:578）
- info b，查看断点信息
- delete n，删除第n个断点

### 查看源代码

- p，print，用来打印变量或者其他信息
- layout src，出现一个窗口可以查看源代码，等同于Ctrl-X + A


### 打印表达式

- l，列出程序的源代码，默认每次显示10行。

### 查询运行信息

- bt，backtrace，查看调用过程


##core文件
是否生成core dump
```
$ ulimit -c
```
如果结果为0，说明当程序崩溃时，系统并不能生成core dump。则要如下操作

```
$ ulimit -c unlimited
```

## 参考资料
[gdb 调试利器](http://linuxtools-rst.readthedocs.org/zh_CN/latest/tool/gdb.html)