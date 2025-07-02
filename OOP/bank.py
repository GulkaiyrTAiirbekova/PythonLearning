"""
Задача 5
Создайте класс "Банк", где каждый пользователь имеет
уникальный счёт. Реализуйте систему пополнения, снятия,
проверки баланса и ограничений на минимальный остаток.
"""
class Bank:
    def __init__(self, name: str):  # двойное подчеркивание
        self.bank_name = name

    def greet(self):
        return f"Добро пожаловать в наш {self.bank_name} банк"


class Client(Bank):
    def __init__(self, bank_name: str, client_first_name: str, amount: float, id: int):
        super().__init__(bank_name)
        self.client_first_name = client_first_name
        self._amount = amount
        self.id = id

    @property
    def clean_amount(self):
        return self._amount

    @clean_amount.setter
    def clean_amount(self, new_amount: float):
        if new_amount < 0:
            raise ValueError('Баланс не должен быть отрицательным')
        self._amount = new_amount

    def greet(self):
        base_greet = super().greet()
        return f"{self.client_first_name}, {base_greet} — на вашем счету (ID: {self.id}) доступно {self._amount}."


# Пример использования
client = Client('Mbank', 'Ivan', 101, 1)
client.clean_amount = 1  # установка нового баланса
print(client.clean_amount)  # вывод баланса
print(client.greet())  # приветствие
