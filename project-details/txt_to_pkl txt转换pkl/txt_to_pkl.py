'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-30 08:25:11
@LastEditors: HCQ
@LastEditTime: 2020-07-30 13:58:04
'''
import os
import numpy as np
import _pickle as pickle 

# def multiple_replace(file):
#       """
#   read file
#   if find
#     replace
#     write to file
#   """
# f = open(file, "r+")
# text = f.readlines()
# f.seek(0)
# f.truncate()
# for line in text:
#     line = line.replace('Pedestrian','1')
#     line = line.replace('Car', '2')
#     line = line.replace('Cyclist', '3')
#     line = line.replace('Truck', '4')
#     line = line.replace('Tricar', '5')
#     f.write(line)
# f.close()

root_dir='predictions'
filename = os.listdir(root_dir)
file_number = len(filename)
li= []
for i in range(1):
    dets_path = os.path.join('predictions', filename[i][:-4] + '.txt')
    # print(dets_path)
    # multiple_replace(dets_path)
    f = open(dets_path, "r+")
    text = f.readlines()
    for line in text:
        list1 = line.split()
    
        data = {
            'name': [list1[0],],
            'truncated':[list1[1],],
            'occluded':[list1[2],],
            'alpha':[list1[3],],
            'bbox': list(map(float,list1[4:8])),# 字符串数组转为数字数组
            'dimensions':list1[8:11],
            'location':list1[11:14],
            'rotation_y':[list1[14], ],
            'score':[list1[15],],
            'metadata':
                {
                    'image_prefix': '/home/ma-user/work/workspace/DeepCamp_Lidar',
                    'num_point_features': 4,
                    'image_idx': filename[i][:-4],
                    'token': filename[i][:-4]
                }
        }
        # print(data)

        li.append(data)
print(li)
print(len(li))
with open('reslut.pkl', 'ab+') as f:
    pickle.dump(li, f)
# # 读取
# with open('reslut.pkl','rb') as f:
#     while True:
#         try:
#             aa = pickle.load(f)
#             print(aa)
#         except EOFError:
#             break