class BankAccount:
	def __init__(self, bank_name, owner_name,acc_num,balance):
		self.bank_name = bank_name
		self.owner_name = owner_name
		self.acc_num = acc_num
		self.balance = balance
	
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount):
		if amount < self.balance:
			self.balance -= amount
		else:
			print("Insufficient funds to withdraw")
	def get_balance(self):
		print(self.balance)