---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#查找
##二分查找
```python
def bsearch(ary, val):
    low = 0
    high = len(ary) - 1
    while low <= high:
        mid = low + ((high - low) >> 1) # 防止low和high过大溢出
        if ary[mid] > val:
            high = mid - 1
        elif ary[mid] < val:
            low = mid + 1
        else:
            return mid
```