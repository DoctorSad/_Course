"""
    Написать функцию валидирования номера телефона.
    - номер должен содержать 12 цифр
    - начинаться на 380
"""


def main():
    s = input("Enter phone number: ")
    if is_valid_phone(s):
        print("OK")
    else:
        print("Invalid phone number")


def is_valid_phone(s):
    if len(s) != 12:
        return False
    if not s.startswith("380"):
        return False
    # if len(s) != 12 or not s.swartswith("380"):
    return True


if __name__ == "__main__":
    main()
