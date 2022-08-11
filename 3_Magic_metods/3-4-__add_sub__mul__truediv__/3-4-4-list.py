class NewList:
    def __init__(self, lst=None):
        self.lst = lst.copy() if lst and type(lst) == list else []

    def get_list(self):
        return self.lst

    def __rsub__(self, other):
        return NewList(self.diff_list(other, self.lst))

    def __sub__(self, other):
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.diff_list(self.lst, other_list))

    @staticmethod
    def diff_list(lst_1, lst_2):
        sub = lst_2.copy()
        return [x for x in lst_1 if not NewList.is_elem(x, sub)]

    @staticmethod
    def is_elem(val, sub_lst):
        res = any(map(lambda xx: type(val) == type(xx) and val == xx, sub_lst))
        if res:
            sub_lst.remove(val)
        return res


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.get_list())
