'''
Description: labelme json文件读取和保存
Tips: 需要设置路径
link： https://codeleading.com/article/59014139939/
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 17:30:08
LastEditTime: 2021-04-13 18:08:29
FilePath: /Python/data_process/json/labelme_json.py
'''

import os,json
import numpy as np

def read_json(json_path):
	f = open(json_path)  ##当文件中包含中文时,设置以utf-8解码模式读取文件open(out_path, 'w',encoding='utf-8'，默认以gbk模式读取文件，
	json_file = json.load(f)
	return json_file

def save_json(out_path,json_file):
	f = open(out_path, 'w',encoding='utf-8')  ##设置以utf-8解码模式读取文件,默认为gbk模式
	json.dump(json_file,f)

def edit_labelme_json(labelme_json):
	# 对labelme生成的json文件进行内容编辑
	# labelme数据格式以字典形式存储，格式如下：
	# labelme_json = {'flags':{},"shapes":[],
	# 	"lineColor":[0,255,0,128],"fillColor": [255,0,0,128],
	# 	"imagePath": "",
	# 	"imageData":''}
	version = labelme_json['version']
	flags = labelme_json['flags']
	shapes = labelme_json['shapes'] # 获取json shape
	imagePath = labelme_json['imagePath']
	imageData = labelme_json['imageData']
	imageHeight = labelme_json['imageHeight']
	imageWidth = labelme_json['imageWidth']

	##################### 编辑 #############################
	label_list = [] #记录json中所有物体的标签
	label_dic = {} #记录每个label出现的个数

	# imageHeight = int(imageHeight/10) #图像缩放
	# imageWidth = int(imageWidth/10)
	new_shapes = list([])
	for tmp_shape in shapes:
		for shape_key,shape_values in tmp_shape.items():
			## 对每个类别进行计数并修改类别标签名，将语义分割标签转化为实例分割标签
			if shape_key == 'label':
				# shape_values = shape_values
				if shape_values not in label_list:
					label_list.append(shape_values) # 物体标签'curb'
					label_dic.update({shape_values:0})
					shape_values = shape_values+'0'
				else:
					label_dic.update({shape_values:label_dic[shape_values]+1})
					shape_values = shape_values+str(label_dic[shape_values])
				label_values = shape_values # 'curb0'
			## 其他参数均不变
			elif shape_key == 'points':
    				points_values = shape_values # 二维数组
			elif shape_key == 'group_id':group_id_values = shape_values
			elif shape_key == 'shape_type':shape_type_values = shape_values
			elif shape_key == 'flags':flags_values = shape_values
		# 生成一个新的json数据
		new_shape = {'label':label_values,'points':points_values,'group_id':group_id_values,'shape_type':shape_type_values,'flags':flags_values}
		new_shapes.append(new_shape)
	new_json = {'version':version,
				'flags':flags,
				'shapes':new_shapes,
				'imagePath':imagePath,
				'imageData':imageData,
				'imageHeight':imageHeight,
				'imageWidth':imageWidth}

	return new_json # # 生成一个新的json数据

def list_json(path):
	sup_ext = ['.json']
	all_list = list(map(lambda x:os.path.join(path,x),os.listdir(path)))
	json_list = [x for x in all_list if os.path.splitext(x)[1] in sup_ext]
	return json_list

def get_outpath(out_dir,name):
	if not os.path.exists(out_dir):os.makedirs(out_dir)
	return os.path.join(out_dir,os.path.basename(name))

if __name__ == '__main__':
    # json_dir = 'json_ori'
	# out_dir = 'json'
	json_dir = '/home/hcq/pointcloud/Python/data_process/json/json_data'
	out_dir = '/home/hcq/pointcloud/Python/data_process/json/json_result'
	json_list = list_json(json_dir)
	for i in range(len(json_list)):
		json_r = read_json(json_list[i])
		json_ed = edit_labelme_json(json_r) # 处理json数据
		outpath = get_outpath(out_dir,json_list[i])
		save_json(outpath,json_ed)

