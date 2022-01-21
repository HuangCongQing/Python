
'''
Description:
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-01-20 16:20:06
LastEditTime: 2022-01-20 20:59:49
FilePath: /Python/data_process/json/json2txt_lidar.py
'''

import os
import json
import numpy as np
from  tqdm import tqdm


json_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_data/'  # json文件路径
out_dir = '/home/hcq/pointcloud/Python/data_process/json/livox_result/'  # 输出的 txt 文件路径


def get_json(json_file, filename):
    # 读取 json 文件数据
    with open(json_file, 'r') as load_f:
        content = json.load(load_f)

    # # 循环处理
    tmp = filename
    filename_txt = out_dir + tmp + '.txt'
    # 创建txt文件
    fp = open(filename_txt, mode="w", encoding="utf-8")
    # 将数据写入文件
    str_tmp = ""  # 存储字符串内容
    # 1.获取version、flags数据============================================
    objects = content["objects"]
    print(len(objects))
    print("Output", objects[0]["content"])
    # 遍历3障碍物
    for i in range(len(objects)):
        # 判断objects是否符合要求
        if "content" not in content["objects"][i].keys():
            continue
        label = content["objects"][i]["content"]["label"]
        print("label:", label)
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
    files = os.listdir(json_dir)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        filename = file.split('.')[0]
        print(filename)  # 000015
        get_json(json_dir + file, filename)


if __name__ == '__main__':
    main()