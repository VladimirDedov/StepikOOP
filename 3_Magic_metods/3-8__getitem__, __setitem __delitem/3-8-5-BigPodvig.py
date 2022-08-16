class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value: int = 0):
        self.value = start_value

    def __setattr__(self, key, value):

        if type(value) not in (int,):
            raise ValueError('возможны только целочисленные значения')
        else:
            object.__setattr__(self, key, value)


class TableValues:
    def __init__(self, rows: int, cols: int, cell=CellInteger):
        self.cell = cell
        self.rows = rows
        self.cols = cols
        self.cells = self.create_tuple()


    def create_tuple(self):
        if self.cell != CellInteger:
            raise ValueError('параметр cell не указан')
        tmp_list = []
        list_to_tuple = []
        for i in range(self.rows):
            for j in range(self.cols):
                tmp_list.append(self.cell())
            list_to_tuple.append(tuple(tmp_list))
            tmp_list.clear()
        return tuple(list_to_tuple)

    def __setitem__(self, key, value):
        i,j=key
        if type(value) != int:
            raise ValueError('параметр cell не указан')
        self.cells[i][j].value=value

    def __getitem__(self, item):
        i, j = item
        return self.cells[i][j].value




table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[0, 0] = 1
c=CellInteger(10)
print(c.value)


# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
