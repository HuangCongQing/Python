'''
Author: your name
运行命令：python pcd2bin.py convert /home/hcq/pointcloud/Python/data_process/data /home/hcq/pointcloud/Python/data_process/data
Date: 2021-07-28 16:27:26
LastEditTime: 2021-07-28 16:27:27
LastEditors: your name
Description: In User Settings Edit
FilePath: /Python/data_process/pcdbin/pcd2bin.py
'''

import os
import numpy as np
import fire

def read_pcd(filepath):
    lidar = []
    with open(filepath,'r') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            if len(linestr) == 3: # 判断坐标位置(每行空格分成多多少个)===========================================
                linestr_convert = list(map(float, linestr))
                print("linestr_convert: ", linestr_convert)
                lidar.append(linestr_convert)
            line = f.readline().strip()
            # print("line: ", line)
    return np.array(lidar)


def convert(pcdfolder, binfolder):
    current_path = os.getcwd()
    ori_path = os.path.join(current_path, pcdfolder)
    file_list = os.listdir(ori_path)
    des_path = os.path.join(current_path, binfolder)
    if os.path.exists(des_path):
        pass
    else:
        os.makedirs(des_path)
    for file in file_list: 
        (filename,extension) = os.path.splitext(file)
        velodyne_file = os.path.join(ori_path, filename) + '.pcd'
        print("============当前读取文件: %s =========" %(velodyne_file))
        pl = read_pcd(velodyne_file)
        pl = pl.reshape(-1, 4).astype(np.float32)
        velodyne_file_new = os.path.join(des_path, filename) + '.bin'
        pl.tofile(velodyne_file_new)
    
if __name__ == "__main__":
    fire.Fire()    