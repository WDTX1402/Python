import turtle as t
import math

class Circle:
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def getArea(self):
		return math.pi * (self.r ** 2)

	def getPerimeter(self):
		return 2 * math.pi * self.r

	def move(self, newX, newY):
		self.x = newX
		self.y = newY
	def draw(self):
		t.penup()
		t.goto(self.x, self.y) 
		t.right(90)
		t.fd(self.r)
		t.left(90)
		t.pendown()
		t.circle(self.r)
		t.done()
		

lol = Circle(10,10,50)
lol.draw()