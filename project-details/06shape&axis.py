'''
Description: shpae&axis
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-11 15:02:28
LastEditTime: 2022-08-06 22:48:17
FilePath: /Python/project-details/06shape&axis.py
'''

import numpy as np

# shape
a=np.array(
            [ 
            [ [1,2,3],
            [2,3,4]],

            [[2,3,4],
            [1,2,1]]
            ])
print(a)
# print(a.shape, a.shape[0]) # a.shape=(2,2,3)，维度对应的下标为(0,1,2) 其中0维->1, 1->2 , 2->3
# 以sum为例，先记住：axis=几，几对应的shape就消失，如axis=0，之后的shape为(2,3)；axis=2,则变成（2,2）

# axis
b = np.sum(a, axis=0) # (2,3)
print("axis=0: ",b)
f = np.sum(a, axis=1)
print("axis=1: ",f) # (2,1,3)

d=[[1,2,3],[4,5,6]]
print("二维数组：",d)
c = np.sum(d, axis=0) # 第一行+第二行
print(c)

