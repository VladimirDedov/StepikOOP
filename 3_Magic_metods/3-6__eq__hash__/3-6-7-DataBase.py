class Record:
    pk_lst = [1]

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio if type(fio) == str else None
        self.descr = descr if type(descr) == str else None
        self.old = int(old)
        self.pk = Record.pk_lst[-1] + 1
        Record.pk_lst.append(self.pk)

    def __eq__(self, other):
        return self.old == other.old and self.fio.lower() == other.fio.lower()

    def __hash__(self):
        return hash((self.fio.lower(), self.old))


class DataBase:
    def __init__(self, path):
        self.dict_db = {}
        self.path = path

    def write(self, record: Record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk: int):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


lst_in = [
    'Балакирев С.М.; программист; 33',
    'Балакирев С.М.; программист; 33',
    'Кузнецов А.В.; разведчик-нелегал; 35',
    'Суворов А.В.; полководец; 42',
    'Иванов И.И.; фигурант всех подобных списков; 26',
    'Балакирев С.М.; преподаватель; 37'
]


def get_list_word(st: str):
    fio, descr, old = st.split(';')
    return [fio, descr, old]


db = DataBase('path')

for st in lst_in:
    st = get_list_word(st)
    obj = Record(*st)
    db.write(obj)

print(db.read(2))
print(db.dict_db)
