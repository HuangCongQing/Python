#主要是爬虫

import re  # 正则表达式
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'


print(re.search(pattern1, string))

print(re.search(pattern2, string))


# 匹配多种可能 ，使用[]
# r[au]n  ran,run


# 更多种

# [0 - 9]
# [a - z]
# [0-9a-z]

# 特征数字匹配

# 见下图

# ![image.png](https: // upload-images.jianshu.io/upload_images/4340772-16128d66f7b19c7d.png?imageMogr2/auto-orient/strip % 7CimageView2/2/w/1240)


