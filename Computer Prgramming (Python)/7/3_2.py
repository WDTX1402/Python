import turtle as t
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def getArea(self):
        area = math.pi * (self.radius ** 2)
        return area
    def getPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        return newX, newY
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.radius)




inpus = Circle(-200,50,150)
inpus.draw()
inpus.move(-50,-60)
inpus.draw()

t.done()