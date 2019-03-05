# list
a = [1, 2, 33, 4, 1, 56, 7, -1]
# a.append(123) # append
print(a)

a.insert(1, 0) # 插入
print(a)

a.remove(33)  # remove value 第一个值
print(a)

print(a[0])
print(a[-1])  # 最后一位

print(a[0:3])
print(a[:3])
print(a[3:])

print(a[-3:])

# 索引
print(a.index(1))
print(a.count(1))  # 出现几次

# 排序
a.sort(reverse=True)

print(a)
