import time


class Mechanical:
    flag = True

    def __init__(self, date):
        if self.flag:
            self.date = date
        self.flag = False

    def __setattr__(self, key, value):
        if self.flag:
            object.__setattr__(self, key, value)


class Aragon:
    flag = True

    def __init__(self, date):
        if self.flag:
            self.date = date
        self.flag = False

    def __setattr__(self, key, value):
        if self.flag:
            object.__setattr__(self, key, value)


class Calcium:
    flag = True

    def __init__(self, date):
        if self.flag:
            self.date = date
        self.flag = False

    def __setattr__(self, key, value):
        if self.flag:
            object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    lst_slots = {}

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and type(filter) == Mechanical and slot_num not in self.lst_slots:
            self.lst_slots[slot_num] = filter
        elif slot_num == 2 and type(filter) == Aragon and slot_num not in self.lst_slots:
            self.lst_slots[slot_num] = filter
        elif slot_num == 3 and type(filter) == Calcium and slot_num not in self.lst_slots:
            self.lst_slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if slot_num in self.lst_slots:
            del self.lst_slots[slot_num]

    def get_filters(self):
        return tuple(self.lst_slots.values())

    def water_on(self):
        if len(self.lst_slots) == 3:
            if type(self.lst_slots[1]) == Mechanical and type(self.lst_slots[2]) == Aragon and type(
                    self.lst_slots[3]) == Calcium:
                if 0 <= (time.time() - self.lst_slots[1].date) <= GeyserClassic.MAX_DATE_FILTER and 0 <= (
                        time.time() - self.lst_slots[1].date) <= GeyserClassic.MAX_DATE_FILTER and 0 <= (
                        time.time() - self.lst_slots[1].date) <= GeyserClassic.MAX_DATE_FILTER:
                    return True
        return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
print(my_water.get_filters())
print(time.time() - GeyserClassic.lst_slots[1].date)
print(my_water.water_on())
