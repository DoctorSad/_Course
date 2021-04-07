"""
    Модифицируем программу.

    Помимо имени, с клавиатуры вводится фамилия, год рождения и город.
    Необходимо сохранить введенный данные.
    Вывести на экран имя и город каждого студента.
"""


def main():
    students = get_students()

    for student_info in students:
        print(f"{student_info[0]} из города {student_info[3]}.")


def get_students(n: int = 2) -> list:
    list_ = []

    print("Заполните имя, фамилию, год рождения и город (через пробел)")
    for i in range(n):
        info = input(f"Студент #{i + 1}: ")
        list_.append(info.split())
    return list_


if __name__ == "__main__":
    main()
