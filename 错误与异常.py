# coding=gbk  
'''
Created on 2017年8月14日

@author: hasee
'''
# 语法错误  syntax errors&& 异常Exceptions

# while True  print("语法错误")
# print(8/0)



    
    # while True:
    #         try:
    #             x = int(input("Please enter a number: "))
    #             break
    #         except ValueError:
    #             print("Oops!  That was no valid number.  Try again   ")
        
            
    # 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
#     except (RuntimeError, TypeError, NameError):
#         pass


    # import sys
    # 
    # try:
    #     f = open('myfile.txt')
    #     s = f.readline()
    #     i = int(s.strip())
    # except OSError as err:
    #     print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise
            
# 抛出指定异常
    # Python 使用 raise 语句抛出一个指定的异常。
    
# raise NameError('HiThere')
    
    
#　定义清理行为
    # try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
#      
     
# 预定义的清理行为

for line in open("File-test.txt"):
    print(line, end="")
    
    # 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法: 
with open("File-test.txt") as f:
    for line in f:
        print(line, end="")



    
    
    
    
    
    
    
    
    