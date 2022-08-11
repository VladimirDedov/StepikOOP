class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self, book_list=None):
        self.book_list = book_list if book_list and type(book_list) == list else []

    def __add__(self, other):
        if type(other) == Book:
            self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)

l=Lib()

book = Book('title', 'author', 'year')
book1 = Book('iii', 'ooo', 'ppp')
l=l+book
l+=book1
print(l.book_list)
l-=0
print(l.book_list[0].title)
print(len(l))