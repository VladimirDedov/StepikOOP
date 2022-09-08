class AppStore:
    lst_app = []

    @classmethod
    def add_application(cls, app):
        cls.lst_app.append(app)


    @classmethod
    def remove_application(cls, app):
        cls.lst_app.remove(app)

    def block_application(self, app):
        indx=AppStore.lst_app.index(app)        
        AppStore.lst_app[indx].blocked=True

    @classmethod
    def total_apps(cls):
        return len(cls.lst_app)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)

print(app_youtube.blocked)
print(store.total_apps())
print(AppStore.lst_app)
