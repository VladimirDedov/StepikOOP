import math


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coord_lst = tuple([0] * args[0])
        else:
            self.coord_lst = tuple(args)


    def set_coords(self, *args):
        if len(self.coord_lst)<len(args):
            self.coord_lst=args[:len(self.coord_lst)]
        elif len(self.coord_lst)>len(args):
            self.coord_lst=args[:len(args)]+self.coord_lst[len(self.coord_lst)-1:]
        else:
            self.coord_lst = args


    def get_coords(self):
        return self.coord_lst

    def __len__(self):
        return len(self.coord_lst)

    def __abs__(self):
        res=0
        for i in self.coord_lst:
            res+=i*i
        return math.sqrt(res)

vector3D = RadiusVector(3)
#print(vector3D.coord_lst)
vector3D.set_coords(3, -5.6, 8)
#print(vector3D.coord_lst)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются

vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.coord_lst)
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)
print()