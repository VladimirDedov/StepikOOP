class Cart:

    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        lst = []
        for i in self.goods:
            lst.append(f'{i.name}: {i.price}')
        return lst


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV('samsung', 1500))
cart.add(TV('lg', 500))
cart.add(Table('sss', 1500))
cart.add(Notebook('ddd', 500))
cart.add(Notebook('sdsd', 500))
cart.add(Cup('sdsd', 500))
print(cart.get_list())
