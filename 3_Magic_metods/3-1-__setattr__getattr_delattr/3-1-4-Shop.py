class Product:
    count = 1

    def __init__(self, name='', weight=0, price=0):
        self.id = Product.count
        Product.count = 1 + Product.count
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name':
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                object.__setattr__(self, key, value)
        elif key == 'weight' or key == 'price':
            if type(value) not in (int, float) or value<0:
                raise TypeError("Неверный тип присваиваемых данных")
            else:
                object.__setattr__(self, key, value)
        elif key == 'id':
            if type(value) != int:
                raise TypeError("Неверный тип присваиваемых данных")
            else:
                object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


class Shop:
    def __init__(self, name_shop: str, goods=[]):
        self.goods = goods
        self.name_shop = name_shop

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
del(book.id)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, {p.id}")
