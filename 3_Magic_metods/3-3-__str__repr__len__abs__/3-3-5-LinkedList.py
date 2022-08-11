class ObjList:
    def __init__(self, data):
        self.__date = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__date

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class LinkedList:
    obj_lst = []

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
            LinkedList.obj_lst.append(obj)

        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj
            LinkedList.obj_lst.append(obj)

    def remove_obj(self, indx):

        obj = LinkedList.obj_lst[indx]

        p, n = obj.prev, obj.next
        if obj is None:
            return
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p
        LinkedList.obj_lst.pop(indx)

    def __len__(self):
        return len(LinkedList.obj_lst)

    def __call__(self, indx, *args, **kwargs):
        return LinkedList.obj_lst[indx].data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev
print(n)
print(s)
n = 0
h = linked_lst.head
while h:
    print(n)
    h = h._ObjList__next
    n += 1
