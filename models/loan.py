from datetime import datetime


class Loan:

    def __init__(self, book, user):
        self.book = book
        self.user = user
        self.loan_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()

    def is_active(self):
        return self.return_date is None

    def __str__(self):
        return (
            f"Libro: {self.book.title} "
            f"- Usuario: {self.user.name}"
        )