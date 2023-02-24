'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-08-06 23:49:37
LastEditTime: 2023-02-24 16:24:01
FilePath: /Python/类和对象/class.py
'''

# 类的创建
class Student(object):
    count = 0  # 类属性

    def __init__(self, name, age):  # __init__为类的构造函数
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    def output(self):  # 实例方法
        print(self.name)
        print(self.age)


if __name__ == '__main__':
    stu1 = Student('Zhangsan', 18)  # 使用Student类对象stu1
    print("stu1.name = %s" % (stu1.name,))  # 利用对象stu1获取对象属性name。输出stu1.name = Zhangsan
    print("stu1.age = %d" % (stu1.age,))  # 利用对象stu1获取对象属性age。输出stu1.age = 18
    stu1.output()  # 利用对象stu1调用output方法。