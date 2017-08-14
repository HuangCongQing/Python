# encoding: utf-8
'''
Created on 2017年8月14日

@author: hasee
'''
# 可复用
# Python 中的函数可以像普通变量一样当做参数传递给另外一个函数
#　装饰器的作用就是为已经存在的对象添加额外的功能。
# def foo():
#     print("foo")
# 
# def bar(func):
#     func()
# 
# bar(foo)

# 简单装饰器
# 
# def use_logging(func):
# 
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
#     return wrapper
# 
# def foo():
#     print('i am foo')
# 
# foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
# foo()                   # 执行foo()就相当于执行 wrapper()

# @ 语法糖
import time  
   
def timeit(func):  
    def wrapper():  
        start = time.clock()  
        func()  
        end =time.clock()  
        print ('used:'), end - start  
    return wrapper  
  
@timeit  
def foo():  
    print ('in foo()')  
   
foo()  