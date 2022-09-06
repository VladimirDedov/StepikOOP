class Digit:
    def __init__(self, value):
        print('Вызов Digit')
        if type(value) in (int, float):
            self.value = value
        else:
            raise TypeError('значение не соответствует типу объекта')

class Integer(Digit):
    def __init__(self, value):
        print('Вызов Integer')
        if type(value) in (int,):
            super(Integer, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        print('Вызов Float')
        if type(value) in (float,):
            super(Float, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        print('Вызов Positive')
        if value > 0:
            super(Positive, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        print('Вызов Negative')
        if value < 0:
            super(Negative, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):

    def __init__(self, value):
        print('Вызов PrimeNumber')
        super(PrimeNumber, self).__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        print('Вызов FloatPositive')
        super(FloatPositive, self).__init__(value)


p1, p2, p3 = PrimeNumber(12), PrimeNumber(11), PrimeNumber(2)
f1, f2, f3, f4, f5 = FloatPositive(1.1), FloatPositive(2.2), FloatPositive(3.3), FloatPositive(1.4), FloatPositive(1.5)

digits = [p1, p2, p3, f1, f2, f3, f4, f5]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

lst_p = list(filter(lambda x: isinstance(x, PrimeNumber), digits))
print(isinstance(p1, PrimeNumber))

print(lst_float)
