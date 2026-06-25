class BookAlreadyLoanedException(Exception):

    def __init__(self):
        super().__init__(
            "El libro actual se encuentra prestado"
        )