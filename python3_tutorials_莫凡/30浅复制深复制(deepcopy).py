import copy

a = [1, 2, 3]
b = a

id(a)  # 硬盘索引
id(b)

print('a:', id(a), '\nb:', id(b))
print(id(a)==id(b))
a[0] = 3

print(b)

c = copy.copy(a)  # shallow copy
print(id(c) == id(a))

n = [1, 2, [3, 4]]
m=copy.copy(n)
print(id(m) == id(n))
print(a[2]==b[2]) # 一样的


# deep copy

e = copy.deepcopy(n)

print(e[2]==n[2])