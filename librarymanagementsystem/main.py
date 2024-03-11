from libraryClass import Library
from bookClass import Book

def display_menu():
    print("\nLibrary Menu:")
    print("1. Add book")
    print("2. List all books")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Search books by title")
    print("6. Search books by author")
    print("7. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    my_library = Library()

    while True:
        user_choice = display_menu()

        if user_choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            my_library.add_book(Book(title, author))

        elif user_choice == "2":
            my_library.list_books()

        elif user_choice == "3":
            title = input("Enter the title of the book to check out: ")
            my_library.check_out_book(title)

        elif user_choice == "4":
            title = input("Enter the title of the book to return: ")
            my_library.return_book(title)

        elif user_choice == "5":
            title = input("Enter the title to search for: ")
            my_library.search_books_by_title(title)

        elif user_choice == "6":
            author = input("Enter the author to search for: ")
            my_library.search_books_by_author(author)

        elif user_choice == "7":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
