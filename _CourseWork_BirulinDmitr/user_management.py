
from pathlib import Path
import json
from menu_functions import main_menu
from menu_functions import second_menu
from menu_functions import third_menu
from user_function import sort_users
from user_function import delete_user
from user_function import detailed_user
from user_function import reset_password
from user_function import new_user
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
        user_choice = main_menu()
        if user_choice == 1:
            database_of_users.append(new_user(file_errors, database_of_users))
        elif user_choice == 2:
            choice_second_menu = second_menu()
            if choice_second_menu == 1:
                print(f'\nКоличество зарегистрированных пользователей: {len(database_of_users)}')
                input()
            elif choice_second_menu == 2:
                sorted_database = sort_users(database_of_users)
                user_from_db = detailed_user(sorted_database)
                third_choice_menu = third_menu()
                if third_choice_menu == 1:
                    reset_password(user_from_db)
                elif third_choice_menu == 2:
                    delete_user(user_from_db, database_of_users)
        elif user_choice == 3:
            tmp = import_file()
            database_of_users = tmp[0]
            file_user_data = tmp[1]
        elif user_choice == 4:
            with open(file_user_data, "w") as f:
                data = json.dumps(database_of_users, indent=4)
                f.write(data)
            break


if __name__ == "__main__":
    main()
