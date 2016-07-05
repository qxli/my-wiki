---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
/*
Implement int sqrt(int x).

Compute and return the square root of x.
*/
class Solution {
public:
    int mySqrt(int x) {
        int l = 1;
        int r = x/2+1;
        while(l <= r){
            int mid = (l + r)/2;
            if(x/mid>=mid && x/(mid+1)< mid+1){
                return mid;
            }
            if(x/mid < mid){
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return 0;
    }
};
```