<<<<<<< HEAD
"""
    Необходимо реализовать программу, которая принимает текст и удаляет из него
    все, что находится в скобочках "(", ")". Скобки могут быть вложенными.
    И выводит получившийся текст.
    ___________________________________________________________________________

    Например:

    >>> Программа принимает текст(вводится с клавиатуры(с помощью input())),
    форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран.

    Результат:
    Программа принимает текст, форматирует его и выводит на экран.
"""
import re

# Вариант 1: стандартный подход
#
# while True:
#     for _ in range(20):
#         print('\n')
#     print('Введите строку:')
#     string = input('')
#     l_skobka = 0
#     r_skobka = 0
#     temp_string = string
#     error = 0
#     index = 0
#     start_index = 0
#     end_index = 0
#     left_open = 0
#
#     if (string.count('(') + string.count(')')) % 2 != 0:
#             error = 1
#     for i in string:
#         if i == '(':
#             l_skobka += 1
#         elif i == ')':
#             r_skobka += 1
#         if r_skobka > l_skobka:
#             error = 1
#             break
#
#     if error:
#         print('Наплужено с количеством и порядком скобок')
#         input()
#     else:
#         count_skobok = string.count('(')
#         while count_skobok != 0:
#             for i in temp_string:
#                 if i == '(':
#                     start_index = index
#                     left_open = 1
#                 if i == ')':
#                     if left_open:
#                         end_index = index
#                         temp_string = temp_string[0:start_index] + temp_string[end_index + 1:]
#                         left_open = 0
#                         break
#                 index += 1
#             start_index = 0
#             index = 0
#             end_index = 0
#             left_open = 0
#             count_skobok -= 1
#         for _ in range(20):
#             print('\n')
#         print('Введенная строка: ')
#         print(f'"{string}"')
#         print('       Результат обработки:')
#         print(f'       "{temp_string}"')
#         out = input('                                    Будем вводить новую строку (Y/n)?: ')
#         if not out or out == 'Y':
#             for _ in range(20):
#                 print('\n')
#             string = ''
#             continue
#         elif out == 'n':
#             break

# Вариант №2: Регулярные выражения

print('Введите строку:')
string = input('')
while re.findall(r'[()]', string):
    del_ = re.findall(r"[(][^()]*[)]", string)
    if len(del_):
        for i in del_:
            string = string.replace(i, "")
    else:
        break
print(string)
=======
<<<<<<< HEAD
"""
    Необходимо реализовать программу, которая принимает текст и удаляет из него
    все, что находится в скобочках "(", ")". Скобки могут быть вложенными.
    И выводит получившийся текст.
    ___________________________________________________________________________

    Например:

    >>> Программа принимает текст(вводится с клавиатуры(с помощью input())),
    форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран.

    Результат:
    Программа принимает текст, форматирует его и выводит на экран.
"""
import re

# Вариант 1: стандартный подход
#
# while True:
#     for _ in range(20):
#         print('\n')
#     print('Введите строку:')
#     string = input('')
#     l_skobka = 0
#     r_skobka = 0
#     temp_string = string
#     error = 0
#     index = 0
#     start_index = 0
#     end_index = 0
#     left_open = 0
#
#     if (string.count('(') + string.count(')')) % 2 != 0:
#             error = 1
#     for i in string:
#         if i == '(':
#             l_skobka += 1
#         elif i == ')':
#             r_skobka += 1
#         if r_skobka > l_skobka:
#             error = 1
#             break
#
#     if error:
#         print('Наплужено с количеством и порядком скобок')
#         input()
#     else:
#         count_skobok = string.count('(')
#         while count_skobok != 0:
#             for i in temp_string:
#                 if i == '(':
#                     start_index = index
#                     left_open = 1
#                 if i == ')':
#                     if left_open:
#                         end_index = index
#                         temp_string = temp_string[0:start_index] + temp_string[end_index + 1:]
#                         left_open = 0
#                         break
#                 index += 1
#             start_index = 0
#             index = 0
#             end_index = 0
#             left_open = 0
#             count_skobok -= 1
#         for _ in range(20):
#             print('\n')
#         print('Введенная строка: ')
#         print(f'"{string}"')
#         print('       Результат обработки:')
#         print(f'       "{temp_string}"')
#         out = input('                                    Будем вводить новую строку (Y/n)?: ')
#         if not out or out == 'Y':
#             for _ in range(20):
#                 print('\n')
#             string = ''
#             continue
#         elif out == 'n':
#             break

# Вариант №2: Регулярные выражения

print('Введите строку:')
string = input('')
while re.findall(r'[()]', string):
    del_ = re.findall(r"[(][^()]*[)]", string)
    if len(del_):
        for i in del_:
            string = string.replace(i, "")
    else:
        break
print(string)
=======
"""
    Необходимо реализовать программу, которая принимает текст и удаляет из него
    все, что находится в скобочках "(", ")". Скобки могут быть вложенными.
    И выводит получившийся текст.
    ___________________________________________________________________________

    Например:

    >>> Программа принимает текст(вводится с клавиатуры(с помощью input())),
    форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран.

    Результат:
    Программа принимает текст, форматирует его и выводит на экран.
"""
import re

# Вариант 1: стандартный подход
#
# while True:
#     for _ in range(20):
#         print('\n')
#     print('Введите строку:')
#     string = input('')
#     l_skobka = 0
#     r_skobka = 0
#     temp_string = string
#     error = 0
#     index = 0
#     start_index = 0
#     end_index = 0
#     left_open = 0
#
#     if (string.count('(') + string.count(')')) % 2 != 0:
#             error = 1
#     for i in string:
#         if i == '(':
#             l_skobka += 1
#         elif i == ')':
#             r_skobka += 1
#         if r_skobka > l_skobka:
#             error = 1
#             break
#
#     if error:
#         print('Наплужено с количеством и порядком скобок')
#         input()
#     else:
#         count_skobok = string.count('(')
#         while count_skobok != 0:
#             for i in temp_string:
#                 if i == '(':
#                     start_index = index
#                     left_open = 1
#                 if i == ')':
#                     if left_open:
#                         end_index = index
#                         temp_string = temp_string[0:start_index] + temp_string[end_index + 1:]
#                         left_open = 0
#                         break
#                 index += 1
#             start_index = 0
#             index = 0
#             end_index = 0
#             left_open = 0
#             count_skobok -= 1
#         for _ in range(20):
#             print('\n')
#         print('Введенная строка: ')
#         print(f'"{string}"')
#         print('       Результат обработки:')
#         print(f'       "{temp_string}"')
#         out = input('                                    Будем вводить новую строку (Y/n)?: ')
#         if not out or out == 'Y':
#             for _ in range(20):
#                 print('\n')
#             string = ''
#             continue
#         elif out == 'n':
#             break

# Вариант №2: Регулярные выражения

print('Введите строку:')
string = input('')
while re.findall(r'[()]', string):
    del_ = re.findall(r"[(][^()]*[)]", string)
    if len(del_):
        for i in del_:
            string = string.replace(i, "")
    else:
        break
print(string)
>>>>>>> 278ff2c11360ab7b20877b63a9b5e1864c106edf
>>>>>>> a6ac6e7990d8f393f6719320e7f406413280a759
