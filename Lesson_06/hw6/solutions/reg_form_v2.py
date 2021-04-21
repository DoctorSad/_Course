"""
    Модифицируйте форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""
import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    phone_number = get_phone_number()
    email = get_email()
    password = get_password()

    print_info(phone_number, email, password)
    save_info(phone_number, email, password)


def get_phone_number():
    """Получение номера телефона"""
    s = input("Введите номер телефона: ")
    phone_number = format_phone(s)
    if not is_valid_phone(phone_number):
        return get_phone_number()
    return phone_number


def format_phone(s):
    """Форматирование номера телефона"""
    digits = "".join(i for i in s if i.isdigit())
    phone = "380" + digits[-9:]
    return phone


def is_valid_phone(phone):
    """Валидация номера телефона"""
    if len(phone) != 12:
        log_error("phone", "Недостаточно цифр в номере.", phone)
        return False
    return True


def get_email():
    """Получение email"""
    email = input("Введите email: ")
    if not is_valid_email(email):
        return get_email()
    return email


def is_valid_email(email):
    """Валидация email"""
    if len(email) < 6:
        log_error(
            "email", "Минимальная длина 6 символов.", email, use_print=False
        )
        return False
    if email.count("@") != 1:
        print("Неверный формат email.")
        return False
    domain = email.split("@")[1]
    if len(domain.split(".")) < 2:
        print("Неверный формат email.")
        return False
    # if not re.search(r"^[\w]+[\w.-]*@[\w.-]+\.[a-zA-Z]{2,}$", email):
    #     return False
    return True


def get_password():
    """Получение пароля и его подтверждения"""
    password = input("Введите пароль: ")

    if not is_valid_password(password):
        return get_password()

    confirmed = input("Подтвердите пароль: ")
    if password != confirmed:
        print("Пароли не совпадают.")
        return get_password()
    else:
        return password


def is_valid_password(password):
    """Функция валидации пароля"""
    if len(password) < 8:
        print("Слишком короткий пароль (минимум 8 символов).")
        return False

    digits = lowers = uppers = specials = 0
    for char in password:
        if char.isspace():
            print("Пароль не должен содержать пробельных символов.")
            return False
        elif char.isdigit():
            digits = 1
        elif char.islower():
            lowers = 1
        elif char.isupper():
            uppers = 1
        else:
            specials = 1

    if digits + lowers + uppers + specials != 4:
        print(
            "Ненадежный пароль. Используйте буквы в верхнем и "
            "нижнем регистре, цифры и спец-символы."
        )
        return False

    return True


def print_info(phone_number, email, password):
    print(
        "\nПоздравляем с успешной регистрацией!\n"
        f"Ваш номер телефона: +{phone_number}\n"
        f"Ваш email: {email}\n"
        f'Ваш пароль: {"*" * len(password)}'
    )


def save_info(phone_number, email, password):
    """Сохранение данных в файл"""
    file_path = BASE_DIR / "users.txt"
    with open(file_path, "a") as f:
        print(f"{phone_number} {email} {password}", file=f)


def log_error(field, message, value, use_print=True):
    """Логирование ошибок. Отображение и сохранение в файл"""
    if use_print:
        print(message)

    file_path = BASE_DIR / "errors.txt"
    with open(file_path, "a") as f:
        print(f'{field}: "{message}"; value: {value}', file=f)


if __name__ == "__main__":
    main()
