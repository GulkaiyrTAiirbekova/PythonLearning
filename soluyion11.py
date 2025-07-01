#"get the last and first el"
# def func(list):
#     return list[0],[-1]
#
# print(func(list))
#Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#  Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = [i for i in a if i <= 5]
# print(result)

#Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вывести числа общие для обейх списков
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = [i for i in a if i in b]
# print(c)

#Задача 3
# Отсортируйте словарь
# по значению в порядке возрастания и убывания

# age = {'Tom': 15, 'Sam': 2, 'Ali': 8, 'Sasha': 19}
# def  sorted_dict(age):
#     result = []
#     for key,value in age.items():
#         result.append(value)
#     return sorted(result )
# print(sorted_dict(age))

"""Задача 3
Отсортируйте словарь
по значению в порядке возрастания и убывания.

fruits = {
    "яблоко": 50,
    "апельсин": 20,
    "банан": 30,
    "груша": 10
}


fruits_list = list(fruits.items())

def get_price(fruit):
    return fruit[1]
sorted_list_p = sorted(fruits_list, key=get_price)
sorted_list_n = sorted(fruits_list, key=get_price, reverse=True)

sorted_fruits1 = dict(sorted_list_p)
sorted_fruits2 = dict(sorted_list_n)
print(sorted_fruits1)
print(sorted_fruits2)"""

