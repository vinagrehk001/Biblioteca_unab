class BookNotFoundException(Exception):

    def __init__(self):
        super().__init__("Libro no encontrado")