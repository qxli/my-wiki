---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

---

最笨的方法就是两个循环，算出所有等于9的数，题目中也没有说是否是有序的，如果没有顺序可以先排下序，排序后，可以只循环一次，利用两个指针，一个在开始，另一个在结尾，下面就是这个方法。

```python
def twoSum(ary, target):
    ary.sort()
    left = 0
    right = len(ary) -1
    res = []
    while left<right:
        if ary[left] + ary[right] == target:
            res.append(ary[left])
            res.append(ary[right])
            break
        elif ary[left] + ary[right] > target:
            right -= 1
        else:
            left += 1
    return res
```

---
下面这个算法，是空间换时间的一种解法，利用一个字典去当前元素和目标值的差值，只用循环一遍就可以找到。

```python
def twoSum(ary, target):
    m = {}
    res = []
    for i in range(0, len(ary)):
        if not m.has_key(ary[i]):
            m[target - ary[i]] = i
        else:
            res.append(ary[m[ary[i]]])
            res.append(ary[i])
            break
    return res
```