title: "Getting Started"
layout: page
date: 2099-06-02 00:00

##简介

- Git是目前世界上最先进的分布式版本控制系统（没有之一）。

##操作
### 更改用户配置

- `$ git config --global user.name "John Doe"`
- `$ git config --global user.email johndoe@example.com`
- `$ git config --global push.default simple`


### 从远端克隆一个本地库

- `git clone username@host:/path/to/repository`  


### 提交修改

- `git add file`  
*把它们添加到暂存区*

- `$ git commit -m "代码提交信息"`  
*改动已经提交到了 HEAD，但是还没到你的远端仓库。*

- `$ git push origin master`  
*Git 会自动为你将此远程仓库命名为 origin，将这些改动提交到远端仓库,可以把 master 换成你想要推送的任何分支。*

### 创建分支

- `git checkout -b feature_x`  
*创建一个叫做“feature_x”的分支，并切换过去*

- `git branch -d feature_x`  
*把新建的分支删掉*

### 更新代码

- `git pull`  
*更新你的本地仓库至最新改动*

### 查看状态

- `git status`

### 删除文件

- `git rm file`

### 版本回退

- `git reset --hard commit_id`

### 撤销修改

- `git checkout -- file`  


##问题
1.执行git push有如下提示
```
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)
```
解决办法：`$ git config --global push.default simple`
##参考资料

- [Git 官网](http://git-scm.com)
- [Git - 简易指南](http://www.bootcss.com/p/git-guide/)
- [Git教程](http://lvwzhen.github.io/Git-Tutorial/)
