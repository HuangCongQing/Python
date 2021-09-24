'''
Description: test
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-11-17 13:50:28
LastEditTime: 2020-11-17 14:02:14
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