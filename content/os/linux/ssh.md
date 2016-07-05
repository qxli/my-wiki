---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#ssh

##通过ssh连接远程机器  

 - `$ ssh user@host`  
*默认端口22，可省略* 

 - `$ ssh -p 2222 user@host`  
*指定端口连接*

##无密码登陆

 - `$ ssh-keygen`  
*第一步，生成密钥，一路回车就行*  

 - `$ ssh-copy-id -i ~/.ssh/id_ras.pub user@host`  
*第二步，将公钥id_ras.pub拷贝到目标机器上，提示会输入密码*  

 - `$ ssh-copy-id -i ~/.ssh/id_ras.pub '-p 2222 user@host'`   
*如果需要指定端口，需要加引号*   


##问题

####1. Address X.X.X.X maps to localhost, but this does not map back to the address - POSSIBLE BREAK-IN ATTEMPT! 

```
$ vim /etc/ssh/ssh_config
GSSAPIAuthentication no
```

####2.Write failed: Broken pipe

```
#方法一：如果您有多台服务器，不想在每台服务器上设置，只需在客户端的 ~/.ssh/ 文件夹中添加 config 文件，并添加下面的配置：
ServerAliveInterval 60
#方法二：如果您有多个人管理服务器，不想在每个客户端进行设置，只需在服务器的 /etc/ssh/sshd_config 中添加如下的配置：
ClientAliveInterval 60
#方法三：如果您只想让当前的 ssh 保持连接，可以使用以下的命令：
$ ssh -o ServerAliveInterval=60 user@sshserver
```