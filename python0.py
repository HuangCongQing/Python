# -*- coding: UTF-8 -*-
'''
Created on 2017年8月12日

@author: Chongqing
'''
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

# 默认情况下，Python 3 源码文件以 UTF-8 编码
print("Hello Python35 Chongqing 重庆")
import os
import requests # import 的 Package

list=[1, 2, 3, "重庆"]
print('list_' + str(list))

print (os.getcwd())
r = requests.get('http://www.baidu.com')
print(r.url)
print(r.encoding)
# print(r.text)