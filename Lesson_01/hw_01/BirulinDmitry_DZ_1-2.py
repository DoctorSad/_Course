"""
    Программа принимает на ввод 4 числа.
    Необходимо сложить первые два и отдельно вторые два.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""

num_1 = int(input('Введите число №1: '))
num_2 = int(input('Введите число №2: '))
num_3 = int(input('Введите число №3: '))
num_4 = int(input('Введите число №4: '))
print('\nРезультат деления суммы первых двух чисел на сумму вторых двух чисел составляет:')
print((num_1 + num_2) / (num_3 + num_4))
