"""
    1. Определить структуру User с полями username, email и password,
    при этом password - необязательное поле

    2. Добавить возможность сбросить пароль объекту User
"""


class User:
    def __init__(self, username, email, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        """Метод будет срабатывать при отображении списка объектов"""
        return f'<User: username="{self.username}">'

    def reset_password(self):
        """Сброс пароля путем генерации нового"""
        # описываем логику сброса/генерации или используем функцию gen_password
        new_password = "some_random_pass"
        # записываем новый пароль в атрибут
        self.password = new_password

    def get_info(self):
        return f"{self.username}:{self.email}"


if __name__ == "__main__":
    users = [
        User("max", "max@mail.com", "#Fw@#Rwefw"),
        User("jane", "jane@mybox.com", "qwerty0"),
        User("john", "john@inbox.com"),
    ]
    print(users)

    # сбросим пароль третьему пользователю
    users[2].reset_password()

    for user in users:
        print(user.get_info(), user.password)
