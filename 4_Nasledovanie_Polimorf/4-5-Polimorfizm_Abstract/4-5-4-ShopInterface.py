class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    idd = 1

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = ShopItem.idd
        ShopItem.idd += 1

    def get_id(self):
        return self._id


l = ShopItem('fff', 1, 2)
print(l.get_id())
