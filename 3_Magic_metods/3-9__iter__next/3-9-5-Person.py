class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst=[fio, job, old, salary, year_job]


    def validate(self, indx):
        if 0 <= indx < 5:
            return True
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.validate(key)
        self.lst[key]=value

    def __getitem__(self, item):
        self.validate(item)
        return self.lst[item]



pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
