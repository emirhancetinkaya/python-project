class Library:
    def __init__(self, file_name='books.txt'):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')

    def __del__(self):
        self.file.close()

    def book_check(self, title):
        try:
            self.file.seek(0)
            books = self.file.read().splitlines()
            books = [book.strip().split(',')[0] for book in books]

            if title in books:
                return "This book is in the library"
            else:
                return "The book was not found in the library"
        except FileNotFoundError:
            return "File not found"       

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        total_books = len(books)
        for book in books:
            title, author, release_date, pages = book.split(',')
            print(f"Title: {title}, Author: {author}")
            
        print("Books in our library management system are listed", "\n")    
        print(f"Total number of books: {total_books}\n")    

    def add_book(self):
        print("you can save book")
        title = input("Please enter book title: ")
        # eger kitap varsa kontrol et
        if self.book_check(title) == 'This book is in the library':
            print(f"Book '{title }' already exist in the library")
            return
        author = input("Please enter book author: ")
        release_date = input("Please enter release year: ")
        pages = input("Please enter number of pages: ")
        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' successfully added to file.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            if title_to_remove not in book:
                self.file.write(book)
        print(f"Book '{title_to_remove}' successfully removed to file.")

    

lib = Library()


while True:

    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit(Q to exıt)")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'Q':
        break
    else:
        print("Invalid choice. Please enter a valid option.")