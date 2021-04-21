"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл passwords.txt
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    3*. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""
import random

from pathlib import Path
from string import ascii_lowercase, ascii_letters, digits, punctuation

BASE_DIR = Path(__file__).resolve().parent
passwords_path = BASE_DIR / "passwords.txt"


def main():
    choice = input(
        "1. Сгенерировать простой пароль\n"
        "2. Сгенерировать средний пароль\n"
        "3. Сгенерировать сложный пароль\n"
    )
    if choice == "1":
        password = gen_password(ascii_lowercase)
    elif choice == "2":
        password = gen_password(ascii_letters + digits)
    elif choice == "3":
        password = gen_strong_pw()

    if password:
        print(password)
        save(password)


def save(password):
    """Сохранение password в файл"""
    with open(passwords_path, "a") as f:
        print(password, file=f)


def gen_password(chars, length=8):
    """Базовая функция для генерации пароля"""
    password = ""
    for _ in range(length):
        password += random.choice(chars)

    if not is_available_pw(password):
        try:
            return gen_password(chars, length)
        except RecursionError:
            print("Уникальные пароли закончились.")
            return None
    return password


def is_available_pw(password):
    """Функция проверяет есть ли password в файле с паролями"""
    if not passwords_path.exists():
        return True

    with open(passwords_path, "r") as f:
        # for line in f.readlines():
        #     if password == line.strip():
        #         return False

        if password in f.read():
            return False
    return True


def gen_strong_pw():
    """Функция для генерации сложного пароля"""
    length = random.randint(8, 16)
    password = gen_password(ascii_letters + digits + punctuation, length)

    if not is_strong_pw(password):
        return gen_strong_pw()
    return password


def is_strong_pw(password):
    """Функция для валидации сложного пароля"""
    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        elif not char.isspace():
            counter_s += 1

    if counter_d and counter_u and counter_l and counter_s:
        return True
    return False


if __name__ == "__main__":
    main()
