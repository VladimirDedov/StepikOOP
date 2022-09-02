class Track:
    def __init__(self, *args):
        self.__points = []
        if type(args[0]) != PointTrack:
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            for i in args:
                if type(i) == PointTrack:
                    self.__points.append(i)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        if type(pt)==PointTrack:
            self.__points.append(pt)

    def add_front(self, pt):
        if type(pt) == PointTrack:
            self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)

    def print_points(self):
        print(self.__points)


class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
t=Track(2,4)
pt = PointTrack(1, 2)
t.add_front(pt)
t.pop_front()
print(t.points)

print(pt)  # PointTrack: 1, 2

tr.print_points()
