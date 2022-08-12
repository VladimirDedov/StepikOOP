class Track:
    def __init__(self, start_x, start_y):
        self._start_x = start_x
        self._start_y = start_y
        self.speed = None
        self.lst = []

    def add_point(self, x, y, speed):
        self.lst.append([(x, y), speed])

    def __getitem__(self, item):
        if 0 <= item < len(self.lst) and type(item) == int:
            return [self.lst[item][0], self.lst[item][1]]
        else:
            raise IndexError('некорректный индекс')


    def __setitem__(self, key, value):
        if 0 <= key < len(self.lst) and type(key) == int:
            self.lst[key][1] = value
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]  # IndexError
