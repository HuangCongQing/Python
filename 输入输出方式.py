# coding=gbk  
'''
Created on 2017年8月14日

@author: 黄重庆
'''

# 接收用户的输入： input()
# 输入格式：str(), str.format() 

# 读写文件
    # f.read()
    # f.readline()

# str_1 = input("Enter a string:")
# str_2 = input("Enter another a string:")


## Output
# print("str_1 is :" + str_1 + ", str_2 is :" + str_2)
# print("str_1 is {} +  str_2 is {}".format(str_1, str_2))


## 读写文件
# 打开一个文件
# f = open("File-test.txt", "w")
f = open("File-test.txt", "r")

# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
str0 = f.read()
print(str0)
str1 = f.tell()
print("字节数：", str1)

# 关闭打开的文件
f.close()


# python文件写入也可以进行网站爬虫,我的python版本是3.6，以下代码是打开project.txt文件，
# 并向里面写入http://www.baidu.com网站代码。
from urllib import request

response1 = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response1.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件

