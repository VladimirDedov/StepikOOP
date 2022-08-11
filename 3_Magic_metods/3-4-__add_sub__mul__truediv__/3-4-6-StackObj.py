class StackObj:
    prev_obj = None
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack:


    def __init__(self, top=None):
        self.top = top

    def push_back(self, obj):
        if self.top == None:
            self.top = obj
            StackObj.prev_obj = obj
        else:
            StackObj.prev_obj.next = obj
            StackObj.prev_obj = obj

    def pop_back(self):
        prev_prev = None
        h = 0
        obj = self.top
        while obj:
            if obj.next == None:
                prev_prev.next = None
                break
            prev_prev = obj
            obj = obj.next

    def __add__(self, other):
        StackObj.prev_obj.next = other
        StackObj.prev_obj = other
        return self

    def __mul__(self, other):
        if type(other) == list:
            for i in other:
                self.push_back(StackObj(i))
        return self

    def __iadd__(self, other):
        return self + other


st = Stack()
st.push_back(StackObj('uio'))
st = st + StackObj('sdf')
st += StackObj('qwe')
st = st * ['data_1', 'data_2', 'data_N']
