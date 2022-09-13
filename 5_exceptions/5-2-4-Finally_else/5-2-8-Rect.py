class Rect:
    def __init__(self, x, y, width, height):
        if x not in (int, float) or y not in (int, float) or width < 0 or height < 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):

r=Rect(0,1,-2 ,2)