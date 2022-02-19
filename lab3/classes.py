# 1)
class newstr:
    
    def __init__(self, st):
        self.string = st

    def getString(self):
        return self.string

    def printString(self):
        print(self.string.upper())

S1 = newstr('Nursat')
# print(S1.getString())
# S1.printString()

# 2)

class Shape:
    def __init__(self, fig):
        self.area = fig
    def def_area(self):
        print(0)

class Square(Shape):
    def __init__(self, x, area):
        self.lenth = x
        super().__init__(area)
    def area(self):
        print(self.lenth * self.lenth)

class Rectangle(Shape):
    def __init__(self, area, a, b):
        super().__init__(area)
        self.a_side = a
        self.b_side = b
    def area2(self):
        print(self.a_side * self.b_side)
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'{self.x},{self.y}')
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
    def dist(self,point2):
        res = ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
        print(res)

# p1 = Point(1, 10)
# p2 = Point(7, 8)
# p1.show()
# p1.move(0,0)
# p1.dist(p2)

class Account:
    def __init__(self, name, soname, balance):
        self.name = name
        self.soname = soname
        self.balance = balance
    def deposit(self, money):
        self.balance = self.balance + money
    def withdraw(self, unmoney):
        if self.balance - unmoney < 0: print('Недостаточно средств для снятия')
        else: self.balance = self.balance - unmoney
    def show_balance(self):
        print(self.balance)
