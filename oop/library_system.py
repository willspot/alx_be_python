# library_system.py

class Book:
    def __init__(self, title, author):
        """Constructor to initialize book title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return the string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor to initialize the eBook, with file size as an additional attribute."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return the string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor to initialize the print book, with page count as an additional attribute."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return the string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Constructor to initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (or its derived type) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

