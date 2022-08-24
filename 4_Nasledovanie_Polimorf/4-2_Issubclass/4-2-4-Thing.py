class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __str__(self):
        return self.name


class DictShop(dict):
    def __init__(self, things: dict = None):
        self.things = {} if things is None else things
        if type(self.things) != dict:
            raise TypeError('аргумент должен быть словарем')
        for key in self.things.keys():
            if not issubclass(type(key), Thing):
                raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(self.things)

    def __setitem__(self, key, value):
        if not issubclass(type(key), Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
print(th_1)
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

# dict_things[1] = th_1  # исключение TypeError
