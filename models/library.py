from metaclasses.singleton_meta import SingletonMeta


class Library(metaclass=SingletonMeta):

    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []