'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-10-22 10:06:47
LastEditTime: 2021-10-22 10:36:33
FilePath: /Python/data_process/txt/读取文件名并生成txt文件.py
'''
import os


class ReadImageName():
    def __init__(self):
        self.path = '/home/hcq/data/test_anno_2021-08-02-10-22-25_bag试标结果/试标结果/点云追踪结果/转换后结果数据/test_anno_2021-08-02-10-22-25_bag'

    def readname(self):
        filenames = os.listdir(self.path)
        flielist = []

        for item in filenames:
            if item.endswith('.txt'):
                # itemname = os.path.join(self.path, item) # '/home/hcq/data/test_anno_2021-08-02-10-22-25_bag试标结果/试标结果/点云追踪结果/源文件/test_anno_2021-08-02-10-22-25_bag/000009.jpg'
                # itemname = itemname[-11:] #
                # flielist.append(itemname) # 000001 saved
                flielist.append(item[0:6]) # 000001 saved
        # sort
        flielist = [int(x) for x in flielist]
        flielist.sort() #
        flielist = ['%06d'%x for x in flielist] # 数字转成字符
        # save
        fo = open("filename.txt", "w")
        for item in flielist:
            fo.write(str(item) + "\n")


if __name__ == '__main__':
    log = ReadImageName()
    log.readname()