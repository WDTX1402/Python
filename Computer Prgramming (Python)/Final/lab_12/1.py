from abc import ABC, abstractmethod
import turtle as t

class TwoDShape(abstractmethod):
		@abstractmethod
		def draw(self):
			pass

class Line(TwoDShape):
		def __init__(self,x1,y1,x2,y2):
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2
		def draw(self):
			t.penup()
			t.goto(self.x1, self.y1)
			t.pendown()
			t.goto(self.x2, self.y2)
			