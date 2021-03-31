"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""


def main():

    while True:

        # 1. Пользователь вводит номер телефона.
        while True:
            str_number = input('Введите номер телефона: ')
            number_out = phone_number(str_number)
            if number_out:
                # print(f'Результат: {number_out}')
                break
            else:
                print('Недостаточно цифр в номере')
                continue

        # 2. Пользователь вводит email.
        while True:
            email = input('\nВведите email: ')
            email_out = true_email(email)
            if email_out:
                # print(f'email правильный: {email}')
                break
            else:
                print('email неправильный!')

        # 3. Пользователь ввод пароль.
        while True:
            confirmation = None
            password = input('\nВведите пароль: ')
            out_password = true_password(password)
            if out_password:
                print('Введите подтверждение пароля: ')
                confirmation = input()
                if confirmation == password:
                    # print('Пароль успешно введен!')
                    break
                else:
                    print('Подтверждение не соответствует паролю!')
                    continue
            else:
                print('Пароль слабый')
        password_for_output = '*' * len(password)
        print('\n        Поздравляем с успешной регистрацией!')
        print(f'        Ваш номер телефона: +{number_out}')
        print(f'        Ваш email: {email}')
        print(f'        Ваш пароль: {password_for_output}')

        # Обработка выхода из программы
        if exit_program():
            continue
        else:
            break


def phone_number(str_number: str) -> int:
    numbers = []
    for i in str_number:
        if i.isdigit():
            numbers.append(i)
    number = ''.join(numbers)
    if len(number) < 10:
        return 0  # Недостаточно цифр в номере
    elif len(number) >= 10:
        return int('38' + number[len(number) - 10:])  # Возврат номера в формате 380981234567


def true_email(email: str) -> int:
    if len(email) <= 6:
        return 0  # длина меньше шести символов
    elif email.find('@') == -1:
        return 0  # Нет символа "@". Введенная строка не может быть электронным адресом'
    elif email.rfind('.') < email.find('@') or not email.count('.'):
        return 0  # Некорректный формат адреса
    else:
        return 1  # Формат адреса корректный


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
    if len(password) < 8:
        return 0  # длина пароля меньше восьми символов
    elif space_present:
        return 0  # Присутствуют пробельные символы
    elif upper_present == 0 or lower_present == 0 or digit_present == 0 or spec_present == 0:
        return 0  # если нет lower или upper или digit
    else:
        return 1


def exit_program() -> int:
    out = input('                                    Заполнить еще одну форму регистрации (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        return 1  # Продолжаем программу
    else:
        return 0  # Заканчиваем программу


if __name__ == "__main__":
    main()
