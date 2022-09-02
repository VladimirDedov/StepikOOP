from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass


    def get_info(self):
        return 'Базовый класс Model'

class ModelForm(Model):
    id = 1
    def __init__(self, login, password):
        self._login=login
        self._password=password
        self._id = ModelForm.id
        ModelForm.id += 1

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())