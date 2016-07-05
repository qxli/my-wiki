---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#samba

###安装samba
```
$ yum -y install samba samba-client
```

###添加用户
```
$ smbpasswd -a newuser
```

###重启服务
```
$ /etc/init.d/smb restart
```
