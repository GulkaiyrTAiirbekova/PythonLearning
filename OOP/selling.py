"""Создайте класс "Магазин", в котором хранятся товары и их
количество. Реализуйте методы: добавить товар, продать
товар, проверить наличие, вывести отчёт по складу.
"""


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.products = {}  # словарь: товар -> количество

    def add_product(self, product_name: str, quantity: int):
        if quantity <= 0:
            return "Нельзя добавить товар с отрицательным количеством."
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
        return f"Добавлено {quantity} шт. товара '{product_name}' в магазин '{self.name}'."

    def sell_product(self, product_name: str, quantity: int):
        if product_name not in self.products:
            return "Такого товара нет в магазине."
        if self.products[product_name] < quantity:
            return "Недостаточно товара на складе."
        self.products[product_name] -= quantity
        if self.products[product_name] == 0:
            del self.products[product_name]
        return f"Продано {quantity} шт. товара '{product_name}'."

    def check_product(self, product_name: str):
        return self.products.get(product_name, 0)

    def report(self):
        if not self.products:
            return "Склад пуст."
        return "\n".join(f"{name}: {qty} шт." for name, qty in self.products.items())

shop = Shop("Центральный рынок")
print(shop.add_product("Яблоки", 10))
print(shop.add_product("Бананы", 5))
print(shop.sell_product("Яблоки", 3))
print(shop.check_product("Яблоки"))
print(shop.report())
