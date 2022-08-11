from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if self.get_int_float(real):
            self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if self.get_int_float(img):
            self.__img = img

    def get_int_float(self, val):
        if type(val) in (int, float):
            return True
        else:
            raise ValueError("Неверный тип данных.")
    def __abs__(self):
        return abs(sqrt(self.real*self.real + self.img*self.img))

cmp=Complex(7,8)
cmp.real=3
cmp.img=4
c_abs=abs(cmp)