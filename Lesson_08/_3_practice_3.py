"""
    1. Напишите функцию, которая генерирует 1kk простых паролей.
    2. Узнайте, сколько паролей из сгенерированных уникальны.
    3. Отобразите 5 самых популярных паролей.
"""
import random
import string

from collections import Counter


def main():
    # 1. Генерируем список 1kk паролей
    passwords = gen_passwords(10 ** 6)

    # 2. Создаем счетчик и получаем количество уникальных паролей
    counter = Counter(passwords)
    print(len(counter))

    # 3. Получаем 5 самых популярных паролей
    most_common = counter.most_common(5)
    print(most_common)
    for pw in most_common:
        print(pw[0])


def gen_passwords(n):
    passwords = []
    for _ in range(10 ** 6):
        password = gen(string.ascii_lowercase)
        passwords.append(password)
    return passwords


def gen(chars, length=8):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


if __name__ == "__main__":
    main()
