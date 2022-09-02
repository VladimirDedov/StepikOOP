from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    prev_obj = None

    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
            Stack.prev_obj = obj
        else:
            Stack.prev_obj._next = obj
            Stack.prev_obj = obj

    def pop_back(self):
        link=None
        #Stack.flag = True
        obj = prev = self._top
        if self._top._next == None:
            link = self._top
            self._top = None
        else:
            while True:
                if obj._next == None:
                    prev._next = None
                    link=obj
                    obj = None
                    break
                prev = obj
                obj = obj._next
        return link

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"

st = Stack()
st.push_back(StackObj("obj 1"))

del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj, st._top)