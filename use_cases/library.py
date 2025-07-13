class Library:

    def __init__(self) -> None:

        self.list_books = []
    
    def add_book(self, book):
        self.list_books.append(book)

    def list_available_books(self):

        available_books = [book for book in self.list_books if not book.is_borrowed]

        for book in available_books:
            print(f"The book '{book.title}' with author '{book.author}' has this status: '{book.is_borrowed}'")

    def list_all_books(self):
        
        for book in self.list_books:
            print(f" we have this book {book.title} in this library wrtitten by {book.author} and it's availability is {book.is_borrowed}")

    def get_book(self, name):

        for books_name in self.list_books:
            if name in books_name.title:
                print(f"the boook {books_name.title} author {books_name.author} {books_name.is_borrowed}")

    def borrow_book(self, title):

        for book in self.list_books:

            if title in book.title:
                book.borrow_book()
                print(f"The book {book.title} was borrowed")

    def return_book(self, title):

        for book in self.list_books:
            if title in book.title:
                book.return_book()
                print(f"the book {book.title} was returned correctly")
            

class Book:

    def __init__(self, title:str, author:str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed=True

    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"The book was returned")
        else:
            print(f"The book is no being borrowed")
    

    
if __name__ == "__main__":


    # book status
    book1 = Book('one hundred of solitude', 'gabriel garcia marquez')
    book2 = Book('Tom sawyer', 'mark tawin')

    # library:

    libreria_principal = Library() 

    libreria_principal.add_book(book1)
    libreria_principal.add_book(book2)
    
    
    libreria_principal.list_available_books()

    libreria_principal.borrow_book('one hundred of solitude')

    libreria_principal.list_available_books()

    libreria_principal.list_all_books()




