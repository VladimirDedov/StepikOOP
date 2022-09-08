# здесь объявляйте класс SingletonFive
class SingletonFive:
    count =0
    __instanse= None
    def __new__(cls, *args, **kwargs):
        cls.count += 1
        if cls.count < 6:
            cls.__instanse =super().__new__(SingletonFive)
            return cls.__instanse
        return cls.__instanse

    def __init__(self, name):
            self.name = name
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
