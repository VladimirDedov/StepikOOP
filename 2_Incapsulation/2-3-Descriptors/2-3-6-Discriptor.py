class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (float,):
            setattr(instance, self.name, value)
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell()] * m for i in range(n)]


table = TableSheet(5, 3)
count = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j] = Cell(count)
        count += 1.0


for i in range(5):
    for j in range(3):
        print(table.cells[i][j].value, end=' ')
    print()