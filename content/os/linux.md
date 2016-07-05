---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

#linux
##命令   
### 文本相关  

- [sed](/os::linux::sed)　[cat](/os::linux::cat)　[wc](/os::linux::wc)　[grep](/os::linux::grep)　[awk](/os::linux::awk)　[uniq](/os::linux::uniq)　[sort](/os::linux::sort)　[split](/os::linux::split)

### 系统相关

- [ssh](/os::linux::ssh)　[kill](/os::linux::kill)　[du](/os::linux::du)　[watch](/os::linux::watch)　[lsof](/os::linux::lsof)　[ps](/os::linux::ps)　[crond](/os::linux::crond)　[date](/os::linux::date)

### 网络相关

- [curl](/os::linux::curl)


### 文件相关

- [ls](/os::linux::ls)　[ln](/os::linux::ln)　[find](/os::linux::find)


##操作

- [设置时区](/os::linux::set-time-zone)
- [设置samba](/os::linux::samba)

##其他
###查看进程打开的文件
```ls -hlrt /proc/25568/fd```

##快捷键
```
ctrl+a:光标移到行首。  
ctrl+b:光标左移一个字母  
ctrl+c:杀死当前进程。  
ctrl+d:退出当前 Shell。  
ctrl+e:光标移到行尾。  
ctrl+h:删除光标前一个字符，同 backspace 键相同。  
ctrl+k:清除光标后至行尾的内容。  
ctrl+l:清屏，相当于clear。  
ctrl+r:搜索之前打过的命令。会有一个提示，根据你输入的关键字进行搜索bash的history  
ctrl+u: 清除光标前至行首间的所有内容。  
ctrl+w: 移除光标前的一个单词  
ctrl+t: 交换光标位置前的两个字符  
ctrl+y: 粘贴或者恢复上次的删除  
ctrl+d: 删除光标所在字母;注意和backspace以及ctrl+h的区别，这2个是删除光标前的字符  
ctrl+f: 光标右移  
ctrl+z : 把当前进程转到后台运行，使用’ fg ‘命令恢复。比如top -d1 然后ctrl+z ，到后台，然后fg,重新恢复
```