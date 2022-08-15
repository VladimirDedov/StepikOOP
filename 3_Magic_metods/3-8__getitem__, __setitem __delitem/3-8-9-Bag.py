class Thing:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, weight):
        self.max_weight = weight
        self.bag = []

    def add_thing(self, thing: Thing):
        if self.max_weight - thing.weight >= 0:
            self.bag.append(thing)
            self.max_weight -= thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def validate(self, indx):
        if -len(self.bag) <= indx < len(self.bag):
            return True
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        if self.validate(item):
            return self.bag[item]

    def __setitem__(self, key, value):
        if self.validate(key):
            if self.max_weight + self.bag[key].weight - value.weight >= 0:
                self.max_weight = self.max_weight + self.bag[key].weight - value.weight
                self.bag[key] = value
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        del self.bag[key]


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))
b[0] = Thing('рубашка', 500)
b[0] = Thing('рубашка', 800)

# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# #bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
# bag[2]=Thing('рубашка', 200)
# print(bag[2].name)  # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name)  # платок
# del bag[0]
# print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
