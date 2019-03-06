
''' zip
lambda
map '''


a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))  # <zip object at 0x000000000120E408>

print(list(zip(a, b)))

for i, j in zip(a, b):
    print(i / 2, j * 2)

zip(a, a, b)


# lambda

def fun1(x, y):
    return (x + y)

fun2 = lambda x, y: x + y

print(fun2(2, 3))

#map

map(fun1, [1], [2])
print(map(fun1, [1], [2]))

list(map(fun1, [1], [2]))
print(list(map(fun1, [1], [2])))
print(list(map(fun1, [1,3], [2,1])))
