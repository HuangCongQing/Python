'''
Author: your name
https://blog.csdn.net/weixin_44128857/article/details/109308833
Date: 2021-07-30 15:58:22
LastEditTime: 2021-07-30 15:59:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Python/data_process/pcdtxt/pcd2txt.py
'''
import pcl
import numpy as np
single_pcd_points = pcl.load('/home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.pcd')   # 用load_XYZI()可以提取第四维信息，但该信息通常没用
single_pcd_points_np = single_pcd_points.to_array()  #转成numpy格式
# 写入文件
np.savetxt("/home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.txt", single_pcd_points_np,fmt='%f',delimiter=',')  #格式为浮点型，用“，”隔开
# 从文件中取出
points = np.loadtxt('/home/hcq/pointcloud/Python/data_process/data/1597975063.081979.rs-bpearl.txt',delimiter=',')
print("**************")
print("done!")
print(points)
