"""Создайте класс "Магазин", в котором хранятся товары и их
количество. Реализуйте методы: добавить товар, продать
товар, проверить наличие, вывести отчёт по складу.
"""


class Shop:
    def _init_(self, name: str, products: list, quantity):
        self.name = name
        self.products = products
        self.quantity = quantity

    def add_product(self, add_product):
        self.add_product = add_product
        if self.quantity <= 0:
            return "Товар не был добавлен, так как он меньше нуля"
        self.quantity += 1
        self.products.append(add_product)

        return f"вы добавили {self.quantity} штук  в {self.product}"

    def sell(self, sell_product):
        for product in self.products:
            product = sell_product
            return f'Проданный товар: {product}'
        self.quantity -=1
