"""
    Для импортирования сторонних модулей, библиотек используется:
    import module

    Для импортирования конкретной функции/константы из модуля:
    from module import some_function

    Импортируемому объкту можно задать псевдоним,
    под которым он будет исползоваться в коде
    from module import some_function as func

    Чтобы импортировать все объекты из модуля (не рекомендуется):
    from module import *

"""

import random
import string

from random import randint as rint, choice
from string import ascii_letters as letters

print(random.randint(1, 10))  # случайное число из диапазона от 1 до 10
print(random.choice("hello world"))  # случайный элемент из последовательности
print(random.sample("hello world", 2))  # случайная выборка 2 элементов

print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_letters)  # ascii_lowercase + ascii_uppercase
print(string.punctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.digits)  # '0123456789'

# при импорте конкретной переменной (функции) обращаемся к ней прямо
print(rint(1, 10))
print(choice("hello world"))

print(letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
