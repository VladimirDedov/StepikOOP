class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        if a > b + c or b > a + c or c > a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    @staticmethod
    def validate(value):
        if value not in (int, float) and value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return True

    def __setattr__(self, key, value):
        if Triangle.validate(value):
            object.__setattr__(self, key, value)
        else:
            TypeError('стороны треугольника должны быть положительными числами')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []

for ls in input_data:
    try:
        lst_tr.append(Triangle(*ls))
    except:
        a = 1

print(lst_tr)
