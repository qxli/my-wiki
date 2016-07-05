title: "Getting Started"
layout: page
date: 2099-06-02 00:00

#rpm

##解压
RPM包是使用cpio格式打包的，因此可以先转成cpio然后解压
```
$ rpm2cpio foo.rpm | cpio -div
```

##查看已安装的rpm包
```
$ rpm -qa
```