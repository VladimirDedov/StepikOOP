class IteratorAttrs:
    def __iter__(self):
        for i in self.__dict__:
            yield i, self.__dict__[i]


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('model', 'size', 'memory')
for attr, value in phone:
    print(attr, value)

print(phone.__dict__)