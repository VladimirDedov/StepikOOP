class Singleton:
    __instance = None
    __instance_s = None
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_s is None:
                cls.__instance_s=object.__new__(cls)
            return cls.__instance_s
        elif cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Game(Singleton):
    prev_name=False
    def __init__(self, name):
        if Game.prev_name is False:
            self.name=name
            Game.prev_name=True

class Game2(Singleton):
    prev_name=False
    def __init__(self, name):
        if Game2.prev_name is False:
            self.name=name
            Game2.prev_name=True


m = Game('1')
n = Game2('2')
b = Game2('2')
print(id(m), id(n), id(b))
print(m.name, n.name)
