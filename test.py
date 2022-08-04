'''
Description: test
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-11-17 13:50:28
LastEditTime: 2022-04-25 14:52:36
FilePath: /Python/test.py
'''
import socket

print(socket.gethostname())  # hcq-G5-5590

import numpy as np

a = np.arange(12).reshape(1,3,4)
print(a)
# print(a>4)
# print(a[a>4])
print(a[:, :, 3]>8)
print(a[a[:, :, 3]>8])


import random
arr = ["2022-12", "2022-33", '3023-12', '2343-24']
print("before: ", arr)
random.shuffle(arr)
print("after: ", arr)