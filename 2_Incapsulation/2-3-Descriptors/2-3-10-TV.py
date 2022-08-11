class String:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class TVProgram:
    def __init__(self, channel):
        self.channel = channel
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for item in self.items:
            if item.uid==indx:
                self.items.remove(item)



class Telecast:

    def __init__(self, uid, name, duration):
        self.uid = uid
        self.name=name
        self.duration=duration

    @property
    def uid(self):
        return self.__id
    @uid.setter
    def uid(self, id):
        self.__id=id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

pr.remove_telecast(3)
for t in pr.items:
    print(f"{t.name}: {t.duration}")