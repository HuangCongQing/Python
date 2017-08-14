# Python
Python学习
 
* 解决Python代码编码问题  Non-UTF-8 code starting with '\xc4' in file
导致出错的根源就是编码问题。
解决方案是：
     在程序最上面加上：
```
# coding=gbk  
```

* Python 报错 TypeError: 'str' object is not callable
```
page = fi.write(str(response1.read()))  
```

原因是我的一个变量名叫str和python api的某个str函数名一样，导致

检查你的代码中变量的名字，看有没有变色的，就是设别为底层函数的即可

## 命令行
*  从shell中退出python命令：是. ... 从shell（终端）中退出python：. 1、输入命令行：$ exit(). 2、快捷键： ctrl+Z. 
