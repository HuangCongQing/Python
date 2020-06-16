'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-06-16 17:19:20
@LastEditors: HCQ
@LastEditTime: 2020-06-16 17:34:12
'''
max_epoch = 20
# lr_decays = {i: 0.1**(1/100) for i in range(1, max_epoch)}
# print(lr_decays)
lr_decays = {i: 0.1 ** (1 / 150) for i in range(1, max_epoch)}
print(lr_decays)