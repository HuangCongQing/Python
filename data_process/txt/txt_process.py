'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 17:29:15
LastEditTime: 2024-10-08 19:10:02
FilePath: /Python/data_process/txt/txt_process.py
'''


def process_txt(path):
    origin_points = []
    unique_points = []
    time = []
    lines = 0
    with open(path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            lines += 1
            if 'origin_points' in line:
                origin_points.append(int(line.split(":")[-1].strip()))
            if 'unique_points' in line:
                unique_points.append(int(line.split(":")[-1].strip()))
            if 'time_statistics_logger.cc:148] perception::LidarSemanticSegmentationModule' in line:
                time.append(float(line.split("|")[1].strip()))
    print(origin_points, unique_points, time)

if __name__ == '__main__':
    path = "/home/chongqinghuang/code/deploy/main/test.log"
    process_txt(path)