""" Создайте классы "Автор" и "Книга".
У каждой книги должен
быть автор. У книги также должны быть методы: "описание
книги" и "проверка принадлежности автору"."""

class Author:
    def __init__(self, first_name: str,  last_name : str):
        self.first_name = first_name
        self.last_name = last_name




class Book(Author):
    def __init__(self, first_name: str,  last_name : str,book: str):
        super().__init__(first_name, last_name)
        self.book= book
        def greet(self):
        return f"Автором  {self.book}  является {self.first_name} {self.last_name}."



book1 = Book(
    "lev",
    "Tolstoy",
    "Oblachnyi Go"
)
result = book1