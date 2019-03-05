# class A开头大写

class Calculator:
    name = "Good calculator"
    price= 10000
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


cal = Calculator()  # Good calculator
cal.name
cal.price  # 为什么没有输出？？？？？？？？？
cal.add(10, 11)  # 21
    
