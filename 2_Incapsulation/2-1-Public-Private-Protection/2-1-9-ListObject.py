class LinkedList:
    data_lst=[]
    prev_obj = None

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
            LinkedList.prev_obj = obj
            LinkedList.data_lst.append(obj.get_data())
        else:
            obj.set_prev(LinkedList.prev_obj)
            LinkedList.prev_obj.set_next(obj)
            LinkedList.prev_obj = obj
            self.tail = obj
            LinkedList.data_lst.append(obj.get_data())

    def remove_obj(self):
        LinkedList.prev_obj.next = None
        self.tail = LinkedList.prev_obj

    def get_data(self):
        lst=[]
        lst=LinkedList.data_lst.copy()
        LinkedList.data_lst.clear()
        return lst


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList(1))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
print(res)
ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
print(ls_one.get_data())