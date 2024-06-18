import abc
import turtle as t

class TwoDShape(metaclass = abc.ABCMeta):
    def __init__(self, x,y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x, y ,x2, y2):
        super().__init__(x, y)
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.goto(self.x2, self.y2)


class Rectangle(TwoDShape):
    def __init__(self, x, y ,width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)

class Circle(TwoDShape):
    def __init__(self, x, y ,r):
        super().__init__(x, y)
        self.r = r

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.r)

class Square(TwoDShape):
    def __init__(self, x, y ,length):
        super().__init__(x, y)
        self.l = length

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for i in range(4):
            t.fd(self.l)
            t.right(90)


l1 = Line(10,20,50,0)
r1 = Rectangle(-20,-20.,50,30)
c1 = Circle(0, -70, 20)
s1 = Square(0, -130, 20)

list = [l1,r1,c1,s1]

for i in list:
    i.draw()

t.done()