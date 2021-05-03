

def main_menu() -> int:
    print('\n' * 15)
    print('1. Зарегистрировать нового пользователя')
    print('2. Просмотреть список пользователей')
    print('3. Импорт пользователей из файла')
    print('4. Выход\n')
    while True:
        print('Выберите пункт меню (от 1 до 4): ', end='')
        tmp = input()
        try:
            choice = int(tmp)
        except ValueError:
            continue
        if 4 < choice or choice < 1:
            continue
        print('\n' * 15)
        return choice


def second_menu() -> int:
    print('\n' * 15)
    print('1. Просмотреть количество зарегистрированных пользователей')
    print('2. Вывести подробную информацию о пользователе\n')
    while True:
        print('Выберите пункт меню (1 или 2): ', end='')
        tmp = input()
        try:
            choice = int(tmp)
        except ValueError:
            continue
        if 2 < choice or choice < 1:
            continue
        return choice


def third_menu() -> int:
    print('\n1. Сбросить пароль')
    print('2. Удалить пользователя')
    print('3. Выйти в главное меню\n')
    while True:
        print('1, 2 или 3?: ', end='')
        tmp = input()
        try:
            choice = int(tmp)
        except ValueError:
            continue
        if 3 < choice or choice < 1:
            continue
        return choice
