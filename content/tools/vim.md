title: "Getting Started"
layout: page
date: 2099-06-02 00:00

#VIM

##大小写转换
```
~            将光标下的字母改变大小写

3~           将光标位置开始的3个字母改变其大小写

g~~          改变当前行字母的大小写

U / u        将可视模式下选择的字母全改成大写/小写

gUU / guu    将当前行的字母改成大写/小写

3gUU / 3guu  将从光标开始到下面3行字母改成大写/小写

gUw / guw    将光标下的单词改成大写/小写

```

##删除
```
g/pattern/d  删除包含特定字符的行

v/pattern/d  删除不包含指定字符的行
```