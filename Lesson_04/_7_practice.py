"""
    Посчитать, сколько английских букв в введенной строке.
"""
import string


s = input('Введите строку: ')

count = 0
for i in s:
    if i in string.ascii_letters:
        count += 1

print(count)

"""
    Определить 3 найболее часто встречаемых символов в строке
"""


"""
    Удалить повторяющиеся пробелы в строке.
"""