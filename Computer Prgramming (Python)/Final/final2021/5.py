from abc import ABC, abstractmethod


class Sale_item(ABC):
	def __init__(self,price):
		self.price = price
	@abstractmethod
	def calculate_cost(self):
		 pass

class Food(Sale_item):
	def __init__(self,price):
		super().__init__(price)
	def calculate_cost(self):
		 pass


class Book(Sale_item):
	def __init__(self, price):
		super().__init__(price)
	
	def calculate_cost(self):
		return self.price * 0.85


class Appliance(Sale_item):
	def __init__(self, price):
		super().__init__(price)
	
	def calculate_cost(self):
		return self.price * 1.07

class Itemized_food(Food):
	def __init__(self, price, quantity):
		super().__init__(price)
		self.quantity = quantity
	
	def calculate_cost(self):
		return self.price * self.quantity


class Measured_food(Food):
	def __init__(self, price, weight):
		super().__init__(price)
		self.weight = weight
	
	def calculate_cost(self):
		 return self.price * self.weight


def main():
    veg = Itemized_food(40, 2)  
    mango = Measured_food(70, 1.8)  
    book = Book(200)                         
    app = Appliance(1200)                         

    total_cost = veg.calculate_cost() + mango.calculate_cost() + book.calculate_cost() + app.calculate_cost()
    print(f"The total cost of the purchased items is: {total_cost:.2f} Bahts")

if __name__ == "__main__":
    main()