'''
Description:  # 遍历文件并删除指定文件（只保存pcd的，不要只带有jpg的）
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-08-18 19:29:19
LastEditTime: 2021-08-18 20:11:31
FilePath: /Python/project-details/00path/04_01删除文件filter.py
'''
import os
import shutil
from tqdm import tqdm
def filter(path):
    roots = os.listdir(path)
    folders = []
    '''bfs traverse the folders'''
    for i in roots:
        if 'py' not in i:
            folders.append(i)

    for folder in tqdm(folders):
        folder_path = path+'/'+folder+'/'
        second = os.listdir(folder_path)
        for s in second:
            second_path = folder_path+s+'/'
            bags = os.listdir(second_path)
            black_list = []
            for bag in bags:
                bag_path = second_path+bag+'/'
                files = os.listdir(bag_path)
                files = ''.join(files)
                if('pcd' not in files):
                    black_list.append(bag_path)
            
            # for l in black_list:
            #     shutil.rmtree(l)

print('process finished')

if __name__ == '__main__':
    filter('/media/hcq/hcq4T/huituo_data_collection/detection/ouster_bagfile_extract/shenbao')
            
    
