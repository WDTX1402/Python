class Clock:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self,h,m,s):
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.hour = h
            self.minute = m
            self.second = s
        else:
            return "Invalid input"
    def get_time(self):
        return self.hour, self.minute, self.second

    def tick(self):
            self.second += 1
            if self.second >= 60:
                self.second = 0
                self.minute += 1
                if self.minute >= 60:
                    self.minute = 0
                    self.hour += 1
                    if self.hour >= 24:
                        self.hour = 0
    def display_time(self):
        am_pm = "AM"
        hour = self.hour
        if hour >= 12:
            am_pm = "PM"
            if hour > 12:
                hour -= 12
        if hour == 0:
            hour = 12
        return f"{hour:02d}:{self.minute:02d}:{self.second:02d} {am_pm}"

time = Clock(15,55,30)
# print(time.display_time())

for i in range(86400):
    time.tick()
    print(time.display_time())