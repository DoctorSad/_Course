"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501


def main():
    while True:
        import string
        import random
        password = ''
        password_lenght = 0
        print('       1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)')
        print('       2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)')
        print('       3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра', end='')
        print(' и 1 спец-символ, длина от 8 до 16 символов)')
        print('       4. Пользовтельский пароль')
        print('            (1, 2, 3, 4 - выбор пункта меню, q - Выход): ', end='')
        menu_ = menu(input())

        if menu_ == 1:
            for _ in range(8):
                password += random.choice(string.ascii_lowercase)
            print(f'\nСгенерированный пароль: {password}')
            if exit_program():
                continue
            else:
                break
        elif menu_ == 2:
            for _ in range(8):
                password += random.choice(string.ascii_lowercase + string.ascii_uppercase)
            print(f'\nСгенерированный пароль: {password}')
            if exit_program():
                continue
            else:
                break
        elif menu_ == 3:
            while True:
                print('Выберите длину пароля (от 8 до 16 символов): ', end='')
                password_lenght = input()
                try:
                    password_lenght = int(password_lenght)
                except ValueError:
                    print('Вы не ввели диапазоны с типом <int>')
                else:
                    if password_lenght < 8 or password_lenght > 16:
                        print('Выбранная длина меньше 8 и больше 16 символов')
                        continue
                    else:
                        while True:
                            password = ''
                            for _ in range(password_lenght):
                                password += random.choice(string.ascii_lowercase + string.ascii_uppercase
                                                          + string.digits + string.punctuation)
                            if true_password(password):
                                break
                            else:
                                continue
                        print(f'\nСгенерированный пароль: {password}')
                break
            if exit_program():
                continue
            else:
                break
        elif menu_ == 4:
            ascii_lowercase = None
            ascii_uppercase = None
            digits = None
            punctuation = None
            temp_string = ''
            out_password = ''
            len_of_password = None
            print('Длина пароля: ')
            len_of_password = int(input())
            print('Из чего будет делаться выбор: ')
            print('abcdefghijklmnopqrstuvwxyz', '(Y/n?): ', end='')
            ascii_lowercase = yes_or_no(input())
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '(Y/n?): ', end='')
            ascii_uppercase = yes_or_no(input())
            print('0123456789', '(Y/n?): ', end='')
            digits = yes_or_no(input())
            print('!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~', '(Y/n?): ', end='')
            punctuation = yes_or_no(input())

            if ascii_lowercase:
                temp_string += string.ascii_lowercase
            if ascii_uppercase:
                temp_string += string.ascii_uppercase
            if digits:
                temp_string += string.digits
            if punctuation:
                temp_string += string.punctuation

            for _ in range(len_of_password):
                out_password += random.choice(temp_string)

            print(f'\nСгенерированный пароль: {out_password}')
            if exit_program():
                continue
            else:
                break

        elif menu_ == -1:
            break


def menu(answer: str) -> int:
    if answer == '1':
        return 1  # Выбор первого пункта меню
    elif answer == '2':
        return 2  # Выбор второго пункта меню
    elif answer == '3':
        return 3  # Выбор 3-го пункта меню
    elif answer == '4':
        return 4  # Выбор 4-го пункта меню
    else:
        return -1  # Выход из программы


def true_password(password: str) -> int:
    import string
    space_present = 0
    upper_present = 0
    lower_present = 0
    digit_present = 0
    spec_present = 0
    for i in password:
        if i.isspace():
            space_present = 1
            break
    for i in password:
        if i.isupper():
            upper_present = 1
            break
    for i in password:
        if i.lower():
            lower_present = 1
            break
    for i in password:
        if i.isdigit():
            digit_present = 1
            break
    for i in password:
        q = string.punctuation.count(i)
        if string.punctuation.count(i):
            spec_present = 1
            break
    if space_present:
        return 0  # Присутствуют пробельные символы
    elif upper_present == 0 or lower_present == 0 or digit_present == 0 or spec_present == 0:
        return 0  # если нет lower или upper или digit
    else:
        return 1


def yes_or_no(answer: str) -> int:
    if answer == 'Y' or answer == '':
        return 1  # Ответ "Да"
    else:
        return 0  # Ответ "Нет"


def exit_program() -> int:
    out = input('                                    Вернуться в меню (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        return 1  # Продолжаем программу
    else:
        return 0  # Заканчиваем программу

if __name__ == "__main__":
    main()
