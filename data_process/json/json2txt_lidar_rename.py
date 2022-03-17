
'''
Description:同时输出pcd和txt
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-01-20 16:20:06
LastEditTime: 2022-03-17 21:15:46
FilePath: /Python/data_process/json/json2txt_lidar_rename.py
'''

import os
import json
import numpy as np
from  tqdm import tqdm

# 本文件测试
json_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_data/'  # json文件路径
out_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_result/'  # 输出的 txt 文件路径


# 项目输入
json_livox_dirs = []
# json_livox = ['/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-1', '/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-2']
json_livox = ['/home/hcq/data/2022anno/HT融合追踪交付0317/标注结果']
# pcd文件
# /home/hcq/data/2022anno/2021.12.10-shenbao/10.25-1/_2021-10-25-09-44-52/livox
pcd_livox = "/home/hcq/data/2022anno/2021.12.10-shenbao/10.25-1/"


# 输出
out_dir_livox_txt = '/home/hcq/data/2022anno/finaul_result/txt_result/'
out_dir_livox_pcd = '/home/hcq/data/2022anno/finaul_result/pcd_result/'

# step1 整理目录层级，得到所有json列表
for i in json_livox:
    # path_paths =
    # for path_path in os.listdir(path):
    #     for path in json_livox + path_path:
    #         file_path =  json_livox + path_path + path
    for j in os.listdir(i):
        list_json = os.listdir('%s/%s/livox/'%(i,j)) # ['000002.json', '000044.json', ...]
        # 1 排序（转数字排序，再转字符）
        flielist = [int(x.split('.')[0]) for x in list_json] # 只有json
        flielist.sort()
        flielist = ['%06d.json' % x for x in flielist]  # 数字转成字符00000.json
        # 2 遍历保存完整json路径
        # for k in list_json:
        for k in flielist:
            # json.load(open('%s/%s/livox/%s' % (i,j,k)))
            json_livox_dirs.append('%s/%s/livox/%s' % (i,j,k)) # 所有json文件路径
            # '/home/hcq/data/2022anno/融合交付/融合交付/2021.12.10-shenbao/10.25-1/_2021-10-25-11-40-50/livox/000002.json'
# print(len(json_livox_dirs))

# ======================================================上面先运行============================================================
# step2 处理每个json文件
# json_file '/home/hcq/data/2022anno/HT融合追踪交付0317/标注结果/_2021-10-25-10-12-37/livox/000000.json'
def get_json(json_file, out_dir, filename):
    # 读取 json 文件数据
    with open(json_file, 'r') as load_f:
        content = json.load(load_f)

    # 修改输出文件名
    # filename = 0
    # filename = '%06d' % filename # filename 修改名字 '000000'
    filename_txt = out_dir +filename + '.txt' # 保存txt文件路径============
    # 保存pcd名字  json的路径
    pcd_path = pcd_livox + json_file.split("/")[-3] + "/livox/" + json_file.split("/")[-1].split(".")[0] + ".pcd"
    # 重命名并保存pcd到指定位置
    src = pcd_path
    dst = out_dir_livox_pcd + filename + ".pcd" # 保存pcd文件路径============
    os.rename(src, dst)
    
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
        str_tmp += str(yaw) + "  " +  str(trackid) # 行尾
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
    # 遍历每个json文件，输出为 out_dir_livox_txt + filename_livox +txt
    for file_livox in tqdm(json_livox_dirs):  # 遍历文件夹
        # print(filename_livox)  # 000015
        get_json(file_livox, out_dir_livox_txt, '%06d' % filename_livox)
        # print("Extracted %d json file"%filename_livox)
        filename_livox+=1 # 输出文件名从00000递增
    print("Extracted successfully")

if __name__ == '__main__':
    # main()
    main_livox()