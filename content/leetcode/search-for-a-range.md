---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
/*
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
*/
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> v = {-1,-1};
        int start = 0;
        int end = 0;
        int low = 0;
        int high = nums.size()-1;
        while(low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        start = low;
        low = 0;
        high = nums.size() -1;
        while(low <= high){
            int mid = (low + high)/2;
            if (nums[mid] <= target){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        end = high;
        if(start <= end){
            v.clear();
            v.push_back(start);
            v.push_back(end);
        }
        return v;
    }
};
```