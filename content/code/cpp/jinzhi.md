---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#不同进制转化
##十进制 <--> 二进制
```cpp
std::string int2bin(int num) {
    std::string ret;
    while(num>0){
        int c = num % 2;
        ret.insert(ret.begin(), c+'0');
        num /=2;
    }
    return ret;
}

int bin2int(std::string s) {
    int ret = 0;
    for(int i=0; i<s.size(); i++) {
        int n = s[i] - '0';
        ret = ret*2 + n;
    }
    return ret;
}
```
##十进制 <--> 八进制
```cpp
std::string int2oct(int num) {
    std::string ret;
    while(num>0) {
        int c = num % 8;
        ret.insert(ret.begin(), c+'0');
        num /= 8;
    }
    return ret;
}

int oct2int(std::string s) {
    int ret = 0;
    for(int i=0; i<s.size(); i++) {
        int n = s[i] -'0';
        ret = ret*8 +n;
    }
    return ret;
}
```
##十进制 <--> 十六进制
```cpp
std::string int2hex(int num) {
    std::string ret;
    while(num>0) {
        int c = num % 16;
        char ch = '0' + c;
        if(c > 9) {
            ch = 'A' + c % 9 - 1;
        }
        ret.insert(ret.begin(), ch);
        num /= 16;
    }
    return ret;
}

int hex2int(std::string s) {
    int ret = 0;
    for(int i=0; i<s.size(); i++) {
        int n = s[i] - '0';
        if(n > 9) {
            n = s[i] - 'A' + 1 + 9;
        }
        ret = ret*16 + n;
    }
    return ret;
}
```