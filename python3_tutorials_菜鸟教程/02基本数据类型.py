# -*- coding: utf-8 -*-
# coding=gbk  
'''
Created on 2017年8月12日

@author: Chongqing
'''
# Python3 中有六个标准的数据类型：
    # Number（数字）
    # String（字符串） 不可更改
    # List（列表）          可更改
    # Tuple（元组）       不可更改
    # Sets（集合）
    # Dictionary（字典）可更改


# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Set（集合）、Dictionary（字典）。

# 多个变量赋值
a, b, c=1,2,"Chognqing"
print(a,b,c)

# 1,数字 ---int float 布尔值(False, True) 复数J
d,e,f,g = 10, 1.5,True, 4+3j
print(d,e,f,g)

    ## type(),查询变量所指的对象类型，     isinstance
print(type(d),type(e),type(f),type(g))
print(isinstance(a, int))

    # del语句删除一些对象。
    # del var_a, var_b

    # 数值运算
print(2 / 4)  # 除法，得到一个浮点数
print( 2 // 4) # 除法，得到一个整数
print(2 ** 5) # 乘方

# 字符串 String，单引号，双引号，反斜杠转义字符
    # 0 为开始值，-1 为从末尾的开始位置。
    # Python中的字符串不能改变。

str = "Huang"
print(str[0:-2]) # 输出str[0]--str[-3],,,不输出str[-2]
print(str*2)  # 复制2次
print(str+" Chong")# 连接字符串

    # 不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串。。反斜杠(\)可以作为续行符    
print('Huang\Chong')      # ??????????????????????没有转义
print(r'Huang\Chong')
    # Python中的字符串不能改变。

# 列表List 变量[头下标:尾下标] ------------数组--------------------------------------------------------
    # ython字符串不一样的是，列表中的元素是可以改变的：
    #List内置了有很多方法，例如append()、pop()等
list = ['Haung',12, 2.34]
print("list[1:]", list[1:])
list[1:] = [] # 可重置
print(list[1:])     


# Tuple（元组）    
    # 虽然tuple的元素不可改变，但它可以包含可变的对象
tup = (1,"HAung")
# tup[0]=1  #  修改元组元素的操作是非法的

    # 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号


# Set（集合） 顺序真的好好随意
    # 集合（set）是一个无序不重复元素的序列
    # 成员关系测试和删除重复元素
    # 用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim2', 'Mary3', 'Tom', 'Jack5', 'Rose6'}
print(student)   # 输出集合，重复的元素被自动去掉
# 成员测试
if('Rose6' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(b)
 
print(a - b)     # a和b的差集
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素


# Dictionary（字典）
    # 列表是有序的对象结合，字典是无序的对象集合。
    # 字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
dict ={}
dict['name']='Huang'
dict[1]=123

tinydict={'name': 'Chongqing', 'ages': 20}

print(dict["name"])
print(tinydict.keys())
print(tinydict.values())

    # 构造函数 dict() 可以直接从键值对序列中构建字典如下：
print({x: x**2 for x in (2, 4, 6)})

    # Python数据类型转换
s='ChongQIng'
# 将序列 s 转换为一个元组

print(tuple(s))
print(dict(tup)) # 创建一个字典。str 必须是一个序列 (key,value)元组。











