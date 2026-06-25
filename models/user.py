from models.person import Person


class User(Person):

    def show_information(self):
        return (
            f"Usuario: {self.name} "
            f"{self.last_name} "
            f"DNI: {self.dni}"
        )