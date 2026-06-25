class LoanNotFoundException(Exception):

    def __init__(self):
        super().__init__("Prestamo no encontrado")