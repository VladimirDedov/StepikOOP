class IterColumn:
    def __init__(self, lst, column):
        self.lst=lst
        self.column=column
    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]

lst = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]
      ]
it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)