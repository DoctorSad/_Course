"""
    Загрузить данные из файла и отобразить.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# строим путь к директории 'files' в этом же каталоге
FILES_DIR = BASE_DIR / "files"
FILES_DIR.mkdir(exist_ok=True)  # создаем директорию, если ее нет


def main():
    students = load_students()

    for student_info in students:
        print(f"{student_info[0]} из города {student_info[3]}.")


def load_students() -> list[list]:
    student_list = []

    file_path = FILES_DIR / "students.txt"  # строим путь к файлу
    if not file_path.exists():
        # если файла нет - возвращаем пустой список
        print("Файл students.txt не обнаружен.")
        return []

    with open(file_path, "r") as f:
        for line in f.readlines():
            student_list.append(line.split())
    return student_list


if __name__ == "__main__":
    main()
