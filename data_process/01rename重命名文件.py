import os


class BatchRename():
    """
    批量重命名文件夹中的图片文件
    """
    def __init__(self,path):
        self.path = path

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            Suffix_name = ['.png', '.jpg', '.jpeg', '.tif']
            if item.endswith(tuple(Suffix_name)):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0) * n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting %s--to-->%s' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    path = "./cccc"        # 图片文件夹路径
    demo = BatchRename(path).rename()

# 输出：
# converting D:\python_script\cccc\www (1).jpg --to--> D:\python_script\cccc\000001.jpg
# converting D:\python_script\cccc\www (2).jpg --to--> D:\python_script\cccc\000003.jpg
# converting D:\python_script\cccc\www (3).jpg --to--> D:\python_script\cccc\000004.jpg
# converting D:\python_script\cccc\www (4).jpg --to--> D:\python_script\cccc\000005.jpg
# converting D:\python_script\cccc\www (5).jpg --to--> D:\python_script\cccc\000006.jpg
# total 10 to rename & converted 11 jpgs
