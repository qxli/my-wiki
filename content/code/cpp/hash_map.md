---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#hash_map

##声明
```cpp
#include <ext/hash_map>
using namespace __gnu_cxx;
```

##效率
与map对比，100w或1000w比map得find快3倍

总体来说，hash_map 查找速度会比map快，而且查找速度基本和数据量大小无关，属于常数级别;而map的查找速度是log(n)级别。
hash还有hash函数的耗时。当有100w条记录的时候，map也只需要20次的比较，200w也只需要21次的比较！所以并不一定常数就比log(n)小！
hash_map对空间的要求要比map高很多，所以是以空间换时间的方法，而且，hash_map如果hash函数和hash因子选择不好的话，
也许不会达到你要的效果，所以至于用map，还是hash_map，从3个方面来权衡： 查找速度, 数据量, 内存使用，还有一个就是你的经验！
没有特别的标准