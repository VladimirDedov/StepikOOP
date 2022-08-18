class Animal:
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: int):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'


cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())
dog=Dog('пёс', 4, 'хаски', (2, 3))
print(dog.get_info())
