'''
Description: np.savetxt()
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 18:12:31
LastEditTime: 2021-04-13 18:31:09
FilePath: /Python/data_process/txt/txt_save.py
'''
import numpy as np 
l1=np.arange(5) 
l2,l3=l1*2,l1*3 
np.savetxt('/home/hcq/pointcloud/Python/data_process/txt/test.txt', (l1,l2,l3), fmt="%.18f,%.18f,%.18f,%.18f,%.18f", delimiter="\n") 