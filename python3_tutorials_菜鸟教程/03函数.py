'''
Created on 2017年8月12日

@author: Chongqing
'''
# def 函数名（参数列表）:
#     函数体

# 函数调用
    #定义函数
def printme(str):
    "打印任意字符串："
    print(str);
    return;
    # 调用函数
    
print(printme("我要调用函数"))    


# 参数传递
    # 在 python 中，类型属于对象，变量是没有类型的：
    
    # 可更改(mutable)与不可更改(immutable)对象

    # 传不可变对象实例
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2
    # 传可变对象实例
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print ("函数内取值: ", mylist)
   # 不带参数值的return语句返回None
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)


# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
    # ambda的主体是一个表达式，而不是一个代码块
sum = lambda arg1, arg2: arg1+arg2;
print("匿名函数相加后的值：",sum(20,30))

# 变量作用域

x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

        #Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
        # 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的


# global 和 nonlocal关键字

        # 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
        # global修改全局变量 
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print("global关键字声明：",num)
fun1()
        # 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer1():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print("nonlocal:",num)
outer1()
