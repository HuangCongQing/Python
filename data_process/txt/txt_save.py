'''
Description: np.savetxt() 参考：https://www.cnblogs.com/lindaxin/p/8392956.html
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 18:12:31
LastEditTime: 2021-04-13 18:33:08
FilePath: /Python/data_process/txt/txt_save.py
'''
import numpy as np 
l1=np.arange(5) 
l2,l3=l1*2,l1*3 
data = [[  0.,   1.,   2.,   3.,   4.], 
       [  0.,   2.,   4.,   6.,   8.], 
       [  0.,   3.,   6.,   9.,  12.]]
# np.savetxt('/home/hcq/pointcloud/Python/data_process/txt/test.txt', (l1,l2,l3), fmt="%.18f,%.18f,%.18f,%.18f,%.18f", delimiter="\n") 
np.savetxt('/home/hcq/pointcloud/Python/data_process/txt/test.txt', data, fmt="%.18f,%.18f,%.18f,%.18f,%.18f", delimiter="\n") 
#  第一个参数可以指定保存的路径以及文件名，注意指定的文件路径必须存在，它不会为你新建新的文件，会报错。fmt="%.18f,%.18f"指定保存的文件格式，delimiter="\n"表示分隔符