
'''
Description:
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-01-20 16:20:06
LastEditTime: 2022-01-21 10:55:10
FilePath: /Python/data_process/json/json2txt_lidar.py
'''

import os
import json
import numpy as np
from  tqdm import tqdm


json_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_data/'  # json文件路径
out_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_result/'  # 输出的 txt 文件路径


# livox
json_livox_dirs = []
json_livox = ['/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-1', '/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-2']
# 输出
out_dir_livox = '/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/livox_result/'



for i in json_livox:
    # path_paths =
    # for path_path in os.listdir(path):
    #     for path in json_livox + path_path:
    #         file_path =  json_livox + path_path + path
    for j in os.listdir(i):
        list_json = os.listdir('%s/%s/livox/'%(i,j))
        # 排序（转数字排序，再转字符）
        flielist = [int(x.split('.')[0]) for x in list_json]
        flielist.sort()
        flielist = ['%06d.json' % x for x in flielist]  # 数字转成字符00000.json
        for k in list_json:
            # json.load(open('%s/%s/livox/%s' % (i,j,k)))
            json_livox_dirs.append('%s/%s/livox/%s' % (i,j,k))
            # '/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-1/_2021-10-25-11-40-50/livox/000002.json'
# print(len(json_livox_dirs))

def get_json(json_file, out_dir, filename):
    # 读取 json 文件数据
    with open(json_file, 'r') as load_f:
        content = json.load(load_f)

    # 修改输出文件名
    # filename = 0
    # filename = '%06d' % filename # filename 修改名字 '000000'
    filename_txt = out_dir + filename + '.txt'
    # 创建txt文件
    fp = open(filename_txt, mode="w", encoding="utf-8")
    # 将数据写入文件
    str_tmp = ""  # 存储字符串内容
    # 1.获取数据============================================
    objects = content["objects"]
    # print(len(objects))
    # print("Output", objects[0])
    # 遍历障碍物
    for i in range(len(objects)):
        # 判断objects是否符合要求
        if "content" not in content["objects"][i].keys():
            continue
        label = content["objects"][i]["content"]["label"]
        # print("label:", label)
        str_tmp += str(label) + "  " # 0维
        cx = (content["objects"][i])["center"]["x"]
        cy = (content["objects"][i])["center"]["y"]
        cz = (content["objects"][i])["center"]["z"]
        str_tmp += str(cx) + "  " + str(cy)+ "  " + str(cz)+ "  "  ##暂存内容
        dx = (content["objects"][i])["dimensions"]["length"]
        dy = (content["objects"][i])["dimensions"]["width"]
        dz = (content["objects"][i])["dimensions"]["height"]
        str_tmp += str(dx) + "  " + str(dy)+ "  " + str(dz)+ "  "  ##暂存内容
        yaw = (content["objects"][i])["rotation"]["z"] # 7 yaw角
        trackid =  (content["objects"][i])["objectid"] # 8
        str_tmp += str(yaw) + str(trackid) # 行尾
        #   换行
        str_tmp +=  "\n"  ##暂存内容
    fp.write(str_tmp)
    fp.close()

def main():
    files = os.listdir(json_dir)  # 得到文件夹下的所有文件名称 ['000000.json', '000015.json']
    s = []
    for file in files:  # 遍历文件夹
        filename = file.split('.')[0]
        # print(filename)  # 000015
        get_json(json_dir + file,  out_dir, filename)
# ====================================================================================

def main_livox():
    # 输出文件名：000000
    filename_livox = 0
    # 遍历每个json文件，输出为 out_dir_livox + filename_livox +txt
    for file_livox in tqdm(json_livox_dirs):  # 遍历文件夹
        # print(filename_livox)  # 000015
        get_json(file_livox, out_dir_livox, '%06d' % filename_livox)
        # print("Extracted %d json file"%filename_livox)
        filename_livox+=1
    print("Extracted successfully")

if __name__ == '__main__':
    # main()
    main_livox()