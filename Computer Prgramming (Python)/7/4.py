import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def getDiscriminant(self):
        return (self.__b ** 2) - (4 *(self.__a * self.__c))
    
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)

x = QuadraticEquation(5,9,2)
print(x.getRoot1())
print(x.getRoot2())  