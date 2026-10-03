class Books: 
    title = ''
    author = ''
    price =''

    def set_book_info(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self): 
        print(f'TITLE: {self.title}, AUTHOR: {self.author}, PRICE: {self.price}BDT')

my_book1 = Books()
my_book2 = Books()
my_book1.set_book_info('1984', 'George Orwell', 250)
my_book2.set_book_info('Harry Potter', 'J.K. Rowling', 450)
my_book1.display_info()
my_book2.display_info()
