class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        if type(next_obj) == StackObj or next_obj == None:
            self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    prev_obj = None
    flag = True
    def __init__(self, top=None):
        self.top=top

    def push(self, obj):
        if Stack.flag:
            self.top = obj
            Stack.flag = False
        else:
            if self.top.next == None:
                self.top.next = obj
                Stack.prev_obj = obj
            else:
                Stack.prev_obj.next = obj
                Stack.prev_obj = obj

    def get_data(self):
        if self.top==None:
            return []
        obj = self.top
        lst_res = []
        while True:
            lst_res.append(obj.data)
            if obj.next == None:
                break
            obj = obj.next
        return lst_res

    def pop(self):
        Stack.flag=True
        obj=prev = self.top
        if self.top.next==None:
            self.top = None
        else:
            while True:
                if obj.next == None:
                    prev.next=None
                    obj=None
                    break
                prev = obj
                obj = obj.next
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.push(StackObj("obj4"))
st.pop()
st.pop()


res = st.get_data()

print(res)
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
print(s.get_data())