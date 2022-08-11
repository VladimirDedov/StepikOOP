class Vector:
    def __init__(self, *args):
        self.lst_coord = list(args)

    def __add__(self, other):
        lst = []
        if len(self.lst_coord) == len(other.lst_coord):
            for i in range(len(self.lst_coord)):
               lst.append( self.lst_coord[i] +other.lst_coord[i])
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*lst)

    def __sub__(self, other):
        lst = []
        if len(self.lst_coord) == len(other.lst_coord):
            for i in range(len(self.lst_coord)):
                lst.append(self.lst_coord[i] - other.lst_coord[i])
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*lst)

    def __mul__(self, other):
        lst = []
        if len(self.lst_coord) == len(other.lst_coord):
            for i in range(len(self.lst_coord)):
                lst.append(self.lst_coord[i] * other.lst_coord[i])
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*lst)

    def __iadd__(self, other):
        if type(other)== int:
            for i in range(len(self.lst_coord)):
                self.lst_coord[i]+=other
        else:
            if len(self.lst_coord) == len(other.lst_coord):
                for i in range(len(self.lst_coord)):
                    self.lst_coord[i]+=other.lst_coord[i]
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        return self

    def __isub__(self, other):
        if type(other) == int:
            for i in range(len(self.lst_coord)):
                self.lst_coord[i] -= other
        else:
            if len(self.lst_coord) == len(other.lst_coord):
                for i in range(len(self.lst_coord)):
                    self.lst_coord[i] -= other.lst_coord[i]
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        return self

    def __eq__(self, other):
        if len(self.lst_coord) == len(other.lst_coord):
            for i in range(len(self.lst_coord)):
                if self.lst_coord[i] == other.lst_coord[i]:
                    continue
                else:
                    return False
            return True
        else:
            return False

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).lst_coord)  # [5, 7, 9]
print((v1 - v2).lst_coord)  # [-3, -3, -3]
print((v1 * v2).lst_coord)  # [4, 10, 18]

v1 += 10
print(v1.lst_coord)  # [11, 12, 13]
v1 -= 10
print(v1.lst_coord)  # [1, 2, 3]
v1 += v2
print(v1.lst_coord)  # [5, 7, 9]
v2 -= v1
print(v2.lst_coord)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
