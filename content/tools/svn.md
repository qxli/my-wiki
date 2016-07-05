title: "Getting Started"
layout: page
date: 2099-06-02 00:00

#SVN

##revert
###改动没有被提交的修改
```
$ svn revert [-R] something
```

##switch
###切换资源库或分支
```
# 切换资源库
$ svn sw --relocate svn://org svn://new .

# 切换分支
$ svn sw svn://branch
```