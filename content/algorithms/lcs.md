---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#最长公共子串
##穷举法

时间复杂度：O(n^2*k)  
空间复杂度：O(1)

```cpp
int comlen(char* p, char* q){
    int len = 0;
    while(*p && *q && *p++ == *q++) {
        ++len;
    }
    return len;
}

int lcs_1(const char* a, int asize, const char* b, int bsize){
    int maxlen =0, maxindex = 0;
    char* p = (char*)a;
    char* q = (char*)b;
    for(int i = 0; i<asize; i++){
        for(int j = 0; j<bsize; j++){
            int len = comlen(&p[i], &q[j]);
            if(len > maxlen){
                maxlen = len;
                maxindex = i;
            }
        }
    }
    printf("maxlen=%d\n", maxlen);
    printf("maxindex=%d\n", maxindex);
    return maxlen;
}
```
##动态规划

时间复杂度：O(n^2)  
空间复杂度：O(n)

```cpp
int lcs_2(const char* a, int asize, const char* b, int bsize) {
    int dp[64] = {0};
    int maxlen =0, maxindex = 0;
    for(int i = 0; i < asize; ++i) {
        for(int j = bsize; j >= 0; --j) {
            if(a[i] == b[j]) {
                if(i == 0 || j == 0) {
                    dp[j] = 1;
                } else {
                    dp[j] = dp[j-1] + 1;
                }
                if(dp[j] > maxlen) {
                    maxlen = dp[j];
                    maxindex = i + 1 - maxlen;
                }
            } else {
                dp[j] = 0;
            }
        }
    }
    printf("maxlen=%d\n", maxlen);
    printf("maxindex=%d\n", maxindex);
    return 0;
}
```
[最长公共子串问题的几种算法](http://www.devhui.com/2015/04/21/Longest-Common-Substring/)