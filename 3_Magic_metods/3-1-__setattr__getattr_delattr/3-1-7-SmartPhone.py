class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        flag = True
        for a in self.apps:
            if a.name != app.name:
                continue
            else:
                flag = False
        if flag:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)

app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
for a in app_3.phone_list:
    print(a)
