"""
    Пример использования модулей random и string

    Программа выводит случайный спец-символ либо число.

    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

import random
import string

# # генерируем строку для выборки
# tmp = digits + punctuation
#
# # выбираем случайный символ из строки
# char = choice(tmp)
#
# print(char)


def main():
    ascii_lowercase = None
    ascii_uppercase = None
    digits = None
    punctuation = None
    menu_ = None
    out_string = ''
    temp_string = ''
    print('Из чего будет делаться выбор: ')
    print('abcdefghijklmnopqrstuvwxyz', '(Y/n?): ', end='')
    ascii_lowercase = yes_or_no(input())
    print('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '(Y/n?): ', end='')
    ascii_uppercase = yes_or_no(input())
    print('0123456789', '(Y/n?): ', end='')
    digits = yes_or_no(input())
    print('!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~', '(Y/n?): ', end='')
    punctuation = yes_or_no(input())
    print('       1. Вывод одного случайного символа из выбранных последовательностей')
    print('       2. Вывод случайного символа из выбранных последовательностей в одну строку')
    print('       (1, 2 - выбор пункта меню, "Enter" - следующий символ, q - выход)): ', end='')

    if ascii_lowercase:
        temp_string += string.ascii_lowercase
    if ascii_uppercase:
        temp_string += string.ascii_uppercase
    if digits:
        temp_string += string.digits
    if punctuation:
        temp_string += string.punctuation

    menu_ = menu(input())
    if menu_ == 1:
        while True:
            print(random_simvol(temp_string), end='')
            what_next = input()
            if what_next == '':
                continue
            elif what_next == 'q':
                break
            else:
                break
    elif menu_ == 2:
        while True:
            out_string += random_simvol(temp_string)
            print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{out_string}', end='')
            what_next = input()
            if what_next == '':
                continue
            elif what_next == 'q':
                break
            else:
                break
    elif menu_ == 3 or menu_ == -1:
        exit()


def yes_or_no(answer: str) -> int:
    if answer == 'Y' or answer == '':
        return 1  # Ответ "Да"
    else:
        return 0  # Ответ "Нет"


def menu(answer: str) -> int:
    if answer == '1':
        return 1  # Выбор первого пункта меню
    elif answer == '2':
        return 2  # Выбор второго пункта меню
    elif answer == 'q':
        return 3  # выход из программы
    else:
        return -1  # Не определено


def random_simvol(my_string: str) -> str:
    return random.choice(my_string)


if __name__ == "__main__":
    main()
