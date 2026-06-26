from models.library import Library
from models.book import Book
from services.book_service import BookService
from services.user_service import UserService
from services.loan_service import LoanService
from factories.person_factory import PersonFactory

library = Library()

book_service = BookService(library)
user_service = UserService(library)
loan_service = LoanService(library)



def books_menu():

    while True:

        print("\nLibros")
        print("1- Agregar")
        print("2- Actualizar")
        print("3- Eliminar")
        print("4- Listar")
        print("0- Volver")

        option = input("Option: ")

        if option == "1":

            title = input("Titulo: ")
            author = input("Autor: ")
            isbn = input("ISBN: ")
            year = int(input("Ano de publicacion: "))
            pages = int(input("Paginas: "))

            book = Book(
                title,
                author,
                isbn,
                year,
                pages
            )

            book_service.add_book(book)

        elif option == "2":

            isbn = input("ISBN: ")
            title = input("Titulo: ")
            author = input("Autor: ")
            year = int(input("Ano de publicacion: "))
            pages = int(input("Paginas: "))

            book_service.update_book(
                isbn,
                title,
                author,
                year,
                pages
            )

        elif option == "3":

            isbn = input("ISBN: ")

            try:
                book_service.delete_book(isbn)
            except Exception as e:
                print(e)

        elif option == "4":
            book_service.list_books()

        elif option == "0":
            break

def users_menu():

    while True:

        print("\nUsuarios")
        print("1- Agregar")
        print("2- Actualizar")
        print("3- Eliminar")
        print("4- Listar")
        print("0- Volver")

        option = input("Opciones: ")

        if option == "1":

            name = input("Nombre: ")
            last_name = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")

            user = PersonFactory.create_user(
                name,
                last_name,
                dni,
                email
            )

            user_service.add_user(user)

        elif option == "2":

            dni = input("DNI: ")

            name = input("Nombre: ")
            last_name = input("Apellido: ")
            email = input("Email: ")

            user_service.update_user(
                dni,
                name,
                last_name,
                email
            )

        elif option == "3":

            dni = input("DNI: ")

            try:
                user_service.delete_user(dni)
            except Exception as e:
                print(e)

        elif option == "4":
            user_service.list_users()

        elif option == "0":
            break

def loans_menu():

    while True:

        print("\nPrestamos")
        print("1- Registrar prestamo")
        print("2- Devolver libro")
        print("3- Prestamos activos")
        print("0- Salir")

        option = input("Opciones: ")

        if option == "1":

            isbn = input("ISBN del libro: ")
            dni = input("DNI del usuario: ")

            book = next(
                (
                    book
                    for book in library.books
                    if book.isbn == isbn
                ),
                None
            )

            user = next(
                (
                    user
                    for user in library.users
                    if user.dni == dni
                ),
                None
            )

            if book and user:

                try:
                    loan_service.register_loan(
                        book,
                        user
                    )

                except Exception as e:
                    print(e)

        elif option == "2":

            isbn = input("ISBN: ")

            try:
                loan_service.return_book(isbn)

            except Exception as e:
                print(e)

        elif option == "3":
            loan_service.list_active_loans()

        elif option == "0":
            break

while True:

    print("\n===== LIBRERIA DIGITAL =====")
    print("1- Libros")
    print("2- Usuarios")
    print("3- Prestamos")
    print("0- Salir")

    option = input("Opciones: ")

    if option == "1":
        books_menu()

    elif option == "2":
        users_menu()

    elif option == "3":
        loans_menu()

    elif option == "0":
        break