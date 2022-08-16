class Cell:
    def __init__(self, value: "any type"):
        self.value = value


class SparseTable:
    def __init__(self, rows: int = 0, cols: int = 0):
        self.rows = rows
        self.cols = cols
        self.dict_cell = {}

    def add_data(self, row: int, col: int, data: Cell):
        self.dict_cell[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        self.validate(row, col)
        del self.dict_cell[(row, col)]
        self.update_index()

    def __getitem__(self, item):
        if item in self.dict_cell:
            return self.dict_cell[(item[0], item[1])].value
        else:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        if key in self.dict_cell:
            self.dict_cell[(key)] = Cell(value)
        else:
            self.dict_cell[(key)] = Cell(value)
            self.update_index()


    def update_index(self):
        self.rows = max(key[0] for key in self.dict_cell)+1
        self.cols = max(key[1] for key in self.dict_cell)+1

    def validate(self, row, col):
        if (row, col) in self.dict_cell:
            return True
        else:
            raise IndexError('ячейка с указанными индексами не существует')


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
# print(st.rows, st.cols)
# st.add_data(0, 0, Cell("cell_00"))
#
# st[2, 5] = 25  # изменение значения существующей ячейки

st[11, 7] = 'cell_117'  # создание новой ячейки
print(st.rows, st.cols)
# print(st.dict_cell)  # cell_00
# # st.remove_data(2, 5)
# print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5]  # ValueError
# st.remove_data(12, 3)  # IndexError
# print(st.rows, st.cols)
