class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    def __init__(self, x=0, y=0):
        self.__x=self.__y=0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if RadiusVector2D.valid(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if RadiusVector2D.valid(y):
            self.__y = y
    @classmethod
    def valid(cls, val):
        if type(val) in (int, float) and cls.MIN_COORD <=val <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(vector):
        return vector.x*vector.x+vector.y*vector.y

v=RadiusVector2D(-101, 1025)
print(RadiusVector2D.norm2(v))
v.x=1025
v.y = -101
print(RadiusVector2D.norm2(v))
print(v.x, v.y)