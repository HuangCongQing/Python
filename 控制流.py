# coding=gbk  
'''
Created on 2017年8月14日

@author: 黄重庆
'''
# if&for
# while && range
# break && contine && pass

# if语句
    # Python 中用 elif 代替了 else if
    # 在Python中没有switch – case语句

    # 以下实例 x 为 0-99 取一个数,y 为 0-199 取一个数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y。
import random

x = random.choice(range(100))
y = random.choice(range(100))

if x>y:
    print("x:",x)
elif x==y:
    print("x+y:",x+y)
else:
    print("y:",y)

#  for循环
    # for可以遍历任何序列的项目，如一个列表或者一个字符串
print("for循环----------------------------------")
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")




# while语句

    # 在Python中没有do..while循环。
    # 可以使用 CTRL+C 来退出当前的无限循环。
    
    # while 循环使用 else 语句
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")


## range()
    #需要遍历数字序列，可以使用内置range()函数。它会生成数列
print("range()-----------------------------------")    
for i in range(5):
    print(i)

    # 也可以使range以指定数字开始并指定不同的增量
for i in range(0, 10, 3) :
    print(i)
    
    # 可以结合range()和len()函数以遍历一个序列的索引
    
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
     print(i, a[i])

    # 使用range()函数来创建一个列表：
    
m=list(range(5))
print(m)

    # 求和
sum = sum(range(101))
print("求和1-100：",sum)

# break和continue语句及循环中的else子句


# pass 语句
    # Python pass是空语句，是为了保持程序结构的完整性。
    # pass 不做任何事情，一般用做占位语句




