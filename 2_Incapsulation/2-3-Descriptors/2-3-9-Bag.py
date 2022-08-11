class Bag:
    w_summ = 0
    def __init__(self, weight):
        self.max_weight = weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):

        if Bag.w_summ + thing.weight <= self.max_weight:
            Bag.w_summ += thing.weight
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    @classmethod
    def get_total_weight(cls):
        return cls.w_summ


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

bag = Bag(80)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
print(f"Вес вещей {w}")
