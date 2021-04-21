"""
    Применение argparser на примере генератора паролей
"""
import argparse
import random

from string import ascii_lowercase, ascii_letters, digits, punctuation


def gen_password(chars, length=8):
    """Базовая функция для генерации пароля"""
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


def gen_simple_pw():
    """Функция для генерации простого пароля"""
    return gen_password(ascii_lowercase)


def gen_medium_pw():
    """Функция для генерации пароля средней сложности"""
    return gen_password(ascii_letters + digits)


def gen_strong_pw():
    """Функция для генерации сложного пароля"""
    length = random.randint(8, 16)
    password = gen_password(ascii_letters + digits + punctuation, length)

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
        return password
    return gen_strong_pw()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="password gen")
    parser.add_argument("-c", "--complexity", default="simple")

    args = parser.parse_args()

    complexity = args.complexity

    if complexity in ["m", "medium"]:
        print(gen_medium_pw())
    elif complexity in ["s", "strong"]:
        print(gen_strong_pw())
    else:
        print(gen_simple_pw())
