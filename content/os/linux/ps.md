---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#ps
##参数

```
-A 显示所有进程
-e 同“-A”
-f 完整格式显示
```

##命令
```
$ ps -ef
UID        PID    PPID      C             STIME   TTY     TIME                 CMD
root     31202   19870      0             22:10     ?     00:00:00             sleep 20
用户uid  进程pid  父进程ppid  使用资源百分比  启动时间  终端    实际使用CPU运作的时间    命令行参数

TTY：该process是在那个终端机上面运作，若与终端机无关，则显示 ?，
另外， tty1-tty6 是本机上面的登入者程序，若为 pts/0 等等的，则表示为由网络连接进主机的程序。
```
