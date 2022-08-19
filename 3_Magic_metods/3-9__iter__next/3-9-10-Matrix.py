class Matrix:
    def __init__(self, *args):
        if type(args[0]) == list:
            self.matrix = args[0]
            self.rows=len(self.matrix)
            for line in self.matrix:
                count = 0
                for col in line:
                    count += 1
                break
            self.cols=count
        else:
            self.rows, self.cols, self.fill_value = args[0], args[1], args[2]
            self.matrix = self.create_matrix()

    def create_matrix(self):
        lst_row = [self.fill_value for i in range(self.cols)]
        res_lst_matrix = [lst_row for i in range(self.rows)]
        return res_lst_matrix

    @staticmethod
    def is_number(numb):
        if type(numb) not in (int, float):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __setattr__(self, key, value):
        if type(value) == list:
            lst = value
            len_col = len(lst[0])  # число строк
            for line in lst:
                count = 0
                for col in line:
                    count += 1
                    self.is_number(col)
                if len_col == count:
                    continue
                else:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        elif type(value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        return object.__setattr__(self, key, value)



    def validate_matrix(self, other):
        if len(self.matrix) == len(other.matrix):
            tuple_matrix = zip(self.matrix, other.matrix)
            for line in tuple_matrix:
                if len(line[0]) != len(line[1]):
                    raise ValueError('операции возможны только с матрицами равных размеров')
        else:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        col = 0
        res_lst = []
        for line in self.matrix:
            for j in line:
                col += 1
            break
        if type(other) == Matrix:
            self.validate_matrix(other)
            for i in range(len(self.matrix)):
                lst = []
                for j in range(col):
                    lst.append(self.matrix[i][j] + other.matrix[i][j])
                res_lst.append(lst[:])
        else:
            for i in range(len(self.matrix)):
                lst = []
                for j in range(col):
                    lst.append(self.matrix[i][j] + other)
                res_lst.append(lst[:])

        return Matrix(res_lst)

    def __sub__(self, other):
        col = 0
        res_lst = []
        for line in self.matrix:
            for j in line:
                col += 1
            break
        if type(other) == Matrix:
            self.validate_matrix(other)
            for i in range(len(self.matrix)):
                lst = []
                for j in range(col):
                    lst.append(self.matrix[i][j] - other.matrix[i][j])
                res_lst.append(lst[:])
        else:
            for i in range(len(self.matrix)):
                lst = []
                for j in range(col):
                    lst.append(self.matrix[i][j] - other)
                res_lst.append(lst[:])

        return Matrix(res_lst)

    def value_indx(self, indx):
        i, j = indx
        if not (0 <= i < self.rows) or not (0 <= j < self.cols):
            raise IndexError('недопустимые значения индексов')
        return i, j

    def __getitem__(self, item):

        i, j = self.value_indx(item)
        return self.matrix[i][j]

    def __setitem__(self, key, value):
        i, j = self.value_indx(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[i][j] = value



l = [
    [2, 2],
    [3, 4]
]
l2 = [
    [2, 3],
    [3, 4]
]
match=Matrix(l)
matrix = Matrix(4, 5, 10)
matrix[3,4]=5
print(matrix.matrix)
print(matrix[3,4], 'hj')

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"
list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"