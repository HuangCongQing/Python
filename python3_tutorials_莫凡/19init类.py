# class A开头大写

class Calculator:
    name = "Good calculator"
    price = 10000
    def __init__(self, name, price, hight, width, weight):
        self.n = name
        self.p = price
        self.h = hight
        self.w = width
        self.w = weight

    def add(self, x, y):  # 默认self
        print(self.name)
        result = x + y
        print(result)
    def minus(self, x, y):
        result = x + y
        print(result)
    def times(self, x, y):
        result = x * y
        print(result)
    def divide(self, x, y):
        print()

# 调用

cal = Calculator('Good', 1, 2, 3, 4)
print(cal)
print(cal.name)

    
