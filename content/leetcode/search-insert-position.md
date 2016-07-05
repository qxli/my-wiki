---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
/*
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        while(low <= high){
            int mid = low + ((high - low)/2);
            if(target < nums[mid]) {
                high = mid - 1;
            } else if (target > nums[mid]){
                low = mid + 1;
            } else {
                return mid;
            }
        }
        return low;
    }
};
```