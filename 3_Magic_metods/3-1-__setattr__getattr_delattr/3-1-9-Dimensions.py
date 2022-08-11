class Dimensions :
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    def __init__(self, a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self,a):
        self.__a=a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def __setattr__(self, key, value):
        if Dimensions.MIN_DIMENSION<=value<=Dimensions.MAX_DIMENSION:
            if key!='MIN_DIMENSION' and key!='MAX_DIMENSION':
                object.__setattr__(self, key, value)
            else:
                raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError
print(d.MAX_DIMENSION)
