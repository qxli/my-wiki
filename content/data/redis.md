tags: 
title: data/redis

#redis

### 批量删除数据库里的key
```
$ redis-cli -h 127.0.0.1 -p 5629 -a '123456' keys "token_*" | xargs redis-cli -h 127.0.0.1 -p 5629 -a '123456' del
```

### 连接redis