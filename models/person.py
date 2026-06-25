from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, last_name, dni, email):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email

    @abstractmethod
    def show_information(self):
        pass