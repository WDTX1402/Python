class EWallet(object):
	def __init__(self, owner, maximum,balance = 0):
		self.owner = owner
		self.balance = balance
		self.max_amount = maximum

	def deposit(self, amount):
		if self.balance + amount < self.max_amount:
			self.balance += amount
		else:
			print("Cannot withdraw: Exceeds maximum keeping amount.")
	

	def withdraw(self, amount):
		if amount < self.balance:
			self.balance -= amount
	
	def getbalance(self):
		return f"Your current balance is {self.balance:.2f}"
		

class SmartEWallet(EWallet):
	def __init__(self, owner, max_amount):
		super().__init__(owner, max_amount)
		self.transaction_history = []
		self.max_withdrawal_amount = max_amount 

	def deposit(self, amount):
		super().deposit(amount)
		self.transaction_history.append(f"Deposit amount:' {amount}, Balance: {self.balance}"

	def withdraw(self, amount):
		if amount > self.max_withdrawal_amount:
			print("Cannot withdraw: Exceeds maximum withdrawal amount.")
			self.transaction_history.append('Attempt at withdrawing failed')
		else:
			super().withdraw(amount)
			self.transaction_history.append(f"Withdrawal amount:' {amount}, Balance: {self.balance}")

	def set_max_withdrawal_amount(self, amount):
		if amount > self.max_amount:
			print("Maximum withdrawal amount cannot exceed maximum wallet amount.")
		self.max_withdrawal_amount = amount

	def get_transaction_history(self):
		return self.transaction_history

wallet = EWallet('John Doe', 1000)
ewallet = SmartEWallet('John Doe', 1000)
ewallet.deposit(900)
ewallet.withdraw(5220)
ewallet.set_max_withdrawal_amount(200)
print(ewallet.getbalance())
print(ewallet.get_transaction_history())