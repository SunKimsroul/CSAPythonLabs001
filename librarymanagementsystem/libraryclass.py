from bookClass import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
            return
        for book in self.books:
            status = "Available" if not book.is_checked_out else "Checked Out"
            print(f"{book.title} by {book.author} - {status}")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                print(book.check_out())
                return
        print(f"{title} is not available for checkout.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                print(book.return_book())
                return
        print(f"{title} was not checked out.")

    def search_books_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books found with that title.")

    def search_books_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books found by that author.")
