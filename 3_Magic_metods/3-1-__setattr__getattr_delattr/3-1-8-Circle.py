class Circle:

    def __init__(self, x: 'int, float', y: 'int, float', radius: 'int, float, >0'):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __setattr__(self, key, value):
        if type(value) in (int, float):
            if key == "_Circle__radius" and value > 0:
                object.__setattr__(self, key, value)
            elif key in ['_Circle__x', '_Circle__y']:
                object.__setattr__(self, key, value)
        elif type(value) == str:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


circle = Circle(10.5, 7, 22)

circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
print(circle.x, circle.y, circle.radius, res)
