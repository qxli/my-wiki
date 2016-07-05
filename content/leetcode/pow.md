---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
/*
x^n = x^(n / 2) *  x^(n / 2) * x^(n % 2)
*/
// 递归
class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0) {
            return 1;
        } else if(n > 0) {
            return power(x, n);
        } else {
            return 1 / power(x, -1*n);
        }
    }
private:
    double power(double x, int n) {
        if(n == 0)
            return 1;
        double y = power(x, n/2);
        if(n % 2 == 0) {
            return y * y;
        } else {
            return y * y * x;
        }
    }
};

// 非递归
class Solution {
public:
    double myPow(double x, int n) {
        bool sign = false;
        unsigned int exp = n;
        if(n < 0) {
            exp = -n;
            sign = true;
        }
        double result = 1.0;
        while (exp){
            if (exp & 1) { // 判断奇偶
                result *= x;
            }
            exp >>= 1; // 右移1位等于除以2
            x *= x;
        }
        return sign ? 1/result:result;
    }
};
```