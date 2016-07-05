---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#date

###获得当前时间
```
$ date '+%Y%m%d%H%M%S'
```

###获得前一天时间
```
$ date -d '-1 day' '+%Y%m%d%H%M%S'
```

###获得当前时间戳
```
$ date +%s
```

###获得指定时间时间戳
```
$ date -d "2014-10-21 15:45:00" +%s
```

###将时间戳转为标准时间格式
```
$ date -d "@1413877500" '+%Y%m%d%H%M%S'
```