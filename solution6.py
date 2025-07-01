"""str_a ="90"
b = 23
c = int(str_a) + b
print(c)
"""
""" #Преобразование string во float 
str_f = "44.6"
n = 13.5
l = float(str_f) + n
print(l)
"""
"""Задача 6
Напишите код, который переводит целое число в строку, при том что его
можно применить в любой системе счисления. """

def func(a=0, b=0):
    if type(a) == int:
        str_a = str(a)
        str_b = str(b)

    return str_a + str_b

print(func(5, 5))
