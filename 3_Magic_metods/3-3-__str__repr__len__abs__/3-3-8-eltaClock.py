class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        d=self.__len__()
        h=d//3600
        m=d%3600//60
        s=d%3600%60
        return f'{h:02}: {m:02}: {s:02}'
    def __len__(self):
        result = (self.clock1.hours - self.clock2.hours) * 3600 + (
                self.clock1.minutes - self.clock2.minutes) * 60 + self.clock1.seconds - self.clock2.seconds

        if result < 0:
            result = 0
        return result

    @staticmethod
    def bool_time(val, flag = True):
        if 0 <= val < 10 and flag:
            return str(val) + '0'
        elif 0 <= val < 10 and flag ==False:
            return '0'+str(val)
        else:
            if val < 0:
                return '00'
            else:
                return str(val)


class Clock:
    def __init__(self, hours, minutes, seconds):
        if self.bool_number(hours) and self.bool_number(minutes) and self.bool_number(seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def bool_number(val):
        if type(val) in (int,) and val >= 0:
            return True
        else:
            return False
