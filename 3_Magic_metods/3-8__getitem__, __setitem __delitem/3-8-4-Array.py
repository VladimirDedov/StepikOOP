class Array:
    def __init__(self, max_length, cell):
        self._max_length = max_length
        self._cell = cell
        self.lst = [self._cell() for _ in range(self._max_length)]

    def is_value(self, value):
        if type(value) != int or  value<0 or value >= self._max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.is_value(item)
        return self.lst[item].value

    def __setitem__(self, key, value):
        self.is_value(key)
        self.lst[key].value = value

    def __repr__(self):
        st = [str(s.value) for s in self.lst]
        return ' '.join(st)


class Integer:
    def __init__(self, start_value=0):
        self._start_value = start_value

    @property
    def value(self):
        return self._start_value

    @value.setter
    def value(self, set_value):
        self._start_value = set_value

    def __setattr__(self, key, value):
        if type(value) not in (int,):
            raise ValueError('должно быть целое число')
        else:
            object.__setattr__(self, key, value)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int[1])
ar_int[1] = 10
#ar_int[1] = 10.5  # должно генерироваться исключение ValueError
#ar_int[10] = 1  # должно генерироваться исключение IndexError
print(ar_int)