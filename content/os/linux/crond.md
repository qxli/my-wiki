---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#计划任务

```
在/etc/crontab添加

*  *  *  *  *  root sh /tmp/test.sh
分 时 日 月 周  用户  命令
```
### 每两小时执行
```
0 */2 * * * root sh xx.sh
```

### 每5分钟执行
```
*/5 * * * * root sh xx.sh
```