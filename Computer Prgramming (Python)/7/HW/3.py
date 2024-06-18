class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def geta (self):
        return self.__a
    def getb (self):
        return self.__b
    def getc (self):
        return self.__c
    def getd (self):
        return self.__d
    def gete (self):
        return self.__e
    def getf (self):
        return self.__f
    def isSolvable (self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return False
    def getX(self):
        if self.isSolvable() == True:
            return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
           
    def getY(self):
        if self.isSolvable() == True:
            return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
        
le = LinearEquation(1,2,3,4,5,6)
print(le.getX())