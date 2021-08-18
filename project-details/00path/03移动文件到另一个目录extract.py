'''
Description: 移动文件到另一个目录
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-08-17 16:16:58
LastEditTime: 2021-08-18 17:56:04
FilePath: /Python/project-details/00path/extract.py
'''
import os
import shutil
from tqdm import tqdm
def main():
    lis = os.listdir('./')
    folders = []
    '''find root folders'''
    for i in lis: 
        if 'py' not in i:
            folders.append(i)
    '''start looping'''
    for folder in tqdm(folders):
        path = './' + folder + '/'
        bags = os.listdir(path)
        for bag in bags:
            bag_path = path+bag+'/'

            types = ['image/', 'pointcloud/os_cloud_node/']
            for t in types:
                if os.path.exists(bag_path+t):
                    files = os.listdir(bag_path+t)
                    for file in files:
                        shutil.move(bag_path+t+ file, bag_path) #move images
                else:
                    print('cannot find {} folder at {}'.format(t, bag_path))

            # if os._exists(bag_path+'os_cloud_node'):




if __name__ == '__main__':
    main()