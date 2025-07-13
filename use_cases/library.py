# Design a small system using OOP that manages books in a library. Your system should be able to:
# 	1.	Add new books to the library.
# 	2.	Borrow a book (mark it as borrowed).
# 	3.	Return a book (mark it as available again).
# 	4.	List all available books.

# Requirements:
# 	•	Each book must have at least a title, an author, and a status (available/borrowed).
# 	•	You must use at least two classes.
# 	•	Apply the principles of encapsulation and responsibility delegation.


class Library:

    def __init__(self) -> None:

        self.list_books = []
    
    def add_book(self, book):
        self.list_books.append(book)

    def list_available_books(self):

        available_books = [book for book in self.list_books if not book.is_borrowed]

        for book in available_books:
            print(f"The book '{book.title}' with author '{book.author}' borrowed status: '{book.is_borrowed}'")

    def list_all_books(self):
        
        for book in self.list_books:
            print(f" we have this book {book.title} in this library wrtitten by {book.author} borrowed status: {book.is_borrowed}")

    def get_book(self, title):

        for book in self.list_books:
            if book.title == title:
                print(f"the boook {book.title} author {book.author} now the borrowed status is: {book.is_borrowed}")

    def borrow_book(self, title):

        for book in self.list_books:

            if book.title == title:
                book.borrow_book()
                print(f"The book {book.title} was borrowed now has this borrowed status: {book.is_borrowed}")

    def return_book(self, title):

        for book in self.list_books:
            if book.title == title:
                book.return_book()
                print(f"the book {book.title} was returned correctly now the borrow status is:  {book.is_borrowed}")
            

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
    
    
    print(f"{'*'*10} initial status")
    libreria_principal.list_available_books()

    libreria_principal.borrow_book('one hundred of solitude')

    print(f"{'*'*10} after borrow one hundred of solitude")

    libreria_principal.list_available_books()
    print(f"{'*'*10} after return the book")

    libreria_principal.return_book('one hundred of solitude')

    print(f"{'*'*10} status all books")

    libreria_principal.list_all_books()




