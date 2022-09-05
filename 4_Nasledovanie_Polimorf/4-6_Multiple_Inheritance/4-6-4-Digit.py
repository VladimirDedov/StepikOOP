class Digit:
    def __init__(self, value):
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) in (int,):
            super(Integer, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        if type(value) in (float,):
            super(Integer, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        if value > 0:
            super(Integer, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        if value < 0:
            super(Integer, self).__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')

class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass



