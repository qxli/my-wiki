---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#智能指针
##auto_ptr
它是"它所指向的对象"的拥有者，所以，```auto_ptr``` 管理的资源必须绝对没有一个以上的```auto_ptr``` 同时指向它。 这是因为资源的拥有者在销毁的时候，会销毁它所拥有的资源，资源不能释放两次，如果同时有两个```auto_ptr```拥有同一个资源，那么，在第一个```auto_ptr```销毁以后，第二个```auto_ptr```就成为野指针了。

##unique_ptr
```unique_ptr```是```auto_ptr```的替代品，它与```auto_ptr```一样拥有唯一拥有权的特性，与```auto_ptr```不一样的是，```unique_ptr```是没有复制构造函数的，因此比```auto_ptr```更安全。

##shared_ptr

1. 它允许多个该智能指针共享地“拥有”同一堆分配对象的内存；```shared_ptr```内部实现上使用的是引用计数这种方法，所以只有在引用计数归零的时候，```shared_ptr```才会真正的释放所占有的堆内存空间的。指针可以随意复制，在函数间传递，或者存储在容器里面。
2. ```shared_ptr```还有两个特有的成员函数，分别是：unique() 用于检查指针是否唯一的，如果是唯一的，就相当于```auto_ptr```，```use_count()``` 返回当前指针的引用计数，```use_count()``` 不提供高效率的操作，所以，```use_count()``` 应该仅仅用于测试或者调试。

##weak_ptr
```weak_ptr``` 被设计为与```shared_ptr``` 共同工作，可以从一个```shared_ptr``` 或者另一个```weak_ptr``` 对象构造，获得资源的观测权。但是```weak_ptr``` 没有共享资源，它的构造函数不会引起指针引用计数的增加。

#参考

- [智能指针学习笔记](http://mingxinglai.com/cn/2013/01/smart-ptr/)
- [C++智能指针简单剖析](http://www.jianshu.com/p/02bb7e6aeb03)
- [到C++11中的智能指针](http://www.jellythink.com/archives/684)
- [C++中的智能指针剖析](http://zheming.wang/czhong-de-zhi-neng-zhi-zhen-pou-xi.html)