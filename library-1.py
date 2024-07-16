library = []
library_set = {}

def add_book(title, author, genre):
    book = (title, author, genre)
    if book not in library:
        library.append(book)
        print(book)
        print("Book added successfully")
    else:
        b=list[book]
        library_set[title] = b
        print("Book already exists in the library")

def remove_from_library(title):
    if title in library_set:
            book=library_set[title]
            library.remove(book)
            del library_set[title]
            print("Book removed successfully")
            return
    print("Book not found")

def search_book(title):
    if title in library_set:
        print("Book found: ", library_set[title])
    else:
        print("Book not found")

def list_books(library):
    if len(library) == 0:
        print("The library is empty. No books to display.")
    else:
        print(library)

def categorize_books():
    genres = {}
    for book in library:
        if book[2] in genres:
            genres[book[2]].append(book)
        else:
            genres[book[2]] = [book]
    for genre, books in genres.items():
        print("Genre: ", genre)
        for book in books:
            print("Book Name, Author, Genre: ", book)

while True:
    print("1.Add books")
    print("2.Remove a book")
    print("3.Search for book")
    print("4.List all books")
    print("5.Categorize books")
    print("6.Exit")
    d = int(input("Enter number between 1 to 6:"))

    if d == 1:
        n = int(input("Enter the number of books to be added in the library:"))
        for i in range(n):
            title = str(input("Enter the title of the book: "))
            author = str(input("Enter the author of the book: "))
            genre = str(input("Enter the genre of the book: "))
            add_book(title, author, genre)

    elif d == 2:
        title = str(input("Enter the name of the book to be removed:"))
        remove_from_library(title)

    elif d == 3:
        title = str(input("Enter the name of the book to be searched:"))
        search_book(title)

    elif d == 4:
        list_books(library)

    elif d == 5:
        categorize_books()

    elif d == 6:
        exit(0)
    else:
        print("Invalid Choice")