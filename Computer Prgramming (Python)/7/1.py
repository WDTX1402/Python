# class Time:
#     def __init__(self,hours,minutes,seconds):
#         self.hours =hours
#         self.minutes=minutes
#         self.seconds=seconds
#     def showtime(self):
#         return (self.hours, ":", self.minutes, ":", self.seconds< "Hrs.")
    
# time1 = Time(9,30,0)
# time1.print()

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def print_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} Hrs."
         
    

time1 = Time(9,30,0)
print(time1.print_time())  
