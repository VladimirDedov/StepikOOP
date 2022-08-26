class ItemAttrs:
    def __init__(self, x, y):
        self.lst = [x, y]

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key]=value


class Point(ItemAttrs):
    def __init__(self, x, y):
        super(Point, self).__init__(x,y)

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
print(x,y, pt[0])
pt[0] = 10
print(x,y, pt[0])