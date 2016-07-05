---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

##GIL
GIL全称**Global Interpreter Lock**，GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念
###产生原因
为了利用多核，Python开始支持多线程。而解决多线程之间数据完整性和状态同步的最简单方法自然就是加锁。 于是有了GIL这把超级大锁，而当越来越多的代码库开发者接受了这种设定后，他们开始大量依赖这种特性（即默认python内部对象是thread-safe的，无需在实现时考虑额外的内存锁和同步操作）。
###避免方法

- multiprocessing
- C 语言扩展机制
- ctypes

##修饰器
装饰器的作用就是为已经存在的对象添加额外的功能。
```python
from functools import wraps

def connect_try_again(attempt):
    def decorator(func):
        @wraps(func)
        def wrapped(*agrs, **kwargs):
            att = 0
            while att < attempt:
                try:
                    return func(*agrs, **kwargs)
                except Exception as e:
                    print "exception"
                    att += 1
        return wrapped
    return decorator

@connect_try_again(attempt=3)
def foo():
    raise Exception("foobar")
```

##函数库

- [时间相关转化](/python::datetime)


## 排序
### 元素为字典
```python
def age(s): 
    return s['age']  
f = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]
f2 = sorted(f,key = lambda x:x['age'], reverse = True)
或
f2 = sorted(f,key = age)      #自定义函数按列表f中字典的age从小到大排序 
```

##数据结构
###set
```
a = t | s          # t 和 s的并集  
b = t & s          # t 和 s的交集  
c = t – s          # 求差集（项在t中，但不在s中）  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）  
```
###list和tuple区别
list可以修改，tuple不可以修改，并且tuple可以作为字典的key

## 参考
[Python集合（set）类型的操作](http://blog.csdn.net/business122/article/details/7541486)   
[PYTHON-基础-时间日期处理小结](http://www.wklken.me/posts/2015/03/03/python-base-datetime.html#2-date)   
[python的排序函数sort,sorted在列表排序和字典排序](http://wangwei007.blog.51cto.com/68019/1100742)    
[Python的GIL是什么鬼，多线程性能究竟如何](http://cenalulu.github.io/python/gil-in-python/)    
[python 线程，GIL 和 ctypes](http://zhuoqiang.me/python-thread-gil-and-ctypes.html)   
[Python装饰器与面向切面编程](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)