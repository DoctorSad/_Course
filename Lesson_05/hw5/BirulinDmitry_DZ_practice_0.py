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


def main():
    print("Введите имя пользователя:", end=" ")
    username = get_username()
    print(f"Добро пожаловать, {username}!")


def get_username() -> str:
    while True:
        not_lower_or_underscore = None
        username = input()
        if username.find('_') == -1:
            not_lower_or_underscore = 1
        else:
            for i in username:
                if not i.islower() and i != '_':
                    not_lower_or_underscore = 1
                    break
        if 6 > len(username) or len(username) > 20:
            print('Длина имени меньше 6-ти или больше 20-ти символов')
            continue
        elif not_lower_or_underscore:
            print('username не состоит из латинских букв в нижнем регистре и _')
            continue
        if username[0] == '_':
            print('username не может начинаться с символа "_"')
            continue
        return username




if __name__ == "__main__":
    main()
