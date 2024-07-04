class Book:
    price = 350

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def -
    ;__str__(self):
        return f'\nName: {self.title}\nAuthor: {self.author}'

book1 = Book('Crime and Punishment', 'Dostoevskiy')

print(book1)

class Manga(Book):
    price = 1350

    def __init__(self, title, author, imagesPerPage):
        Book.__init__(self, title, author)
        self.imagesPerPage = imagesPerPage

    def __str__(self):
        return f'{super(Book).__str__(self)}, \nImages per page: {self.imagesPerPage}'

    def reverse(self):
        print('Читаем справа налево.')

berserk = Manga('Berserk', 'H. P. Lovecraft', 2)

print(berserk)
berserk.reverse()