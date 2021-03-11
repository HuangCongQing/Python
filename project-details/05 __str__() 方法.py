'''
Description:  __str__() 方法  https://www.runoob.com/note/41154
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-11 14:44:40
LastEditTime: 2021-03-11 14:45:06
FilePath: /Python/project-details/05 __str__() 方法.py
'''
class Cat:
    """定义一个猫类"""
 
    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        # self.name = "汤姆"
        # self.age = 20
        self.name = new_name
        self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
        # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量
 
    def __str__(self):
        """返回一个对象的描述信息"""
        # print(num)
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)
 
    def eat(self):
        print("%s在吃鱼...." % self.name)
 
    def drink(self):
        print("%s在喝可乐..." % self.name)
 
    def introduce(self):
        # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
        # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))
 
# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)