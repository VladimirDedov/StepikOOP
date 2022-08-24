class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            self.__validate(i)
        super(ListInteger, self).__init__(lst)

    def __setitem__(self, key, value):
        self.__validate(value)
        super(ListInteger, self).__setitem__(key, value)

    def append(self, numb):
        self.__validate(numb)
        super(ListInteger, self).append(numb)

    @staticmethod
    def __validate(value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError
