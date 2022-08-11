class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (str,) and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, min_length=0, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and self.min_length <= value <= self.max_length:
            setattr(instance, self.name, value)
        else:
            setattr(instance, self.name, None)


class SuperShop:
    def __init__(self, name, goods=[]):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price=None):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
s = Product("Курс по Python", 0)
shop.add_product(s)
shop.add_product(Product("Курс по Python ООП", 2000))
shop.add_product(Product("Курс по Python ООП", 3000))

for p in shop.goods:
    print(f"{p.name}: {p.price}")
