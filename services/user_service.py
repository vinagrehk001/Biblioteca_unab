from typing import Self

from decorators.logger_decorator import log_operation
from exceptions.user_not_found_exception import UserNotFoundException


class UserService:

    def __init__(self, library):
        self.library = library

    @log_operation
    def add_user(self, user):
        self.library.users.append(user)

    @log_operation
    def list_users():

        if len(Self.library.users) == 0:
            print("No se encontraron usuarios registrados")
            return

        for user in Self.library.users:
            print(
                user.show_information()
            )

    @log_operation
    def delete_user(self, dni):

        for user in self.library.users:

            if user.dni == dni:
                self.library.users.remove(user)
                return

        raise UserNotFoundException()

    @log_operation
    def update_user(
            self,
            dni,
            name,
            last_name,
            email
    ):

        for user in self.library.users:

            if user.dni == dni:
                user.name = name
                user.last_name = last_name
                user.email = email
                return

        raise UserNotFoundException()
