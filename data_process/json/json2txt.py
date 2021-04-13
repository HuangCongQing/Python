'''
Description: json转txt文件
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 18:34:32
LastEditTime: 2021-04-13 18:47:15
FilePath: /Python/data_process/json/json2txt.py
'''


import os
import json
import numpy as np
from  tqdm import tqdm

def read_json(json_path):
    # 当文件中包含中文时,设置以utf-8解码模式读取文件open(out_path, 'w',encoding='utf-8'，默认以gbk模式读取文件，
    f = open(json_path)
    json_file = json.load(f)
    return json_file


def save_json(out_path, json_file):
    f = open(out_path, 'w', encoding='utf-8')  # 设置以utf-8解码模式读取文件,默认为gbk模式
    json.dump(json_file, f)


def edit_labelme_json(labelme_json):
    # 对labelme生成的json文件进行内容编辑
    # labelme数据格式以字典形式存储，格式如下：
    # labelme_json = {'flags':{},"shapes":[],
    # 	"lineColor":[0,255,0,128],"fillColor": [255,0,0,128],
    # 	"imagePath": "",
    # 	"imageData":''}
    version = labelme_json['version']
    flags = labelme_json['flags']
    shapes = labelme_json['shapes']  # 获取json shape
    imagePath = labelme_json['imagePath']
    imageData = labelme_json['imageData']
    imageHeight = labelme_json['imageHeight']
    imageWidth = labelme_json['imageWidth']

    ##################### 编辑 #############################
    label_list = []  # 记录json中所有物体的标签
    label_dic = {}  # 记录每个label出现的个数

    points_values = ''
    # imageHeight = int(imageHeight/10) #图像缩放
    # imageWidth = int(imageWidth/10)
    for tmp_shape in tqdm(shapes):
        for shape_key, shape_values in tmp_shape.items():
            # 对每个类别进行计数并修改类别标签名，将语义分割标签转化为实例分割标签
            if shape_key == 'points':
                points_values = shape_values  # 二维数组
                np.savetxt('/home/hcq/pointcloud/Python/data_process/json/json_result/labelme_test.txt', points_values, fmt="%.18f,%.18f", delimiter="\n") 
            # 生成一个新的json数据


def list_json(path):
    sup_ext = ['.json']
    all_list = list(map(lambda x: os.path.join(path, x), os.listdir(path)))
    json_list = [x for x in all_list if os.path.splitext(x)[1] in sup_ext]
    return json_list


if __name__ == '__main__':
    # json_dir = 'json_ori'
    # out_dir = 'json'
    json_dir = '/home/hcq/pointcloud/Python/data_process/json/json_data'
    out_dir = '/home/hcq/pointcloud/Python/data_process/json/json_result'
    json_list = list_json(json_dir)
    for i in range(len(json_list)):
        json_r = read_json(json_list[i])
        json_ed = edit_labelme_json(json_r)  # 处理json数据
