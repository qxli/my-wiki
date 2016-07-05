title: "Getting Started"
layout: page
date: 2099-06-02 00:00

#GCC / G++

## 介绍
GCC是GNU Compiler Collection的简称,除编译程序外,还包含其他相关工具.GCC可将高级语言编写的源代码构建成计算机直接执行的二进制代码.

##编译选项
### -o
指定目标名称,缺省的时候,编译出来的文件是a.out

### -E
仅作预处理并直接显示,不进行编译,汇编和链接

### -S
预处理和编译到汇编语言(自动生成.s文件),不进行汇编和链接

### -c
仅作预处理,编译和汇编并生成目标文件(与源文件同名,后缀为.o)

### -I
指定不在标准或是系统搜索路径中的 include 文件路径

### -g
产生调试信息

### -l
编译的时候需要链接的库，如-lpthread

### -D
设定预处理的宏，比如 -DNDEBUG

### -Wall
显示所有的警告

### -O
使用编译优化级别1编译程序.O后可附带其他的数值,表示不同的优化级别.级别越大优化效果越好,编译时间越长.

### -std
指定语言标准，比如 -std=c++11等；

### -shared
生成共享目标文件,用于建立共享链接库.

### -fPIC
作用于编译阶段，告诉编译器产生与位置无关代码(Position-Independent Code),则产生的代码中，没有绝对地址，全部使用相对地址，故而代码可以被加载器加载到内存的任意位置，都可以正确的执行。这正是共享库所要求的，共享库被加载时，在内存的位置不是固定的。

### -fpermissive
Downgrade some diagnostics about nonconformant code from errors to warnings. 
Thus, using -fpermissive will allow some nonconforming code to compile.

### -finput-charset
指定输入文件的的字符编码，如-finput-charset=GBK

##区别

- 对于.c后缀的文件,gcc把它当做是C程序；g++当做是C++程序；
- 对于.cpp后缀的文件，gcc和g++都会当做c++程序。
- 编译阶段，g++会调用gcc(也就是说);连接阶段，通常会用g++来完成，这是因为gcc命令不能自动和c++程序使用的库连接。
 gcc可以用来编译c++但是它不会自动调用链接的c++库，你需要自己手动链接，使用如下命令： gcc -lstdc++ main.cpp。g++则会自动调用链接的c++库。