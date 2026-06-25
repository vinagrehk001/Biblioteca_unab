class Book:

    def __init__(
            self,
            title,
            author,
            isbn,
            publication_year,
            pages
    ):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.pages = pages

    def __str__(self):
        return (
            f"{self.title} - "
            f"{self.author} - "
            f"ISBN: {self.isbn}"
        )