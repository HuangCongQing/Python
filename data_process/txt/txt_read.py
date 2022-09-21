'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-13 18:12:20
LastEditTime: 2022-09-21 17:40:23
FilePath: /Python/data_process/txt/txt_read.py
'''

with open('../extracted/'+file, 'w') as p:
    count = 0
    for line in f.readlines():
        if '>' == line[0]:
            count += 1
        if count == 3:
            p.close()
            break
        p.write(line)
    f.close()