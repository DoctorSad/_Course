"""
    Ввести с помощью input() 3 числа.
    Вывести их с помощью print() в обратном порядке.
    Пример работы программы:
    Ввод:
    1
    125
    13
    Вывод:
    13
    125
    1
"""
number = []
number.append(int(input('Введите число №1: ')))
number.append(int(input('Введите число №2: ')))
number.append(int(input('Введите число №3: ')))

print('Введенные числа в обратном порядке выглядят следующим образом:\n', number[2], ', ', number[1], ', ', number[0], sep='')