import turtle
import abc


class Char(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def draw(self, x, y):
        pass

    @abc.abstractmethod
    def getWidth(self):
        pass

class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('0')

    def getWidth(self):
        return 14

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('1')

    def getWidth(self):
        return 10

class Char2(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('2')

    def getWidth(self):
        return 14

class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('3')

    def getWidth(self):
        return 14

class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('4')

    def getWidth(self):
        return 14

class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('5')

    def getWidth(self):
        return 14

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('6')

    def getWidth(self):
        return 14

class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('7')

    def getWidth(self):
        return 14

class Char8(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('8')

    def getWidth(self):
        return 14

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write('9')

    def getWidth(self):
        return 14


num_char_map = {
    '0': Char0(),
    '1': Char1(),
    '2': Char2(),
    '3': Char3(),
    '4': Char4(),
    '5': Char5(),
    '6': Char6(),
    '7': Char7(),
    '8': Char8(),
    '9': Char9()
}

def drawNum(x):
    x_str = str(x)
    x_position = 0 
    for digit in x_str:
        char_obj = num_char_map[digit]
        char_obj.draw(x_position, 0)
        x_position += char_obj.getWidth()

drawNum(1234567890)
turtle.done()
