"""
    Редактирование текстового файла.

    Отредактировать файл files/text.txt таким образом, чтоб он начинался
    строкой "BEGIN" и заканчивался строкой "END"
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    file_path = BASE_DIR / "files" / "text.txt"
    with open(file_path, "r+") as f:
        # читаем файл
        data = f.read()

        # изменяем данные в переменной
        data = "BEGIN\n" + data
        if data.endswith("\n"):
            data += "END"
        else:
            data += "\nEND"

        # переводим курсор в начала файла и перезаписываем измененные данные
        f.seek(0)
        f.write(data)


if __name__ == "__main__":
    main()
