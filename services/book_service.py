from decorators.logger_decorator import log_operation
from exceptions.book_not_found_exception import BookNotFoundException


class BookService:

    def __init__(self, library):
        self.library = library

    @log_operation
    def add_book(self, book):
        self.library.books.append(book)

    @log_operation
    def list_books(self):

        if len(self.library.books) == 0:
            print("No se encontraron libros")
            return

        for book in self.library.books:
            print(book)

    @log_operation
    def delete_book(self, isbn):

        for book in self.library.books:

            if book.isbn == isbn:
                self.library.books.remove(book)
                return

        raise BookNotFoundException()

    @log_operation
    def update_book(
            self,
            isbn,
            title,
            author,
            publication_year,
            pages
    ):

        for book in self.library.books:

            if book.isbn == isbn:
                book.title = title
                book.author = author
                book.publication_year = publication_year
                book.pages = pages
                return

        raise BookNotFoundException()