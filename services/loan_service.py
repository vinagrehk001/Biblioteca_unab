from decorators.logger_decorator import log_operation
from models.loan import Loan
from exceptions.loan_not_found_exception import LoanNotFoundException
from exceptions.book_already_loaned_exception import BookAlreadyLoanedException


class LoanService:

    def __init__(self, library):
        self.library = library

    @log_operation
    def register_loan(self, book, user):

        for loan in self.library.loans:

            if loan.book.isbn == book.isbn and loan.is_active():
                raise BookAlreadyLoanedException()

        loan = Loan(book, user)

        self.library.loans.append(loan)

    @log_operation
    def return_book(self, isbn):

        for loan in self.library.loans:

            if loan.book.isbn == isbn and loan.is_active():
                loan.return_book()
                return

        raise LoanNotFoundException()

    @log_operation
    def list_active_loans(self):

        active_loans = [
            loan
            for loan in self.library.loans
            if loan.is_active()
        ]

        if len(active_loans) == 0:
            print("No hay prestamos activos")
            return

        for loan in active_loans:
            print(loan)