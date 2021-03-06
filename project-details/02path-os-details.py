'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-20 22:30:12
@LastEditors: HCQ
@LastEditTime: 2020-07-25 00:30:02
'''
# 参考：记录下os.path.dirname(__file__)使用 https://blog.csdn.net/JOJOY_tester/article/details/54598713

# 在运行的时候如果输入完整的执行的路径，则返回.py文件的全路径如：Python c:/test/test.py 则返回路径 c:/test ，如果是python test.py 则返回空；
# os.path.abspath(__file__)返回的是.py文件的绝对路径

import os
import sys
#该文件所在位置：D:\第1层\第2层\第3层\第4层\第5层\test11.py
 
path1 = os.path.dirname(__file__)
print(path1)#获取当前运行脚本的绝对路径  f:\Github\Python\project-details
 
path2 = os.path.dirname(os.path.dirname(__file__)) #
print(path2)#获取当前运行脚本的绝对路径（去掉最后一个路径） f:\Github\Python
 
path3 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
print(path3)#获取当前运行脚本的绝对路径（去掉最后2个路径）f:\Github
 
path4 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(path4)#获取当前运行脚本的绝对路径（去掉最后3个路径）
 
path5 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(path5)#获取当前运行脚本的绝对路径（去掉最后4个路径）
 
path6 = os.__file__                  #获取os所在的目录
print(path6)  # D:\ProgramData\Anaconda3\lib\os.py
path7 = os.path.abspath(__file__)   # 返回的是.py文件的绝对路径。
print(path7)  # 

# 项目中
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
print("sys.path: ", sys.path) # sys.path是一个数组

DATA_DIR = os.path.join(BASE_DIR, 'data') # 在本目录新建data文件夹 "f:\Github\Python\project-details\data"
print("DATA_DIR \n", DATA_DIR)
www = 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip'
zipfile = os.path.basename(www) # 获得文件名modelnet40_ply_hdf5_2048
print('zipfile', zipfile)
# os.system 运行linux命令
# os.system('wget --no-check-certificate %s; unzip %s' % (www, zipfile))


v_f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/home/cjm/Desktop/Deecamp/workspace/DeepCamp_Lidar/test_video_filter")
print("==========v_f==================")
print(v_f)
