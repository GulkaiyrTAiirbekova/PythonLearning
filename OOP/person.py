
"""
Задача 1
Создайте класс "Человек" с атрибутами имя и возраст.
Добавьте метод, который возвращает строку с приветствием.
"""
class Person:
    def __init__(self, first_name: str,  last_name : str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.first_name} {self.last_name}, мне {self.age} лет."

person = Person(
    "Tom",
    "Jackson",
    12,
)
result = person.greet()
print(result)




