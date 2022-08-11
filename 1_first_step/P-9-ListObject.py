import sys

lst_in = [
    '1. Первые шаги в ООП',
    '1.1 Как правильно проходить этот курс',
    '1.2 Концепция ООП простыми словами',
    '1.3 Классы и объекты. Атрибуты классов и объектов'
]


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


head_obj = ListObject(lst_in[0])
obj = head_obj

for i in range(1, len(lst_in)):
    obj_next = ListObject(lst_in[i])
    obj.link(obj_next)
    obj = obj_next
