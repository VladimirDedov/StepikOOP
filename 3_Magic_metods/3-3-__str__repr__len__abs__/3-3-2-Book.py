class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'


book = Book('Python ООП',
            'Балакирев С.М.',
            1024)

print(book)