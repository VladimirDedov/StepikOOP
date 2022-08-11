class PolyLine:
    def __init__(self, start_coord, *args):
        self.lst_coords=[]
        self.lst_coords.append(start_coord)
        self.lst_coords += args

    def add_coord(self, x, y):
        self.lst_coords.append((x, y))

    def remove_coord(self, indx):
        self.lst_coords.pop(indx)

    def get_coords(self):
        return self.lst_coords

p=PolyLine((1,2), (4,5), (6,7))
p.add_coord(7,8)
p.remove_coord(2)
print(p.get_coords())