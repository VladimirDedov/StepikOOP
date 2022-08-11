class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def get_lst(lst):
        res = []
        for i in lst:
            if type(i) in (int, float):
                res.append(i)
        return res

    def __add__(self, other):
        res = []
        for i in self.lst_math:
            res.append(i + other)
        return ListMath(res)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] += other
        return self

    def __sub__(self, other):
        res = []
        for i in self.lst_math:
            res.append(i - other)
        return ListMath(res)

    def __rsub__(self, other):
        res = []
        for i in self.lst_math:
            res.append(other-i)
        return ListMath(res)

    def __isub__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] -= other
        return self

    def __mul__(self, other):
        res = []
        for i in self.lst_math:
            res.append(i * other)
        return ListMath(res)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] *= other
        return self

    def __truediv__(self, other):
        res = []
        for i in self.lst_math:
            res.append(i / other)
        return ListMath(res)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] /= other
        return self


# lst = ListMath([1, "abc", -5, 7.68, True])
# lst = lst + 76  # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# print(lst.lst_math)
#
# lst = lst - 76  # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst  # вычитание из числа каждого числа списка
# lst -= 76.3
#
# lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
#
# lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst  # деление числа на каждый элемент списка
# lst /= 13.0
lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
print(res3.lst_math, res4.lst_math)
