from abc import ABC, abstractmethod

class PhoneService(ABC):
	def __init__(self, phone_no, customer_name, mm_yyyy):
		self.phone_no = phone_no
		self.customer_name = customer_name
		self.mm_yyyy = mm_yyyy

	@abstractmethod
	def find_cost(self):
		pass


class Post_paid(PhoneService):
	def __init__(self, phone_no, customer_name, mm_yyyy, fixed_cost, allowance, call_duration):
		super().__init__(phone_no, customer_name, mm_yyyy)
		self.fixed_cost = fixed_cost
		self.allowance = allowance
		self.call_duration = call_duration

	def find_cost(self):
		if self.call_duration > self.allowance:
			extra_minutes = self.call_duration - self.allowance
		return self.fixed_cost + extra_minutes


class Pre_paid(PhoneService):
	def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
		super().__init__(phone_no, customer_name, mm_yyyy)
		self.call_duration = call_duration

	def find_cost(self):
		return self.call_duration * 2  # 2 Bahts per minute


class Fixed_line(PhoneService):
	def __init__(self, phone_no, customer_name, mm_yyyy, local_calls):
		super().__init__(phone_no, customer_name, mm_yyyy)
		self.local_calls = local_calls

	def find_cost(self):
		return self.local_calls * 3  # 3 Bahts per local call


def main():
	post_paid_service = Post_paid('081-000-0007', 'John English', '09-2021', 800, 1000, 1250)
	pre_paid_service = Pre_paid('080-000-0007', 'John English', '09-2021', 100)
	fixed_line_service = Fixed_line('02-000-0007', 'John English', '09-2021', 200)

	services = [post_paid_service, pre_paid_service, fixed_line_service]

	for service in services:
		print(f'Cost for {service.phone_no}: {service.find_cost()} Bahts')


if __name__ == '__main__':
	main()
