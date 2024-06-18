import abc

class stationarygood(metaclass = abc.ABCMeta):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abc.abstractmethod
    def get_cost(self):
        pass


class Magazine(stationarygood):
    def __init__(self, name, price):
        super().__init__(name, price)
    def get_cost(self):
        return self.price
    
class Book(stationarygood):
    def __init__(self, name, price):
        super().__init__(name, price)
    def get_cost(self):
        return self.price * 0.9

class Ribbon(stationarygood):
    def __init__(self, name,price, length):
        self.length = length
        super().__init__(name,price) 
    def get_cost(self):
        return self.price * self.length

def TotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.get_cost()
    return total_cost


magazine = Magazine("Computer World", 70)
book = Book("Windows 7 for Beginners", 200)
ribbon = Ribbon("Blue Ribbon",5, 10)


print(f"Total cost:{TotalCost([magazine] * 3 + [book] * 2 + [ribbon])} Bahts")
