---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```python
class Solution(object):
    def threeSum(self, nums):
        target = 0
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-1, 1, -1):
            if i<n-1 and nums[i] == nums[i+1]:
                continue
            twoRes = self.twoSum(nums, i-1, target-nums[i])
            for one in twoRes:
                one.append(nums[i])
                res.append(one)
        return res

    def twoSum(self, ary, end, target):
        all_res = []
        left = 0
        right = end
        while left < right:
            if ary[left] + ary[right] == target:
                res = []
                res.append(ary[left])
                res.append(ary[right])
                all_res.append(res)
                left += 1
                right -= 1
                while left < right and ary[left] == ary[left-1]:
                    left += 1
                while left < right and ary[right] == ary[right+1]:
                    right -= 1
            elif ary[left] + ary[right] > target:
                right -= 1
            else:
                left += 1
        return all_res
```