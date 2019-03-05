# 字典 {键值对}   无序  里面放什么都行

a_list = {1, 2, 3, 4, 5}
d = {'apple': [1,2,3], 'pear': 2, 'orange': {1:'111',2:'222'}}

print(d)

print(d['apple'])
del d['apple']

d['b'] = 20

print(d)
print(d['orange'][1])  # {1:'111',2:'222'}
