import re
import json
import os


def true_password(password: str) -> int:
    if len(password) >= 8 and not re.findall(r"\s", password) and re.findall(r"[a-zа-я]", password) \
        and re.findall(r"[A-ZА-Я]", password) and re.findall(r"[0-9]", password) \
            and re.findall(r"[!#$%&()*+,-.:;<=>?@^_{|}~]", password):
        return 1
    return 0


def true_email(email: str) -> int:
    if len(email) > 6 and re.findall(r"\S+[@]\S+[.]\S+", email):
        return 1
    return 0


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


def is_unique_phone(str_number: int, database_of_users: list):
    for i in database_of_users:
        if i['phone'] == str_number:
            return False
    return True


def import_file():
    print('Введите полный путь к файлу в формате "C:/Users/admin/Desktop/example.json": ', end='')
    while True:
        new_files = input()
        check_file = os.path.exists(new_files)
        if check_file:
            file_user_data = new_files
            with open(file_user_data) as f:
                user_data_in = json.load(f)
            database_of_users = list(user_data_in)
            return [database_of_users, file_user_data]
        else:
            print('Неправильно введен путь к файлу с его именем. Повторите ввод: ', end='')
