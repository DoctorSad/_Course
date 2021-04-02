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


def main():
    from pathlib import Path
    path = Path(__file__).resolve()
    path = path.parent
    file_path = path / "files" / "passwords.txt"

    print('Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра', end='')
    print(' и 1 спец-символ, длина от 8 до 16 символов)')
    while True:
        import string
        import random
        print('Выберите длину пароля (от 8 до 16 символов): ', end='')
        password_lenght = input()
        try:
            password_lenght = int(password_lenght)
        except ValueError:
            print('Вы не ввели диапазоны с типом <int>')
        else:
            if password_lenght < 8 or password_lenght > 16:
                print('Выбранная длина меньше 8 и больше 16 символов')
                continue
            else:
                while True:
                    insecure_password = None
                    with open(file_path, 'r') as f:
                        data = f.readlines()
                    password = ''
                    for _ in range(password_lenght):
                        password += random.choice(string.ascii_lowercase + string.ascii_uppercase
                                                  + string.digits + string.punctuation)
                    if true_password(password):
                        for i in data:
                            if password == i[:len(i) - 1]:
                                print('Insecure password')
                                insecure_password = 1
                        if insecure_password == 1:
                            continue
                        else:
                            with open(file_path, 'a') as f:
                                print(password, file=f)
                        break
                    else:
                        continue
                print(f'\nСгенерированный пароль: {password}')
            if exit_program():
                continue
            else:
                break


def true_password(password: str) -> int:
    import string
    space_present = 0
    upper_present = 0
    lower_present = 0
    digit_present = 0
    spec_present = 0
    for i in password:
        if i.isspace():
            space_present = 1
            break
    for i in password:
        if i.isupper():
            upper_present = 1
            break
    for i in password:
        if i.lower():
            lower_present = 1
            break
    for i in password:
        if i.isdigit():
            digit_present = 1
            break
    for i in password:
        q = string.punctuation.count(i)
        if string.punctuation.count(i):
            spec_present = 1
            break
    if space_present:
        return 0  # Присутствуют пробельные символы
    elif upper_present == 0 or lower_present == 0 or digit_present == 0 or spec_present == 0:
        return 0  # если нет lower или upper или digit
    else:
        return 1


def exit_program() -> int:
    out = input('                                    Вернуться в меню (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        return 1  # Продолжаем программу
    else:
        return 0  # Заканчиваем программу


if __name__ == "__main__":
    main()
