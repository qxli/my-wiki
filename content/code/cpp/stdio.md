---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#stdio
```
#include <stdio.h>
```

## fgets
```cpp
// char * fgets ( char * str, int num, FILE * stream );

FILE* fp = fopen("myfile.txt", "r");
if(NULL == fp) return -1;
char buf[MAXLINE] = {0};
int i = 1;
while(NULL != fgets(buf, MAXLINE, fp)) {
    fprintf(stdout, "%d, %s", i, buf);
    ++i;
}
fclose(fp);
```