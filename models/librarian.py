from models.person import Person


class Librarian(Person):

    def show_information(self):
        return (
            f"Blibliotecario: {self.name} "
            f"{self.last_name}"
        )