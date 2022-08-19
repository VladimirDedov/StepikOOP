class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class Stack:
    prev_obj = None

    def __init__(self):
        self.top = None

    def push_back(self, obj: StackObj):
        if self.top is None:
            self.top = obj
            Stack.prev_obj = obj
        else:
            Stack.prev_obj.next = obj
            Stack.prev_obj = obj

    def push_front(self, obj: StackObj):
        obj.next = self.top
        self.top = obj

    def validate(self, key: int):
        obj = self.top
        count = 0
        while True:
            if obj.next is None:
                break
            else:
                obj = obj.next
                count += 1
        if type(key) != int or key < 0 or key > count:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.validate(key)
        obj = self.top
        h = 0
        prev_obj = None
        while h != key:
            prev_obj = obj
            obj = obj.next
            h += 1
        obj.data = value

    def __getitem__(self, item):
        self.validate(item)
        if item == 0:
            return self.top.data
        else:
            obj = self.top
            h = 0
            while h != item:
                obj = obj.next
                h += 1
            return obj.data

    def __len__(self):
        obj = self.top
        len_stack = 0
        while True:
            if obj.next is None:
                len_stack += 1
                break
            obj = obj.next
            len_stack += 1
        return len_stack

    def __iter__(self):
        obj = self.top
        while True:
            if obj.next is None:
                break
            yield obj
            obj = obj.next
        yield obj


# st = Stack()
# st.push_back(StackObj('0'))
# st.push_back(StackObj('123'))
# st.push_back(StackObj('456'))
# st.push_front(StackObj('000'))
# st[1] = 123  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
# data = st[0]  # получение данных из объекта стека по индексу
# print(data)
# n = len(st)  # получение общего числа объектов стека
# print(f'len {n}')
#
# for obj in st:  # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль
st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
print(st[0])