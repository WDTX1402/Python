import math

class Point(object):
    def __init__(self, x= 0.0,y= 0.0):
        self.x = x
        self.y = y
        
    def printinfo(self):
        print(self.x, self.y)

class Circle(Point):
    def __init__(self, x = 0, y= 0, radius = 0.0):
        super().__init__(x,y)
        self.r = radius
    
    def area(self):
        return math.pi * self.r * 2
    
    def printinfo(self):
        print(f"Position: {self.x},{self.y}; Raidus{self.r}; Area: {self.area()}")
 
c1 = Circle(9,9,9)
c1.printinfo() 