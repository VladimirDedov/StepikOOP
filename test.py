# class MotherBoard:
#     def __init__(self, name, cpu, total_mem_slots=4, *mem_slots ):
#         self.mem_slots=[]
#         self.name = name
#         self.cpu = cpu
#         for i in range(total_mem_slots):
#             print(mem_slots[i].name)
#             self.mem_slots.append(mem_slots[i].name)
#             self.mem_slots.append(mem_slots[i].volume)
#
#         print(mem_slots)
#
#         self.total_mem_slots = total_mem_slots
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
# mem1, mem2 = Memory('kingston', '2gb'), Memory('Kitai', '4gb')
# a=MotherBoard('name', 'pentium', 2, mem1, mem2)
# print(mem1.name)
# class Person:
#     name= 'Сергей Балакирев'
#     job= 'Программист'
#     city= 'Москва'
# p1=Person()
# print(p1.__dict__)
# f='job' in Person.__dict__
# print(f)
# lst={'a': 6}
# print(list(lst))
# from string import ascii_lowercase, digits
# t= ascii_lowercase+digits
# print(t)


# class Person:
#
#     def __init__(self, name, g, h):
#         self.__name = name
#         self.__g = g
#         self.__h = h
#
#
# @property
# def name(self):
#     return self.__name
#
#
# @name.setter
# def name(self, value, g, h):
#     self.__name = value
#     self.__g = g
#     self.__h = h
# b=map(int, ['1','2'])
# print(list(b))
# n={int(i) for i in range(3)}
# n= 5,5,6,'d'
# print(n)

class Geom:
    def __init__(self, width, color):
        if type(width) not in (int, float) or type(color) != str or width < 0:
            raise ValueError('неверные параметры фигуры')

        self._width = width
        self._color = color


class Ellipse(Geom):
    def __init__(self, x1, y1, x2, y2, width=1, color='red'):
        super().__init__(width, color)

        if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
            raise ValueError('неверные координаты фигуры')

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _is_valid(self, x):
        return type(x) in (int, float)

try:
    x1, y1, x2, y2, w = map(float, input().split())
    el = Ellipse(x1, y1, x2, y2, w)
except ValueError as e:
    print(e)