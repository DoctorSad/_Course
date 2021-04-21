"""
    Решение без разбиения логики по отдельным функциям.

"""


def main():
    while True:
        s = input("Введите номер телефона: ")
        digits = "".join(i for i in s if i.isdigit())
        phone_number = "380" + digits[-9:]
        if len(phone_number) != 12:
            print("Недостаточно цифр в номере.")
            continue
        else:
            break

    while True:
        email = input("Введите email: ")
        if len(email) < 6:
            print("Минимальная длина 6 символов.")
            continue
        if email.count("@") != 1:
            print("Неверный формат email.")
            continue
        domain = email.split("@")[1]
        if len(domain.split(".")) < 2:
            print("Неверный формат email.")
            continue
        break

    while True:
        password = input("Введите пароль: ")
        if len(password) < 8:
            print("Слишком короткий пароль (минимум 8 символов).")
            continue
        digits = lowers = uppers = specials = 0
        for char in password:
            if char.isspace():
                print("Пароль не должен содержать пробельных символов.")
                break
            elif char.isdigit():
                digits = 1
            elif char.islower():
                lowers = 1
            elif char.isupper():
                uppers = 1
            else:
                specials = 1
        else:
            if digits + lowers + uppers + specials != 4:
                print(
                    "Ненадежный пароль. Используйте буквы в верхнем и "
                    "нижнем регистре, цифры и спец-символы."
                )
                continue
            else:
                confirmed = input("Повторите пароль: ")
                if password != confirmed:
                    print("Пароли не совпадают.")
                    continue
                else:
                    break

    print(
        "\nПоздравляем с успешной регистрацией!\n"
        f"Ваш номер телефона: +{phone_number}\n"
        f"Ваш email: {email}\n"
        f'Ваш пароль: {"*" * len(password)}'
    )


if __name__ == "__main__":
    main()
