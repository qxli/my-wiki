---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

##Scott Meyer版本
```cpp
template<typename T>
class Singleton
{
public:
    static T& getInstance()
    {
        static T value;
        return value;
    }
 
private:
    Singleton();
    ~Singleton();
};
```

[C++中多线程与Singleton的那些事儿](http://liyuanlife.com/blog/2015/01/31/thread-safe-singleton-in-cxx/)