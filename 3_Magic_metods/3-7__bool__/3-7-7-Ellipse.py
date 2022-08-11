class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1 = args[0] if args[0] else None
            self.y1 = args[1] if args[1] else None
            self.x2 = args[2] if args[2] else None
            self.y2 = args[3] if args[3] else None
            self.flag = True
        else:
            self.flag = False

    def __bool__(self):
        return True if self.flag else False

    def get_coords(self):
        if self.flag:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(0, 0, 1, 1), Ellipse(1, 1, 2, 2)]
for i in lst_geom:
    if bool(i):
        i.get_coords()
d = Ellipse()
print(bool(d))
