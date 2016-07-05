---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

## 示例
### 客户端
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define MAXLINE 4096

int main(int argc, char** argv) {
    int sockfd = 0;
    int n = 0;
    char recvline[MAXLINE] = {0};
    char sendline[MAXLINE] = {0};
    struct sockaddr_in servaddr;

    if(argc != 2) {
        printf("usage: ./clinet ipaddr\n");
        return -1;
    }

    if( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("create socket error\n");
        return -1;
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(6666);
    if( inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0) {
        printf("inet_pton error\n");
        return -1;
    }
    if(connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0) {
        printf("connect error\n");
        return -1;
    }

    printf("send msg to server\n");
    fgets(sendline, MAXLINE, stdin);
    if(send(sockfd, sendline, strlen(sendline), 0) < 0) {
        printf("send error\n");
        return -1;
    }
    close(sockfd);
    return 0;
}
```
### 服务端
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define MAXLINE 4096

int main(int argc, char** argv) {
    int listenfd = 0;
    int connfd = 0;
    struct sockaddr_in servaddr;
    char buff[MAXLINE] = {0};
    int n;

    if((listenfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        printf("create socket error\n");
        return -1;
    }
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(6666);

    if(bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) == -1) {
        printf("bind socket error:%s\n", strerror(errno));
        return -1;
    }

    if(listen(listenfd, 10) == -1) {
        printf("listen socket error\n");
        return -1;
    }
    printf("========waiting for client============\n");
    while(1) {
        if((connfd = accept(listenfd, (struct sockaddr*)NULL, NULL)) == -1) {
            printf("accept socket error\n");
            continue;
        }
        n = recv(connfd, buff, MAXLINE, 0);
        buff[n] = '\0';
        printf("client: %s\n", buff);
        close(connfd);
    }
    close(listenfd);
    return 0;
}
```