#!/usr/local/bin/python2.7
# encoding: utf-8
'''
面向对象编程ObjectOriented -- shortdesc

面向对象编程ObjectOriented is a description

It defines classes_and_methods

@author:     ������

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    1756260160@qq.com
@deffield    updated: Updated
'''
# 此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
# 类的私有属性和方法
# __private_attrs：_private_method  两个下划线开头，声明该属性//////方法为私有，不能在类地外部被使用或直接访问

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        """self代表类的实例，而非类"""
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5

# 类的方法
#类定义
class people1:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people1('重庆',21,68)
p.speak()


# 继承
 
#类定义
class people2:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people2):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people2.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
 
s = student('ken',10,60,3)
s.speak()

# 多继承

#类定义
class people3:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student3(people3):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people3.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,student3):
    a =''
    def __init__(self,n,a,w,g,t):
        student3.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("重庆",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法





# 方法重写

class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法


# 类的私有属性和方法 
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量













