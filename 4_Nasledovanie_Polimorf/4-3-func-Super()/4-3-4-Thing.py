class Thing:
    def __init__(self, name: str, weight: int):
        self.name=name
        self.weight=weight

class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super(ArtObject, self).__init__(name, weight)
        self.author=author
        self.date=date

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super(Computer, self).__init__(name, weight)
        self.memory = memory
        self.cpu = cpu

class Auto(Thing):
    def __init__(self, name, weight,dims):
        super(Auto, self).__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super(Mercedes, self).__init__(name, weight, dims)
        self.model=model
        self.old=old
class Toyota(Auto):
    def __init__(self,name, weight, dims, model, wheel):
        super(Toyota, self).__init__(name, weight, dims)
        self.model=model
        self.wheel=wheel

t=Toyota('avensiz', 205, 4, 'hach', 4 )
print(t.__dict__)