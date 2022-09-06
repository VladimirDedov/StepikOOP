class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __init__(self):
        super(ShopGenericView, self).__init__()
    def __str__(self):
        lst=[]
        for key, value in self.__dict__.items():
            if key !='_id':
                lst.append(f'{key}: {str(value)}')
        return '\n'.join(lst)

class ShopUserView:
    def __init__(self):
        super(ShopUserView, self).__init__()
    def __str__(self):
        lst = []
        for key, value in self.__dict__.items():
            lst.append(f'{key}: {str(value)}')
        return '\n'.join(lst)

class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

class Shop(ShopItem,ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


# shop=Shop('OOP', 'Dedov', 2022)
# print(shop)


book = Book("Python ООП", "Балакирев", 2022)
print(book)

print(book.__dict__)
