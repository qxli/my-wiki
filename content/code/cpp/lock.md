---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
2.1 忘记释放锁
void data_process()
{
    EnterCriticalSection();

    if(/* error happens, forget LeaveCriticalSection */)
        return;

    LeaveCriticalSection();
}

2.2 单线程重复申请锁
void sub_func()
{
    EnterCriticalSection();
    do_something();
    LeaveCriticalSection();
}

void data_process()
{
    EnterCriticalSection();
    sub_func();
    LeaveCriticalSection();
}

2.3 多线程多锁申请
void data_process1()
{
    EnterCriticalSection(&cs1);　　// 申请锁的顺序有依赖
    EnterCriticalSection(&cs2);
    do_something1();
    LeaveCriticalSection(&cs2);
    LeaveCriticalSection(&cs1);
}

void data_process2()
{
    EnterCriticalSection(&cs2);　　// 申请锁的顺序有依赖
    EnterCriticalSection(&cs1);
    do_something2();
    LeaveCriticalSection(&cs1);
    LeaveCriticalSection(&cs2);
}

2.4 环形锁申请

/* 多个线程申请锁的顺序形成相互依赖的环形：
*             A   -  B
*             |      |
*             C   -  D
*/
```