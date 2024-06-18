class Time(object):
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
	
	def __str__(self):
		if self.hour < 24 and self.minute < 60 and self.second < 60:
			return f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs"
		else:
			return "Wrong input"

# Example usage:
time1 = Time(9, 30, 0)
print(time1)  # Should print: 09:30:00 Hrs
