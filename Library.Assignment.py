# Creat a library (book and library classes)
# Book contains a numerical id, book name, author name, number of pages, genre and whether the book is on loan.
# At first, a list is made to the Library in the __init__ function, to which at least five books are added.
# Let's add functions for borrowing and returning a book using id. Added functions to list the books, separating those on loan from other books.
  
class Book:
        def __init__(self, ID, BookName, AuthorName, Pages,Genre,availability):
            self.bookID = ID
            self.BookName = BookName
            self.AuthorName = AuthorName
            self.Pages = Pages
            self.Genre = Genre
            self.availability = True  #Initially book is available
        
class MyLibrary:
        def __init__(self):
            self.books = []
        def addBook(self,book):
            self.books.append(book)

def borrowBook(self, bookID):
        for book in self.books:
            if book.bookID == bookID:
                if book.is_available:
                    book.is_available = False
                    print({book.BookName}+ " is not available.")
                else:
                    print({book.BookName}+ +" is available to borrow.")
                return

def returnBook(self, bookID):
        for book in self.books:
            if book.bookID == bookID:
                if not book.is_available:
                    book.is_available = True
                    print(f"You have returned '{book.BookName}' by {book.author}.")
                else:
                    print(f"'{book.BookName}' is already available in the library.")
                return
        print("Book not found in the library.")

def listBooks(self):
        print("Books in the library:")
        for book in self.books:
            availability = "Available" if book.is_available else "Borrowed"
            print(f"ID: {book.bookID}, BookName: {book.BookName}, Author: {book.author}, Genre: {book.genre}, Pages: {book.Pages}, Status: {availability}")

def main():
    library = MyLibrary()

    # Adding some sample books to the library
    book1 = Book(1, "BOOK1", "F.S", 100, "Classics")
    book2 = Book(2, "BOOK2", "H.L", 200, "Fiction")
    book3 = Book(3, "BOOK3", "G.O", 300, "Dystopian")
    book4 = Book(4, "BOOk4 ", "J.R", 400, "Fantasy")
    book5 = Book(5, "BOOK5", "J.A", 500, "Romance")

    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)
    library.addBook(book4)
    library.addBook(book5)

    while True:
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List all books")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            bookID = int(input("Enter the ID of the book you want to borrow: "))
            library.borrowBook(bookID)
        elif choice == "2":
            bookID = int(input("Enter the ID of the book you want to return: "))
            library.returBook(bookID)
        elif choice == "3":
            library.listBooks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
            main()

