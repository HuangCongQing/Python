'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-06-16 17:19:20
@LastEditors: HCQ
@LastEditTime: 2020-07-05 18:34:20
'''
max_epoch = 20
# lr_decays = {i: 0.1**(1/100) for i in range(1, max_epoch)}
# print(lr_decays)
lr_decays = {i: 0.1 ** (1 / 150) for i in range(1, max_epoch)}
print(lr_decays)
# 感觉这就是学习率衰减，比如 max_epoch=20 ，就是每次的lr_decays都是0.1**(1/100)
# 感觉他这是测试调试用的，因为i值没有变化
# https://github.com/HuguesTHOMAS/KPConv-PyTorch/issues/4


seq_dets = [
[ 0.0000000e+00  2.0000000e+00  2.9831250e+02  1.3530800e+01  -2.1125000e+00 -1.7867000e+00]
[ 0.0000000e+00  2.0000000e+00  1.0504751e+03  1.8412500e+01  -1.0050000e-01 -7.3910000e-01]
[ 0.0000000e+00  2.0000000e+00  3.6472740e+02  3.2821100e+01 -1.0285000e+00 -7.5820000e-01]
  ]
print(int(seq_dets[:,0].min()), int(seq_dets[:,0].max()) + 1)