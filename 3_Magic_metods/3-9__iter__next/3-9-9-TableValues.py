class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    def __init__(self, rows: int, cols: int, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.lst_table = self.create_table()

    def create_table(self):
        lst = [Cell() for i in range(self.cols)]
        res_lst = [lst for i in range(self.rows)]
        return res_lst

    def __setitem__(self, key, value):
        i, j = self.validate_indx(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

        self.lst_table[i][j].data = value

    def __getitem__(self, item):
        i, j = self.validate_indx(item)
        return self.lst_table[i][j].data

    def validate_indx(self, indx):
        i, j = indx
        if type(i) != int or type(j) != int or i > self.rows - 1 or j > self.cols - 1:
            raise IndexError('неверный индекс')
        return i, j

    def __iter__(self):
        for row in self.lst_table:
            yield (x.data for x in row)


table = TableValues(3, 2, int)
table[1, 1] = 3  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[1, 1]  # считывание значения из ячейки с индексами row, col
print(value)
for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
