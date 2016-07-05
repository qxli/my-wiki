---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#排序算法
![](http://ww1.sinaimg.cn/large/81b78497jw1emncvtdf1qj20u10afn0r.jpg?600*600)
##快速排序
1.从数列中挑出一个元素作为基准数。  
2.分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。  
3.再对左右区间递归执行第二步，直至各区间只有一个数。  
  
采用分治法，因为最左边的元素作为比较key，因此移动的时候要从最右边开始移动，当左右汇合后，需要将该元素与key进行交换

```python
def sort(ary):
    return quick_sort(ary, 0, len(ary)-1)

def quick_sort(ary, left, right):
    if left < right:
        mid = partion(ary, left, right)
        quick_sort(ary, left, mid-1)
        quick_sort(ary, mid+1, right)
    return ary

def partion(ary, left, right):
    p = left
    key = ary[left]
    while left < right:
        while left < right and ary[left] <= key:
            left += 1
        while left < right and ary[right] >= key:
            right -=1
        ary[left],ary[right] = ary[right],ary[left]
    ary[left],ary[p] = ary[p],ary[left]
    return left
```

##堆排序
堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。

二叉堆具有以下性质：

父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。
```python
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break
```

[坐在马桶上看算法：快速排序](http://developer.51cto.com/art/201403/430986.htm)   
[经典排序算法总结与实现](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/)