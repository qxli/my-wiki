---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

##单链表
###单链表的反转
#### 分析
```
初始位置：
 +-----+    +-----+    +-----+
 |  A  +--->+  B  +--->+  C  |
 +--+--+    +-----+    +-----+
    ^
head|
    +
    
第一次：
+-----+    +-----+    +-----+
|  A  |    |  B  +--->+  C  |
+--+--+    +--+--+    +-----+
   ^          ^
   |      next|
pre+      head+

第二次：
+-----+    +-----+    +-----+
|  A  <----+  B  |    |  C  |
+-----+    +--+--+    +--+--+
              ^          ^
           pre|      next|
              +      head+

第三次：
+-----+    +-----+    +-----+
|  A  <----+  B  <----+  C  |
+-----+    +-----+    +--+--+
                         ^         ^
                      pre|     next|
                         +     head+

```
#### 实现
```cpp
Node* reverseByLoop(Node *head)
{
    if(head == NULL || head->next == NULL)
        return head;
    Node *pre = NULL;
    Node *next = NULL;
    while(head != NULL)
    {
        next = head->next;

        head->next = pre;
        pre = head;
        head = next;
    }
    return pre;
}
```
###参考
[链表问题集锦](http://wuchong.me/blog/2014/03/25/interview-link-questions/)   
[链表反转问题](http://www.cnblogs.com/kubixuesheng/p/4394509.html)