"""
    Напишите функцию, которая не принимает водных параметров,
    запрашивает у пользователя username, валидирует его и возвращает.

    Валидации:
    - мимимальное количество символов 6 (len)
    - максимальное количество симолов 20 (len)
    - доступны только латинские буквы в нижнем регистре и _ (in, string lib)
    - username не может начинаться символом _ (.startswith())

    Если какое-то из требований не выполняется, запрашиваем повторный ввод.

    * смотрите lesson5/_6_practice_valid.py
"""
from string import ascii_lowercase


def main():
    print("Введите имя пользователя:", end=" ")
    username = get_username()
    print(f"Добро пожаловать, {username}!")


def get_username() -> str:
    username = input()
    errors = []
    if len(username) < 6 or len(username) > 20:
        errors.append("Недопустимая длина (6-20 символов)")

    if username.startswith("_"):
        errors.append('Имя не может начинаться символом "_"')

    for char in username:
        if char not in ascii_lowercase + "_":
            errors.append('Доступны только латинские буквы и "_".')
            break

    if errors:
        print("\n".join(errors))
        return get_username()

    return username


if __name__ == "__main__":
    main()
