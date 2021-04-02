"""
    Модифицируйте форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""


def main():

    from pathlib import Path
    path = Path(__file__).resolve()
    path = path.parent
    file_path = path / "files" / "errors.txt"

    while True:

        # 1. Пользователь вводит номер телефона.
        while True:
            str_number = input('Введите номер телефона: ')
            number_out = phone_number(str_number)
            if number_out:
                # print(f'Результат: {number_out}')
                break
            else:
                print('Неправильный номер')
                with open(file_path, 'a') as f:
                    print(f"Невалидный номер телефона: {str_number}", file=f)
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
                with open(file_path, 'a') as f:
                    print(f"Невалидный email: {email}", file=f)

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
                    with open(file_path, 'a') as f:
                        print(f"Невалидное подтверждение пароля: {confirmation}", file=f)
                    continue
            else:
                print('Пароль слабый')
                with open(file_path, 'a') as f:
                    print(f"Невалидный пароль: {password}", file=f)
        password_for_output = '*' * len(password)
        print('\n        Поздравляем с успешной регистрацией!')
        print(f'        Ваш номер телефона: +{number_out}')
        print(f'        Ваш email: {email}')
        print(f'        Ваш пароль: {password_for_output}')

        file_path = path / "files" / "users.txt"
        with open(file_path, 'a') as f:
            print(f"phone: {str_number}", file=f)
            print(f"email: {email}", file=f)
            print(f"password: {password}", file=f)
            print(f"_____________________________________________", file=f)

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
