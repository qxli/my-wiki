---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#mysql

##客户端使用方法
###登陆
```
$ mysql -h192.168.1.xx -P3306 -u用户名 -p密码 -D数据库名字
```
**-p和密码之间没有空格可以加引号**，或者，在~/.my.cnf中添加如下配置可以自动登录
```
[client]
user=userll
password=C1L9u5cIhUbz
```

###执行语句
```
mysql -e "show databases"
mysql -D db_flow -e "show tables"
```

##语法
###插入
```
#单条
INSERT INTO table_name VALUES (value1, value2,....)
INSERT INTO table_name SET col_name=value1, col_name=value2, ... 

#批量
INSERT INTO `insert_table` (`datetime`, `uid`, `content`, `type`) 
VALUES ('0', 'userid_0', 'content_0', 0), ('1', 'userid_1', 'content_1', 1);
```

###查询
####distinct
```
  #返回记录不同的id的具体值
$ SELECT DISTINCT id FROM tablename;
```
####count
```
  #返回表的记录总数
$ SELECT count(*) FROM tablename
```
####limit
```
#返回前几条或者中间某几行数据
$ SELECT * FROM table LIMIT 5
$ SELECT * FROM table LIMIT 5,10
```

###创建索引
```
$ alter table table_test add index index_test1(name);
```
####联合索引的好处

- "一个顶三个"。建了一个(a,b,c)的复合索引，那么实际等于建了(a),(a,b),(a,b,c)三个索引，因为每多一个索引，都会增加写操作的开销和磁盘空间的开销。对于大量数据的表，这可是不小的开销！
- 覆盖索引。同样的有复合索引（a,b,c），如果有如下的sql: select a,b,c from table where a=1 and b = 1。那么MySQL可以直接通过遍历索引取得数据，而无需回表，这减少了很多的随机io操作。减少io操作，特别的随机io其实是dba主要的优化策略。所以，在真正的实际应用中，覆盖索引是主要的提升性能的优化手段之一
- 索引列越多，通过索引筛选出的数据越少。有1000W条数据的表，有如下sql:select * from table where a = 1 and b =2 and c = 3,假设假设每个条件可以筛选出10%的数据，如果只有单值索引，那么通过该索引能筛选出1000W*10%=100w 条数据，然后再回表从100w条数据中找到符合b=2 and c= 3的数据，然后再排序，再分页；如果是复合索引，通过索引筛选出1000w *10% *10% *10%=1w，然后再排序、分页，哪个更高效，一眼便知

###导出sql
```
$ mysqldump -ukxtserver -h192.168.200.164 -p3306 -p'kxt4787f#16' -p db_fans_opertree > 1.txt
```

##QA
###解决输出中文乱码
```
$ SET NAMES UTF8
```

## 参考
[mysql 创建索引和删除索引](http://www.cnblogs.com/IT-Monkey/p/3293131.html)