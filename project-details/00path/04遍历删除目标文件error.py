'''
Description: 删除命令: shutil.rmtree(rm_path)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-08-18 17:54:55
LastEditTime: 2021-08-18 18:24:09
FilePath: /Python/project-details/00path/04遍历删除目标文件.py
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import tqdm as tqdm


def remove_files_by_folder(folder_path):
    # 遍历文件并删除制定文件
    dataset_dirs = folder_path 
    img_list = []
    for dataset_dir in dataset_dirs:
        for root,dirs,files in os.walk(dataset_dir): # #当前目录路径 、#当前路径下所有子目录 数组 和#当前路径下所有非目录子文件  
            # print(root,dirs) # dirs =  ['1', '2', '3', '4', '5', '6', '7']
            # print("files:", files) # #当前路径下所有非目录子文件
            files = ''.join(files)  
            if "pcd" in files:
                print("not remove")
            else:
                shutil.rmtree(rm_path)
            for file in files:
                if(file.split(".")[-1]== "jpg"): # 判断bag]包
                    print(os.path.join(root,file))
                    rm_path = os.path.join(root,file)
                    img_list.append(os.path.join(root,file))
                    # 删除
                    shutil.rmtree(rm_path)

if __name__ == '__main__':
    folder_path = ['/media/hcq/hcq4T/huituo_data_collection/detection/ouster_bagfile_extract/shenbao'] 
    # folder_path = ['/media/hcq/hcq4T/huituo_data_collection/detection/ouster_bagfile_extract/shenbao']  # 20210705Detection_zhunnneg  detection_yimin
    remove_files_by_folder(folder_path)
