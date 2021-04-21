"""
    Применим функции из 5 урока к решению задачи.

    В итоге, глядя на главную функцию main даже без комментариев понятна суть:
    получение номера телефона и вывод его на экран.

    А логика получения номера телефона вынесена в отдельные функции.
"""


def main():
    phone = get_phone()
    print(phone)


def get_phone() -> str:
    s = input("Введите номер телефона: ")

    phone = phone_format(s)

    if is_valid_phone(phone):
        return phone
    else:
        print("Вы ввели недостаточно цифр. Повторите ввод.")
        return get_phone()


def phone_format(s: str) -> str:
    """Отбирает из строки только цифры и приводит номер к нужному формату"""
    phone = ""
    for i in s:
        if i.isdigit():
            phone += i
    return "380" + phone[-9:]


def is_valid_phone(s: str) -> bool:
    if len(s) != 12 or not s.startswith("380"):
        return False
    return True


if __name__ == "__main__":
    main()
