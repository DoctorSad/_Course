"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
    ...
"""


def main():
    from pathlib import Path
    path = Path(__file__).resolve()
    path = path.parent
    file_path = path / "files" / "phone_book.txt"
    with open(file_path, 'r') as f:
        data = f.readlines()
        f.close()
    out_data = format_data(data)
    print(out_data)

    f = open("files/edited_phone_book.txt", 'a')
    for i in out_data:
        f.write(i)
    f.close()


def format_data(data_in: list) -> list:
    import re
    index = 1
    out_data = []
    for i in data_in:
        tmp = (re.sub(r"\W", '', i))
        tmp_letters = re.findall(r"[a-zA-Z]+", tmp)
        tmp_letters = "".join(tmp_letters)
        tmp_digit = re.findall(r'\d', tmp)
        tmp_digit = "".join(tmp_digit)
        out_data.append(str(index) + '. +380' + str(tmp_digit[len(tmp_digit) - 9:]) + ' - ' + tmp_letters + '\n')
        index += 1
    return out_data


if __name__ == "__main__":
    main()
