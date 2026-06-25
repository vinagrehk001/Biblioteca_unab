from models.user import User
from models.librarian import Librarian


class PersonFactory:

    @staticmethod
    def create_user(
            name,
            last_name,
            dni,
            email
    ):

        return User(
            name,
            last_name,
            dni,
            email
        )

    @staticmethod
    def create_librarian(
            name,
            last_name,
            dni,
            email
    ):

        return Librarian(
            name,
            last_name,
            dni,
            email
        )