---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#memset

##问题
### 1. 不能对C++类对象或struct对象做memset操作
原因：memset 破坏了内部结构，从而不能正常进行析构操作，最终导致crash