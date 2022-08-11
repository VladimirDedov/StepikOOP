class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

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
        if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            object.__setattr__(self, key, value)

    def __le__(self, other):
        return self.a * self.b * self.c <= other.a * other.b * other.c

    def __lt__(self, other):
        return self.a * self.b * self.c < other.a * other.b * other.c

    def volume(self):
        return self.a*self.b*self.c

class ShopItem:
    def __init__(self, name: str, price: int, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
lst_shop_sorted=lst_shop.copy()
lst_shop_sorted=sorted(lst_shop_sorted, key=lambda x: x.dim.volume())
print([i.name for i in lst_shop_sorted])
d=Dimensions(2000, 600, 500)
d.c=12
