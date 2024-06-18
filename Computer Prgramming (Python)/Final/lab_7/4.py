class QuadraticEquation:
	def __init__(self, a, b, c):
		self.__a = a
		self.__b = b
		self.__c = c

	def getA(self):
		return self.__a

	def getB(self):
		return self.__b

	def getC(self):
		return self.__c

	def getDiscriminant(self):
		return (self.__b ** 2) - (4 * self.__a * self.__c)

	def getRoot1(self):
		discriminant = self.getDiscriminant()
		if discriminant < 0:
			return 0
		return (-self.__b + discriminant**0.5) / (2 * self.__a)

	def getRoot2(self):
		discriminant = self.getDiscriminant()
		if discriminant < 0:
			return 0
		return (-self.__b - discriminant**0.5) / (2 * self.__a)