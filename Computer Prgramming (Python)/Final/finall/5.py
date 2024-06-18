from abc import ABC, abstractmethod

class PhoneService(ABC):
	def __init__(self,phone_no,customer_name, mm_yyyy):
		self.phone_no = phone_no
		self.customer_name = customer_name
		self.mm_yyyy = mm_yyyy
	@abstractmethod
	def find_cost():
		pass

class PostPaid(PhoneService):
	def __init__(self, phone_no,customer_name, mm_yyyy,allowance,duration,fixcost):
		super().__init__(phone_no,customer_name, mm_yyyy)a
		self.allowance = allowance
		self.fix_cost = fixcost
		self.duration = duration
	def find_cost(self):
		if self.duration <= self.allowance:
			return self.fix_cost
		else:
			return self.fix_cost + (self.duration- self.allowance)
		
def main():
	service = PostPaid('081-000-0007', 'John English', '09-2021', 800, 1000, 1250)
	print(f'Cost for {service.phone_no}: {service.find_cost()} Bahts')

main()