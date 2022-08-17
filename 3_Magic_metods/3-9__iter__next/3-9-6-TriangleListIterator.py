class TriangleListIterator:
    def __init__(self, lst=None):
        self.lst = lst if type(lst) == list else None

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]

    # def __next__(self):
    #     i = j = 0
    #     if i <len(self.lst) - 1:
    #         if j <= i:
    #             res = self.lst[i][j]
    #             if i == j:
    #                 self.validate_len(i)
    #                 i += 1
    #                 j = 0
    #             j += 1
    #         elif i == j and i == 0:
    #             res = self.lst[i][j]
    #             self.validate_len(i)
    #             i += 1
    #         return res
    #     else:
    #         raise StopIteration
    # def validate_len(self, i):
    #     if i == len(self.lst) - 1:
    #         raise IndexError



lst = [['x00'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32', 'x33']
       ]
it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
it_iter = iter(it)
x = next(it_iter)
