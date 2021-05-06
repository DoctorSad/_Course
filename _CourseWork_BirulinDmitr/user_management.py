from pathlib import Path
import json
from menu_functions import get_main_menu, get_second_menu, get_third_menu
from user_function import sort_users, delete_user, detailed_user, reset_password, new_user
from handling_functions import import_file


def main():
    BASE_DIR = Path(__file__).resolve().parent
    FILES_DIR = BASE_DIR / "Files"
    FILES_DIR.mkdir(exist_ok=True)
    file_user_data = FILES_DIR / "users.json"
    file_errors = FILES_DIR / "errors.txt"

    user_data_in = {}
    with open(file_user_data) as f:
        user_data_in = json.load(f)
    database_of_users = list(user_data_in)

    while True:
        choice_main_menu = get_main_menu()
        if choice_main_menu == 1:  # Зарегистрировать нового пользователя
            database_of_users.append(new_user(file_errors, database_of_users))
        elif choice_main_menu == 2:  # Просмотреть список пользователей
            choice_second_menu = get_second_menu()
            if choice_second_menu == 1:  # Просмотреть количество зарегистрированных пользователей
                print(f'\nКоличество зарегистрированных пользователей: {len(database_of_users)}')
                input()
            elif choice_second_menu == 2:  # Вывести подробную информацию о пользователе
                sorted_database = sort_users(database_of_users)
                user_from_db = detailed_user(sorted_database)
                choice_third_menu = get_third_menu()
                if choice_third_menu == 1:  # Сбросить пароль
                    reset_password(user_from_db)
                elif choice_third_menu == 2:  # Удалить пользователя
                    delete_user(user_from_db, database_of_users)
        elif choice_main_menu == 3:  # Импорт пользователей из файла
            database_of_users = import_file(database_of_users)
        elif choice_main_menu == 4:  # Выход
            with open(file_user_data, "w") as f:
                data = json.dumps(database_of_users, indent=4)
                f.write(data)
            break


if __name__ == "__main__":
    main()
