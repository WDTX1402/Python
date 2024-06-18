import time


class Clock:
    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def set_time(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def run(self):
        while True:
            time.sleep(1)  
            self.increment_time()
            print(self.get_formatted_time())

    def run_time(self):
        self.ss += 1
        if self.ss >= 60:
            self.ss = 0
            self.mm += 1
        if self.mm >= 60:
            self.mm = 0
            self.hh += 1
        if self.hh >= 24:
            self.hh = 0

    def get_formatted_time(self):
        return f"{self.hh:02}:{self.mm:02}:{self.ss:02}"

class AlarmClock(Clock):
    def __init__(self, hh=0, mm=0, ss=0):
        super().__init__(hh, mm, ss)
        self.alarm_hh = 0
        self.alarm_mm = 0
        self.alarm_ss = 0
        self.alarm_setting = False

    def setAlarmTime(self, hh, mm, ss):
        self.alarm_hh = hh
        self.alarm_mm = mm
        self.alarm_ss = ss

    def alarm_on(self):
        self.alarm_setting = True

    def alarm_off(self):
        self.alarm_setting = False

    def run(self):
        while True:
            time.sleep(1)
            self.run_time()
            print(self.get_formatted_time(), "Alarm : ", self.formatted_alarm_time())

            if self.alarm_setting and self.get_alarm_time():
                print("ALARM!")
                break

    def formatted_alarm_time(self):
        return f"{self.alarm_hh:02}:{self.alarm_mm:02}:{self.alarm_ss:02}"

    def get_alarm_time(self):
        return self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss

clock = AlarmClock(0, 1, 55)
clock.setAlarmTime(0, 2, 5) 
clock.alarm_on()
clock.run()
