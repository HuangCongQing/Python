# coding=UTF-8
'''
Author: your name
运行命令：python pcd2bin.py convert /home/hcq/pointcloud/Python/data_process/data /home/hcq/pointcloud/Python/data_process/data
Date: 2021-07-28 16:27:26
LastEditTime: 2021-10-21 21:20:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Python/data_process/pcdbin/pcd2bin/pcd2bin.py
'''

import os
import numpy as np
import fire

def read_pcd(filepath):
    lidar = []
    with open(filepath,'r', encoding='utf-8') as f: # encoding='gbk'
        line = f.readline().strip()  # decode('gbk')
        while line:
            linestr = line.split(" ") # -0.015800 -0.000408 0.000000 0.0  = len(linestr) =4
            if len(linestr) == 4: # 判断坐标位置(每行空格分成多多少个)===========================================
                linestr_convert = list(map(float, linestr))
                # linestr_convert.append(0) # intensity补0
                print("linestr_convert: ", linestr_convert)
                lidar.append(linestr_convert)
            # if len(linestr) == 3: # 判断坐标位置(每行空格分成多多少个)===========================================
            #     linestr_convert = list(map(float, linestr))
            #     linestr_convert.append(0) # intensity补0
            #     print("linestr_convert: ", linestr_convert)
            #     lidar.append(linestr_convert)
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
    for file in file_list: # list遍历
        (filename,extension) = os.path.splitext(file) # 文件和扩展名
        if extension=='.pcd': # 判断
            velodyne_file = os.path.join(ori_path, filename) + '.pcd'
            print("============当前读取文件: %+10s =========" %(velodyne_file))
            pl = read_pcd(velodyne_file)
            pl = pl.reshape(-1, 4).astype(np.float32) # 自己设置四列!!!!=================x,y,z,intensity
            print("pl: %s" %(pl))
            velodyne_file_new = os.path.join(des_path, filename) + '.bin'
            pl.tofile(velodyne_file_new)
    
if __name__ == "__main__":
    fire.Fire()    