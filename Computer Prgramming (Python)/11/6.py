import abc


class Transportation(metaclass = abc.ABCMeta):
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance

    @abc.abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)

    def find_cost(self):
        return 0
    

class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)

    def find_cost(self):
        return (self.distance) * 40
    
class Train(Transportation):
    def __init__(self, start, end, distance, numsta):
        super().__init__(start, end, distance)
        self.numsta = numsta

    def find_cost(self):
        return (self.numsta) * 5
    
walk = Walk("kmitl","lawson at kmitl", 0.6)
taxi1 = Taxi("lawson at kmitl", "ladkrabang station", 5)
train = Train("ladkrabang station", "payathai station", 40, 6)
taxi2 = Taxi("payahtai station", "the british council", 3)

list = [walk, taxi1,train,taxi2]
for i in list:
    print(i.find_cost())
