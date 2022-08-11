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
l={}
l[1]=[1,1,2]
l[1][1]+=1
print(l)