class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class Stack:
    prev_obj = None

    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            Stack.prev_obj = obj
        else:
            Stack.prev_obj.next = obj
            Stack.prev_obj = obj

    def pop(self):
        obj = self.top
        while True:
            if obj.next is None:
                prev_obj.next=None
                return obj
            else:
                prev_obj=obj
                obj = obj.next

    def __getitem__(self, item):
        self.validate(item)
        if item == 0:
            return self.top
        else:
            obj = self.top
            h = 0
            while h != item:
                obj = obj.next
                h += 1

            return obj

    def validate(self, key):
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
        prev_obj=None
        while h != key:
            prev_obj=obj
            obj = obj.next

            h += 1
        if obj.next is not None:
            obj_next = obj.next
        obj = value
        prev_obj.next=obj
        obj.next = obj_next



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
print(st[1].data)  # new obj2
st.pop()
print(st[2].data)
# res = st[3] # исключение IndexError
