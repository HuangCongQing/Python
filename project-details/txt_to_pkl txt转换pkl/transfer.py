'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-30 08:08:43
@LastEditors: HCQ
@LastEditTime: 2020-07-30 12:20:37
'''
import _pickle as pickle 

# f = open('dict_word.pkl', 'rb')
# for line in f:
#     print(line)

# word = pickle.load(open("preditions.pkl", 'rb'), encoding='utf-8')
# print(word)

# D = {
#     'name': 'bob',
#     'major': {
#         'english',
#         'math'
#     },
#     'd': [1, 2, 3, 4, 5, 6, 7]
# }

D = {
    'name': ['Car',],
    'truncated':[0.,],
    'occluded':[0,],
    'alpha':[0,],
    'bbox':[-1,-1,-1,-1],
    'dimensions':[4.5676007,2.041592,1.6213634],
    'location':[2.752196,-6.6567035,0.7322118],
    'rotation_y':[0.0485813, ],
    'score':[0.5716194,],
    'metadata':
        {
            'image_prefix': '/home/ma-user/work/workspace/DeepCamp_Lidar',
            'num_point_features': 4,
            'image_idx':'009001',
            'token':'009001'
        }
}

with open('D.pkl', 'ab+') as f:
    pickle.dump(D, f)


# word = pickle.load(open("D.pkl", 'rb'), encoding='utf-8')
# print(word)


# 读取
with open('D.pkl','rb') as f:
    while True:
        try:
            aa = pickle.load(f)
            print(aa)
        except EOFError:
            break


# word = pickle.load(open("result.pkl", 'rb'), encoding='utf-8')
# print(word)