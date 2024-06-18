import math

class Calculator(object):
    def __init__(self, acc =0.0):
        self.acc = acc
    
    def set_accumulator(self, a):
        self.acc = a

    def get_accumulator(self):
        return self.acc
        
    def add(self,x):
        self.acc += x

    def subtract(self,x):
        self.acc -= x

    def multiply(self,x):
        self.acc *= x

    def divide(self,x):
        self.acc /= x

    def print_result(self):
        print(f"Result: {self.acc}")


class Sci_calc(Calculator):
    def __init__(self, acc):
        super().__init__(acc)
        
    def square(self):
        self.acc = self.acc ** 2
    
    def exp(self,x):
        self.acc = self.acc ** x

    def factorial(self):
       n = math.factorial(self.acc)
       self.acc = n

    def print_result(self):
        print(f"Result: {'{:e}'.format(self.acc)}")

out = Sci_calc(3)

out.get_accumulator()
out.add(2)
out.factorial()
out.print_result()

