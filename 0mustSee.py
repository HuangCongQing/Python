'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-06-16 17:19:20
@LastEditors: HCQ
@LastEditTime: 2020-06-16 17:42:51
'''
max_epoch = 20
# lr_decays = {i: 0.1**(1/100) for i in range(1, max_epoch)}
# print(lr_decays)
lr_decays = {i: 0.1 ** (1 / 150) for i in range(1, max_epoch)}
print(lr_decays)
# 感觉这就是学习率衰减，比如 max_epoch=20 ，就是每次的lr_decays都是0.1**(1/100)
# 感觉他这是测试调试用的，因为i值没有变化
# https://github.com/HuguesTHOMAS/KPConv-PyTorch/issues/4