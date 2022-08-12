class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        if type(item) in (slice,):
            return self.coords[item]
        else:
            return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key]=value

v = RadiusVector(1, 2, 3)
coords_1 = v[0:2]
print(v.coords)
print(coords_1)
