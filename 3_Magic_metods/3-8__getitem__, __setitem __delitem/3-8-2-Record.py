class Record:
    def __init__(self,  **kwargs ):
        self.__dict__.update(kwargs)
        self.total_attrs = len(kwargs)
        self.attrs=tuple(self.__dict__.keys())


    def __setitem__(self, key, value):
        if type(key) not in (int,) or not (-self.total_attrs <= key < self.total_attrs):
            raise IndexError('неверный индекс поля')
        setattr(self, self.attrs[key], value)

    def __getitem__(self, item):
        if type(item) not in (int,) or not (-self.total_attrs <=item< self.total_attrs):
            raise IndexError('неверный индекс поля')
        return getattr(self, self.attrs[item])

r = Record(pk=1, title='Python ООП', author='Балакирев')
r.name='wewe'
r[1]='Dedov'
print(r[1], r.name)