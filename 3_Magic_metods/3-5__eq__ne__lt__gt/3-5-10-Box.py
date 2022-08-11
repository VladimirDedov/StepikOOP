class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        if len(self.box) == len(other.box):
            box_1_indx = []
            box_2_indx = []

            for i in self.box:
                for b in other.box:
                    if i == b:
                        box_1_indx.append(self.box.index(i))
                        box_2_indx.append(other.box.index(b))
                        break

            if len(box_1_indx) == len(box_2_indx) and len(self.box) == len(box_1_indx):
                return True
            return False
        else:
            return False


class Thing:
    def __init__(self, name: str, mass: 'number'):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))


b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
print(res)
