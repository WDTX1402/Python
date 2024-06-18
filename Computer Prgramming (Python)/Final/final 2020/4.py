class EWallet(object):
	def __init__(self, owner, balance = 0,maximum = 0):
		self.owner = owner
		self.balance = balance
		self.max = maximum

	def deposit(self, amount):
		if self.balance + amount < self.max:
			self.balance += amount

	def withdrawall(self, amount):
		if amount < self.balance:
			self.balance -= amount
	
	def getbalance(self):
		return f"Your current balance is {self.balance:.2f}"
		
