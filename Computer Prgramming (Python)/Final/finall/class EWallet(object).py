class EWallet:
    def __init__(self, owner, maxMoney):
        self.owner = owner
        self.maxMoney = maxMoney
        self.balance = 0
    
    def deposit(self, amount):
        if self.balance + amount <= self.maxMoney:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("You have reached maximum amount of money for your account!")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current balance: {self.balance}")
        else:
            print("You don't have enough money to withdraw!'")
    
    def getBalance(self):
        print(f"Current balance: {self.balance} THB")

class SmartEWallet(EWallet):
	def __init__(self,owner,max_amount,balance = 0):
		super().__init__(owner,max_amount,balance)
		self.max_withdraw = 0
		self.history = []
	def set_max_withdraw(self, max):
		if max > 0:
			self.max_withdraw = max
		else:
			print("Must not be negative or zero")
	def deposit(self, amount):
		super().deposit(amount)
		self.history.append(f"{self.owner} deposited {amount}. Current balance is {self.balance}")
	def withdraw(self,amount):
		if amount <= self.max_withdraw:
			super().withdraw(amount)
			self.history.append(f"{self.owner} withdrew {amount}. Current balance is {self.balance}")
		else:
			print("Amount exceeds maximum allowance")
	def get_balance(self):
		return self.balance
	def view_history(self):
		for i in self.history:
			print(i)