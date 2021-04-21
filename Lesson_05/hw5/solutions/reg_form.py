"""
    Решение hw5/reg_form.py

"""


def main():
    phone_number = get_phone_number()
    email = get_email()
    password = get_password()

    print_info(phone_number, email, password)


def get_phone_number():
    """Получение, форматирование и валидация номера телефона"""
    s = input("Введите номер телефона: ")
    digits = "".join(i for i in s if i.isdigit())
    phone_number = "380" + digits[-9:]
    if len(phone_number) != 12:
        print("Недостаточно цифр в номере.")
        return get_phone_number()
    return phone_number


def get_email():
    """Получение и валидация email"""
    email = input("Введите email: ")
    if len(email) < 6:
        print("Минимальная длина 6 символов.")
        return get_email()
    if email.count("@") != 1:
        print("Неверный формат email.")
        return get_email()
    domain = email.split("@")[1]
    if len(domain.split(".")) < 2:
        print("Неверный формат email.")
        return get_email()
    return email


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


if __name__ == "__main__":
    main()
