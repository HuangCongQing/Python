a = [1, 2, 3, 4, 5]

multi_dim_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(a[1])
print(multi_dim_a[0][2])


# 切片转成np.array()处理
import numpy as np
 
# 对于ndarray的切片，格式为[x1:x2, y1:y2]，截取行数为[x1,x2)，列数为[y1,y2)。左边闭空间，右边开空间。
# 如果要截取某一行，格式为[x,:]，截取某一列：[:,y]
# 其他截取以此类推
 
list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
list_ndarray = np.array(list)
list_t = list_ndarray[1:3,1:3]
print(list_t)
 
# 输出如下
# [[ 6  7]
#  [10 11]