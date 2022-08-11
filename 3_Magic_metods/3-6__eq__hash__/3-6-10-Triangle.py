from math import sqrt


class Value:

    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (float, int) and value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = Value()
    b = Value()
    c = Value()

    def __init__(self, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
    def __len__(self):
        return int(self.a + self.b+self.c)

    def __call__(self):
        p=int((self.a + self.b+self.c)/2)
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

b = Triangle(10, 1, 1)
print(b.tr(), len(b))
