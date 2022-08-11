class Server:

    def __init__(self, buffer=[]):
        if Router.lst_server:
            self.ip = Router.lst_server[-1].ip + 1
            Router.link(self)
        else:
            self.ip = 1
            Router.link(self)
        self.buffer = buffer

    def send_data(self, data):
        """для отправки объекта класса Data с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer)"""
        Router.buffer.append(data)
        self.buffer=''

    @staticmethod
    def get_data():
        """возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и
        очищает входной буфер;"""
        lst = []
        for i in range(len(Router.lst_server)):
            if Router.lst_server[i].buffer:
                lst.append(Router.lst_server[i].buffer)
        Router.buffer.clear()
        Router.lst_server.clear()
        return lst

    def get_ip(self):  # Сделано
        """возвращает свой IP-адрес"""
        return self.ip


class Router:
    buffer = []  # список для хранения списка объектов класса Data
    lst_server = []  # список для хранения списка серверов

    @classmethod
    def link(cls, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        (для простоты, каждый сервер соединен только с одним роутером);"""
        cls.lst_server.append(server)

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера"""
        self.buffer.remove(server)

    @classmethod
    def send_data(cls):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться"""
        for i in range(len(cls.lst_server)):
            for j in range(len(cls.buffer)):
                if cls.lst_server[i].ip == cls.buffer[j].ip:
                    print(f'buffer {cls.lst_server[i].buffer}')
                    print(f'data {cls.buffer[j].data}')
                    cls.lst_server[i].buffer = cls.buffer[j].data



class Data:  # Сделано
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from1 = Server()  # Создать  сервер sv_from1 с ip = 1 и пустым буфером

router.link(sv_from1)  # Создать  линк с сервером sv_from1 с ip = 1 с пустым буфером

router.link(Server())  # Создать линк с сервером с  ip = 3

sv_to = Server()  # Создаем сервер куда передаем
router.link(sv_to)  # Соединяем роутер с сервером sv_to ip = 5

print(f' ip = {sv_from1.get_ip()}')

sv_from1.send_data(Data("Hello", sv_to.get_ip()))  # передаем буфер от сервера к роутеру

sv_to.send_data(Data("Hi", sv_from1.get_ip()))
router.send_data()  # отправка буффера роута к серверам по ip
msg_lst_from = sv_from1.get_data()
msg_lst_to = sv_to.get_data()
print(f'fff {sv_from1.buffer}')
