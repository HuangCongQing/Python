APPLE = 100
a=None

def fun():
    global a
    a = 10
    print(a)  # 10
    return a+100
print(a) # None
print(fun())  #110
print(a)