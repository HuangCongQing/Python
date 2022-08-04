<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Date: 2020-06-16 17:18:05
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-08-04 23:58:51
-->

# Python

Python学习
想在哪个文件夹下打开jupyter，就在相对应的文件夹下打开终端
运行
```jupyter-notebook```

* modules：https://github.com/HuangCongQing/python-libraries
  * https://pypi.org
  * https://www.lfd.uci.edu/~gohlke/pythonlibs/



* [json转txt（点云标注）](./data_process\json\json2txt_lidar_rename.py)
* [json转txt](./data_process\json\json2txt_lidar_rename.py)

### Tutorial

* 安装requirement.txt中的包
  `pip3 install -r requirement.txt`

### [python3_tutorials_菜鸟教程](./python3_tutorials_菜鸟教程)

学习网站：http://www.runoob.com/python3/python3-tutorial.html

### [python3_tutorials_莫凡](./python3_tutorials_莫凡)

学习视频网址：https://www.bilibili.com/video/av16926522/?p=2

### [北邮《Python编程与实践》课程 (2020)](https://github.com/fly51fly/Practical_Python_Programming)

学习视频网址：https://www.bilibili.com/video/BV1b7411N7P2

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

* `pip list`

该命令查看的是Python安装的第三方模块。

[self](https://www.cnblogs.com/masbay/p/10688541.html)

## 命令行

* 从shell中退出python命令：是. ... 从shell（终端）中退出python：. 1、输入命令行：$ exit(). 2、快捷键： ctrl+Z.

### issues

1. [同时装了Python3和Python2，怎么用pip？](https://github.com/HuangCongQing/Python/issues/3)
2. [ImportError: DLL load failed: 找不到指定的模块。](https://github.com/HuangCongQing/Python/issues/4)
3. [安装Python模块时，报错[error] Microsoft Visual C++ 14.0 is required](https://github.com/HuangCongQing/Python/issues/5)
4. [出现ReadTimeoutError(self._pool, None, 'Read timed out.')](https://github.com/HuangCongQing/Python/issues/6)
5. [python 各种包下载大全网址](https://github.com/HuangCongQing/Python/issues/7)
6. [如何简单地理解Python中的if __name__ == '__main__'](https://github.com/HuangCongQing/Python/issues/8)
7. [python中出现IndentationError:unindent does not match any outer indentation level错误](https://github.com/HuangCongQing/Python/issues/9)
8. [SyntaxError: invalid syntax](https://github.com/HuangCongQing/Python/issues/10)
9. [TypeError: slice indices must be integers or None or have an __index__ method](https://github.com/HuangCongQing/Python/issues/11)
10. [UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 115: ille](https://github.com/HuangCongQing/Python/issues/12)
11. [打开Anaconda Prompt 显示显示python已停止工作](https://github.com/HuangCongQing/Python/issues/13)
12. [NoPackagesFoundError: Package missing in current win-64 channels: - cudatoolkit 7.5 2](https://github.com/HuangCongQing/Python/issues/14)

## 学习资料及视频

* Python数据分析 升级版https://www.julyedu.com/my/courses
* Python网络爬虫实战https://edu.hellobi.com/course/81/lessons
* 廖雪峰Python 3https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
* lambda: [python lambda表达式](https://www.cnblogs.com/mxh1099/p/5386529.html)
