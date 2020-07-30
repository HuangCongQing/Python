'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-30 11:59:14
@LastEditors: HCQ
@LastEditTime: 2020-07-30 12:12:38
'''

# 整数字符串 list(map(int,list1))
list1 = ['-1', '-1', '-1', '-1'] 
print(list(map(int,list1)) ) # ValueError: invalid literal for int() with base 10: '-1.0000'
# 或者
nums = [int(num) for num in list1]

## 小数 list(map(flaot,list1))

list2 = ['-1.0000', '-1.0000', '-1.0000', '-1.0000'] 
nums = [float(num) for num in list2]
print(list(map(float,list2)))
print(nums)
