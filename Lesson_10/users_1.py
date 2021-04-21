"""
    Создать список из n пользователей через input().
"""


class User:
    def __init__(self, username, email, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        """Метод будет срабатывать при отображении списка объектов,
        а также при форматированном выводе объекта"""
        return f'<User: username="{self.username}">'

    def reset_password(self):
        """Сброс пароля путем генерации нового"""
        # описываем логику сброса/генерации или используем функцию gen_password
        new_password = "some_random_pass"
        # записываем новый пароль в атрибут
        self.password = new_password

    def get_info(self):
        return f"{self.username}:{self.email}"


def main():
    n = input("Сколько пользователей желаете создать? ")
    if not n.isdigit() or int(n) < 1:
        print("Должно быть целое положительное число!")
        return None

    n = int(n)

    users = []
    for i in range(1, n + 1):
        users.append(get_user(i))

    print("Созданные пользователи:", users)


def get_user(i: int) -> User:
    """Получаем данные через input() и инициализируем объект класса User"""
    # для получения данных можно использовать отдельные функции с валидациями
    username = input(f"Введите username пользователя #{i}: ")
    email = input(f"Email для пользователя #{i}: ")
    password = input(f"Пароль для пользователя #{i}: ")

    user = User(username, email, password)
    print(f"\nПользователь {user} добавлен.\n")
    return user


if __name__ == "__main__":
    main()
