"""
    Необходимо сохранять данные студентов в файл при выходе из программы.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# строим путь к директории 'files' в этом же каталоге
FILES_DIR = BASE_DIR / "files"
FILES_DIR.mkdir(exist_ok=True)  # создаем директорию, если ее нет


def main():
    students = get_students()

    for student_info in students:
        print(f"{student_info[0]} из города {student_info[3]}.")

    save_info(students)


def get_students(n: int = 2) -> list[list]:
    list_ = []

    print("Заполните имя, фамилию, год рождения и город (через пробел)")
    for i in range(n):
        info = input(f"Студент #{i + 1}: ")
        list_.append(info.split())
    return list_


def save_info(list_: list[list]) -> None:
    file_path = FILES_DIR / "students.txt"  # строим путь к файлу
    with open(file_path, "a") as f:
        for info in list_:
            print(" ".join(info), file=f)


if __name__ == "__main__":
    main()
