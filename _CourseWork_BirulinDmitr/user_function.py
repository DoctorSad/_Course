import random
import string
from handling_functions import true_password
from handling_functions import phone_number
from handling_functions import is_unique_phone
from handling_functions import true_email


def sort_users(database_of_users: list) -> list:
    sorted_database = list(database_of_users)
    sorted_database.sort(key=lambda x: x['phone'])
    count = 1
    for i in sorted_database:
        if len(str(count)) < 2:
            str_count = str(count).rjust(2, '0')
        else:
            str_count = str(count)
        print(f'{str_count}. {i["phone"]}')
        count += 1
    return sorted_database


def delete_user(user_from_db: dict, database_of_users: list):
    print('Действительно удалить пользователя (Y/n)?: ', end='')
    confirm = input()
    if not confirm or confirm == 'Y':
        for i in database_of_users:
            if i['phone'] == user_from_db['phone']:
                database_of_users.remove(i)
        print('Пользователь будет удален при выходе из программы в главном меню')
        input()
    else:
        print('Пользователь не будет удален при выходе из программы в главном меню '
              '(Действие не подтверждено)')
        input()


def detailed_user(sorted_database: list) -> dict:
    while True:
        print('Введите номер пользователя для вывода детальной информации: ', end='')
        tmp = input()
        try:
            selected_user = int(tmp)
        except ValueError:
            continue
        if len(sorted_database) < selected_user or selected_user < 1:
            continue
        break

    count = 1
    for i in sorted_database:
        if selected_user == count:
            user_from_db = i
            break
        count += 1
    print('             Данные пользователя:')
    print(f'        Номер телефона: +{user_from_db["phone"]}')
    print(f'        Email: {user_from_db["email"]}')
    out_password = '*' * len(user_from_db["password"])
    print(f'        Пароль: {out_password}')
    return user_from_db


def reset_password(user_from_db: dict):
    while True:
        new_password = ''
        for _ in range(10):
            new_password += random.choice(string.ascii_lowercase + string.ascii_uppercase
                                          + string.digits + string.punctuation)
        if user_from_db['password'] == new_password:
            continue
        right_password = true_password(new_password)
        if right_password:
            user_from_db['password'] = new_password
            print(f'У пользователя с номером {user_from_db["phone"]} изменен пароль')
            input()
            break


def new_user(file_errors: str, database_of_users: list) -> dict:

    # 1. Пользователь вводит номер телефона.
    while True:
        str_number = input('Введите номер телефона: ')
        number_out = phone_number(str_number)
        if not is_unique_phone(number_out, database_of_users):
            print('Введенный номер существует в базе пользователей. Введите уникальный номер')
            continue
        if number_out:
            break
        else:
            print('Неправильный номер')
            with open(file_errors, 'a') as f:
                print(f"Невалидный номер телефона: {str_number}", file=f)
            continue

    # 2. Пользователь вводит email.
    while True:
        email = input('\nВведите email: ')
        email_out = true_email(email)
        if email_out:
            break
        else:
            print('email неправильный!')
            with open(file_errors, 'a') as f:
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
                break
            else:
                print('Подтверждение не соответствует паролю!')
                with open(file_errors, 'a') as f:
                    print(f"Невалидное подтверждение пароля: {confirmation}", file=f)
                continue
        else:
            print('Пароль слабый')
            with open(file_errors, 'a') as f:
                print(f"Невалидный пароль: {password}", file=f)

    password_for_output = '*' * len(password)
    print('\n        Поздравляем с успешной регистрацией!')
    print(f'        Ваш номер телефона: +{number_out}')
    print(f'        Ваш email: {email}')
    print(f'        Ваш пароль: {password_for_output}')
    input()

    new_user_add = {"phone": number_out,
                    "email": email,
                    "password": password
                    }
    return new_user_add
