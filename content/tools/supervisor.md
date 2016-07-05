title: "Getting Started"
layout: page
date: 2099-06-02 00:00

##安装
```
$ sudo pip install supervisor
```

##生成配置文件
```
$ echo_supervisord_conf > /etc/supervisord.conf
```

##启动supervisord
```
$ supervisord -c /etc/supervisord.conf
```

##增加启动进程
```
; 设置进程的名称，使用 supervisorctl 来管理进程时需要使用该进程名
[program:your_program_name] 
command=python server.py --port=9000
;numprocs=1                 ; 默认为1
;process_name=%(program_name)s   ; 默认为 %(program_name)s，即 [program:x] 中的 x
directory=/home/python/tornado_server ; 执行 command 之前，先切换到工作目录
user=oxygen                 ; 使用 oxygen 用户来启动该进程
; 程序崩溃时自动重启，重启次数是有限制的，默认为3次
autorestart=true            
redirect_stderr=true        ; 重定向输出的日志
stdout_logfile = /var/log/supervisord/tornado_server.log
loglevel=info
```

##supervisorctl 命令
```
# 停止、重启program_name
$ supervisorctl stop program_name
$ supervisorctl start program_name
$ supervisorctl restart program_name

# 重启supervisord
$ supervisorctl reload
```