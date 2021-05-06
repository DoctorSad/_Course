import re
import json
import os


def true_password(password: str) -> int:
    if len(password) >= 8 and not re.findall(r"\s", password) and re.findall(r"[a-zа-я]", password) \
        and re.findall(r"[A-ZА-Я]", password) and re.findall(r"[0-9]", password) \
            and re.findall(r"[!#$%&()*+,-.:;<=>?@^_{|}~]", password):
        return 1
    return 0


def get_password(file_errors: str) -> str:
    confirmation = None
    password = input('\nВведите пароль: ')
    out_password = true_password(password)
    if out_password:
        print('Введите подтверждение пароля: ', end='')
        confirmation = input()
        if confirmation == password:
            return password
        else:
            print('Подтверждение не соответствует паролю!')
            with open(file_errors, 'a') as f:
                print(f"Невалидное подтверждение пароля: {confirmation}", file=f)
            return get_password(file_errors)
    else:
        print('Пароль слабый')
        with open(file_errors, 'a') as f:
            print(f"Невалидный пароль: {password}", file=f)
        return get_password(file_errors)


def get_email(file_errors: str) -> str:
    email = input('\nВведите email: ')
    email_out = true_email(email)
    if email_out:
        return email
    else:
        print('email неправильный!')
        with open(file_errors, 'a') as f:
            print(f"Невалидный email: {email}", file=f)
        return get_email(file_errors)


def true_email(email: str) -> int:
    if len(email) > 6 and re.findall(r"\S+[@]\S+[.]\S+", email):
        return 1
    return 0


def check_phone_number(str_number: str) -> int:
    numbers = []
    for i in str_number:
        if i.isdigit():
            numbers.append(i)
    number = ''.join(numbers)
    if len(number) < 10:
        return 0  # Недостаточно цифр в номере
    elif len(number) >= 10:
        return int('38' + number[len(number) - 10:])  # Возврат номера в формате 380981234567


def get_phone_number(file_errors: str, database_of_users: list) -> int:
    str_number = input('Введите номер телефона: ')
    number_out = check_phone_number(str_number)
    if not is_unique_phone(number_out, database_of_users):
        print('Введенный номер существует в базе пользователей. Введите уникальный номер')
        return get_phone_number(file_errors, database_of_users)
    if number_out:
        return number_out
    else:
        print('Неправильный номер')
        with open(file_errors, 'a') as f:
            print(f"Невалидный номер телефона: {str_number}", file=f)
        return get_phone_number(file_errors, database_of_users)


def is_unique_phone(str_number: int, database_of_users: list):
    for i in database_of_users:
        if i['phone'] == str_number:
            return False
    return True


def import_file(database_of_users: list):
    print('Введите полный путь к файлу в формате "C:/Users/admin/Desktop/example.json": ', end='')
    merged_database = list(database_of_users)
    while True:
        new_file = input()
        check_file = os.path.exists(new_file)
        if check_file:
            # file_user_data = new_file
            with open(new_file) as f:
                user_data_in = json.load(f)
            imported_database_of_users = list(user_data_in)
            for i in imported_database_of_users:
                flag = 0
                for q in database_of_users:
                    if i['phone'] == q['phone']:
                        flag = 1
                if not flag:
                    merged_database.append(i)
            return merged_database
        else:
            print('Неправильно введен путь к файлу с его именем. Повторите ввод: ', end='')
