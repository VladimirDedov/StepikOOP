class Clock:
    def __init__(self, time=0):
        self.__time = 0

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
        print(self.__time)

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(tm):
        return type(tm) in (int,) and 0 <= tm < 100000


clock = Clock()
clock.set_time(4530)
