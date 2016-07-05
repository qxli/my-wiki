title: "Getting Started"
layout: page
date: 2099-06-02 00:00

## 文件格式
Makefile文件由一系列规则（rules）构成。每条规则的形式如下。
```
<target> : <prerequisites> 
[tab]  <commands>
```

### 目标（target）
一个目标（target）就构成一条规则。目标通常是文件名，指明Make命令所要构建的对象，除了文件名，目标还可以是某个操作的名字，这称为"伪目标"（phony target）。但是，如果当前目录中，正好有一个文件叫做clean，那么这个命令不会执行。因为Make发现clean文件已经存在，就认为没有必要重新构建了，就不会执行指定的rm命令。为了避免这种情况，可以明确声明clean是"伪目标"，写法如下。
```
.PHONY: clean
clean:
        rm *.o temp
```

### 前置条件（prerequisites）
前置条件通常是一组文件名，之间用空格分隔。它指定了"目标"是否重新构建的判断标准：只要有一个前置文件不存在，或者有过更新（前置文件的last-modification时间戳比目标的时间戳新），"目标"就需要重新构建。
```
result.txt: source.txt
    cp source.txt result.txt
```
上面代码中，构建 result.txt 的前置条件是 source.txt 。如果当前目录中，source.txt 已经存在，那么make result.txt可以正常运行，否则必须再写一条规则，来生成 source.txt 。
```
source.txt:
    echo "this is the source" > source.txt
```
上面代码中，source.txt后面没有前置条件，就意味着它跟其他文件都无关，只要这个文件还不存在，每次调用make source.txt，它都会生成。

### 命令（commands）
命令（commands）表示如何更新目标文件，由一行或多行的Shell命令组成。它是构建"目标"的具体指令，它的运行结果通常就是生成目标文件。每行命令之前必须有一个tab键。如果想用其他键，可以用内置变量.RECIPEPREFIX声明。需要注意的是，每行命令在一个单独的shell中执行。这些Shell之间没有继承关系。
一个解决办法是将两行命令写在一行，中间用分号分隔。
```
var-kept:
    export foo=bar; echo "foo=[$$foo]"
```
另一个解决办法是在换行符前加反斜杠转义。
```
var-kept:
    export foo=bar; \
    echo "foo=[$$foo]"
```
最后一个方法是加上.ONESHELL:命令。
```
.ONESHELL:
var-kept:
    export foo=bar; 
    echo "foo=[$$foo]"
```

## 文件语法
### 注释
井号（#）在Makefile中表示注释。
```
# 这是注释
result.txt: source.txt
    # 这是注释
    cp source.txt result.txt # 这也是注释
```

### 回声（echoing）
正常情况下，make会打印每条命令，然后再执行，这就叫做回声（echoing）。在命令的前面加上@，就可以关闭回声。
```
test:
    @# 这是测试
    @echo TODO
```

### 通配符
通配符（wildcard）用来指定一组符合条件的文件名。Makefile 的通配符与 Bash 一致，主要有星号（*）、问号（？）和 [...] 。比如， *.o 表示所有后缀名为o的文件。
```
clean:
        rm -f *.o
```

### 模式匹配
Make命令允许对文件名，进行类似正则运算的匹配，主要用到的匹配符是%。比如，假定当前目录下有 f1.c 和 f2.c 两个源码文件，需要将它们编译为对应的对象文件。使用匹配符%，可以将大量同类型的文件，只用一条规则就完成构建。
```
%.o: %.c
```

### 变量和赋值符
Makefile 允许使用等号自定义变量。调用Shell变量，需要在美元符号前，再加一个美元符号，这是因为Make命令会对美元符号转义。
```
txt = Hello World
test:
    @echo $(txt)
    @echo $$HOME
```
四个赋值运算符 （=、:=、？=、+=）
```
VARIABLE = value
# 在执行时扩展，允许递归扩展。

VARIABLE := value
# 在定义时扩展。

VARIABLE ?= value
# 只有在该变量为空时才设置值。

VARIABLE += value
# 将值追加到变量的尾端。
```

### 内置变量（Implicit Variables）
Make命令提供一系列内置变量，比如，$(CC) 指向当前使用的编译器，$(MAKE) 指向当前使用的Make工具。这主要是为了跨平台的兼容性，详细的内置变量清单见[手册](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html)。
```
output:
    $(CC) -o output input.c
```

### 自动变量（Automatic Variables）
#### $@
$@指代当前目标，就是Make命令当前构建的那个目标。比如，make foo的 $@ 就指代foo。
```
a.txt b.txt: 
    touch $@
```
等同于下面的写法。
```
a.txt:
    touch a.txt
b.txt:
    touch b.txt
```
#### $<
$< 指代第一个前置条件。比如，规则为 t: p1 p2，那么$< 就指代p1。
```
a.txt: b.txt c.txt
    cp $< $@ 
```
等同于下面的写法。
```
a.txt: b.txt c.txt
    cp b.txt a.txt 
```

#### $?
$? 指代比目标更新的所有前置条件，之间以空格分隔。比如，规则为 t: p1 p2，其中 p2 的时间戳比 t 新，$?就指代p2。
#### $^
$^ 指代所有前置条件，之间以空格分隔。比如，规则为 t: p1 p2，那么 $^ 就指代 p1 p2 。
#### $*
$* 指代匹配符 % 匹配的部分， 比如% 匹配 f1.txt 中的f1 ，$* 就表示 f1。
#### $(@D) 和 $(@F)
$(@D) 和 $(@F) 分别指向 $@ 的目录名和文件名。比如，$@是 src/input.c，那么$(@D) 的值为 src ，$(@F) 的值为 input.c。
#### $(<D) 和 $(<F)
$(<D) 和 $(<F) 分别指向 $< 的目录名和文件名。
所有的自动变量清单，请看[手册](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)。下面是自动变量的一个例子。
```
dest/%.txt: src/%.txt
    @[ -d dest ] || mkdir dest
    cp $< $@
```
上面代码将 src 目录下的 txt 文件，拷贝到 dest 目录下。首先判断 dest 目录是否存在，如果不存在就新建，然后，$< 指代前置文件（src/%.txt）， $@ 指代目标文件（dest/%.txt）。