class PhoneBook():
    __book = []

    def add_phone(self, phone):
        self.__book.append(phone)

    def remove_phone(self,indx):
        self.__book.pop(indx)

    def get_phone_list(self):
        return self.__book

class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
p.remove_phone(1)
print(phones)