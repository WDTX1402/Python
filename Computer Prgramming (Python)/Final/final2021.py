
# #Q1
# def find_word_positions(word,list):
# 	wrd = word.lower()
# 	wrdlist = []
# 	for i in list:
# 		wrdlist.append(i.lower())
	
# 	indx = []
# 	for j in range(len(wrdlist)):
# 		if wrd == wrdlist[j]:
# 			indx.append(j)
		
# 	if indx == []:
# 		return 0
# 	else:
# 		return indx

# print(find_word_positions('Python',['python','java', 'c','PYTHON','Prolog']))
# print(find_word_positions('iOS',['Windows','macOS','Linux']))

# #Q2
def popularity_scores(language_scores):
  
	sorted_scores = sorted(language_scores.items(), key=lambda item: item[1], reverse=True)

	ranked_languages = {}
	current_rank = 1
	last_score = None

  
	for language, score in sorted_scores:
		if score == last_score:
	
			ranked_languages[language] = current_rank - 1
		else:
 
			ranked_languages[language] = current_rank
			last_score = score
		current_rank += 1

   
	result = {}
	for language, rank in ranked_languages.items():
		if rank not in result:
			result[rank] = language
		else:
			result[rank] += ", " + language

	return result

pop = {'C++': 99.7, 'C': 96.7, 'Java': 97.5, 'Python': 100, 'C#': 89.4, 'Ruby': 97.5}
print(popularity_scores(pop))

# #Q4
# class SavingAccount(object):
# 	def __init__(self, bank_name, acc_name, acc_id, balance):
# 		self.bank_name = bank_name
# 		self.acc_name = acc_name
# 		self.acc_id = acc_id
# 		self.balance = balance
# 		self.transac_his = []

# 	def deposit(self,money, person,date):
# 		self.balance += money
# 		self.transac_his.append(f"{date}:{person}, Amount Balance:{self.balance}")
# 	def withdraw(self, money, person,date):
# 		if self.balance > money:
# 			self.balance -= money
# 			self.transac_his.append(f"{date}:{person}, Account Balance:{self.balance}")
# 		else:
# 			return f"Insuffecient funds"

# 	def get_balance(self):
# 		return self.balance
# 	def print_statement(self):
# 		for i in self.transac_his:
# 			print(i)


# class OverDrawnAccount(SavingAccount):
#	 def __init__(self, bank_name, acc_name, acc_id, balance, limit):
#		 super().__init__(bank_name, acc_name, acc_id, balance)
#		 self.limit = limit

#	 def withdraw(self, money, person, date):
#		 if self.balance - money >= -self.limit:
#			 super().withdraw(money, person, date)  
#		 else:
#			 return "Overdraft limit exceeded"
		

# saving_acc = SavingAccount("Bank of Python", "John Doe", "12345", 1000)
# saving_acc.deposit(500, "John Doe", "2023-11-05")
# saving_acc.withdraw(200, "Jane Doe", "2023-11-06")
# saving_acc.print_statement()


# overdrawn_acc = OverDrawnAccount("Bank of Python", "Jane Smith", "67890", 1000, 500)
# overdrawn_acc.deposit(500, "Jane Smith", "2023-11-05")
# overdrawn_acc.withdraw(1200, "Jane Smith", "2023-11-05")
# overdrawn_acc.withdraw(300, "Jane Smith", "2023-11-06")
# overdrawn_acc.print_statement()

#Q5
from abc import ABC, abstractmethod


class Sale_item(ABC):
	@abstractmethod
	def calculate_cost(self):
		 pass

class Food(Sale_item):
	def calculate_cost(self):
		 pass


class Book(Sale_item):
	def __init__(self, price):
		self.price = price
	
	def calculate_cost(self):
		return self.price * 0.85


class Appliance(Sale_item):
	def __init__(self, price):
		self.price = price
	
	def calculate_cost(self):
		return self.price * 1.07

class Itemized_food(Food):
	def __init__(self, price_per_item, quantity):
		self.price_per_item = price_per_item
		self.quantity = quantity
	
	def calculate_cost(self):
		return self.price_per_item * self.quantity


class Measured_food(Food):
	def __init__(self, price_per_kg, weight):
		self.price_per_kg = price_per_kg
		self.weight = weight
	
	def calculate_cost(self):
		 return self.price_per_kg * self.weight


def main():
    veg = Itemized_food(price_per_item=40, quantity=2)  
    mango = Measured_food(price_per_kg=70, weight=1.8)  
    book = Book(price=200)                         
    app = Appliance(price=1200)                         

    total_cost = veg.calculate_cost() + mango.calculate_cost() + book.calculate_cost() + app.calculate_cost()
    print(f"The total cost of the purchased items is: {total_cost:.2f} Bahts")

if __name__ == "__main__":
    main()


def count_operands_in_expr(expr):
	# Base case: If the expression is not a tuple, it is an operand
	if not isinstance(expr, tuple):
		return 1
	
	# Recursive case: Otherwise, it's an operation (binary)
	# Count the operands in the left and right sub-expressions
	left, _, right = expr
	return count_operands_in_expr(left) + count_operands_in_expr(right)