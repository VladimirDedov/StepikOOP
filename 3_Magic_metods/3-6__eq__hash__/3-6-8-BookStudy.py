class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = int(year)

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


def get_list_word(st: str):
    fio, descr, old = st.split(';')
    return [fio, descr, old]


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021'
]

lst_bs = []
lst_hash = []

for book in lst_in:
    lst_book = get_list_word(book)
    b = BookStudy(*lst_book)
    lst_bs.append(b)
    lst_hash.append(hash(b))
unique_books=len(set(lst_hash))

print(lst_bs[0]==lst_bs[3])
print(lst_hash)
print(unique_books)
