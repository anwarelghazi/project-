from lib.author import Author
from lib.book import Book

def print_authors():
    authors = Author.get_all()
    print("Authors:")
    for author in authors:
        print(f"ID: {author[0]}, Name: {author[1]}")

def add_author(name):
    author = Author(name)
    author.save()
    print("Author added successfully.")

def delete_author(author_id):
    Author.delete(author_id)
    print("Author deleted successfully.")

def print_books():
    books = Book.get_all()
    print("Books:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Price: {book[2]}, Author ID: {book[3]}")

def add_book(title, price, author_id):
    book = Book(title, price, author_id)
    book.save()
    print("Book added successfully.")

def delete_book(book_id):
    Book.delete(book_id)
    print("Book deleted successfully.")

def main():
    while True:
        print("WELCOME TO BOOK COLLECTION MANAGER")
        print("What would you like to do?")
        print("1. Add Author")
        print("2. Add Book")
        print("3. View Authors")
        print("4. View Books")
        print("5. Delete Author")
        print("6. Delete Book")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Add Author")
            name = input("Enter author's name: ")
            add_author(name)
        elif choice == 2:
            print("Add Book")
            title = input("Enter book's title: ")
            price = float(input("Enter book's price: "))
            author_id = int(input("Enter author's ID: "))
            add_book(title, price, author_id)
        elif choice == 3:
            print_authors()
        elif choice == 4:
            print_books()
        elif choice == 5:
            print("Delete Author")
            author_id = int(input("Enter author's ID to delete: "))
            delete_author(author_id)
        elif choice == 6:
            print("Delete Book")
            book_id = int(input("Enter book's ID to delete: "))
            delete_book(book_id)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
