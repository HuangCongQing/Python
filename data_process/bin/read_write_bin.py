'''
Description: https://www.yuque.com/huangzhongqing/lang/vbh9gmhu2hserqm7
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2024-03-07 19:33:43
LastEditTime: 2024-03-07 19:35:01
FilePath: /Python/data_process/bin/read_write_bin.py
'''

import numpy as np
import os

save_path = 'xxxx/xxx.bin'
# 保存
save_data = np.concatenate((depth[:, np.newaxis], xyz), axis=1)
save_data.tofile( os.path.join(save_path))

# 读取
exited_data =  np.fromfile(save_path,dtype=np.float32).reshape(-1, 9)