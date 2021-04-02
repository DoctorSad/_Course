"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

from pathlib import Path
path = Path(__file__).resolve()
path = path.parent
file_path = path / "files" / "file_practice.txt"
print(file_path)
with open(file_path, 'w') as f:
    f.write("Starting practice with files\n")

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

f = open("files/file_practice.txt", "r")
data = f.read()
print(data[:5])
f.close()

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

f = open("files/file_practice.txt", "r+")
data = f.read()

letter_i = data.count('i')
letter_e = data.count('e')
if letter_i > letter_e:
    data = data.replace('i', 'e')
else:
    data = data.replace('e', 'i')
f.write(data)
f.close()

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""


f = open("files/file_practice.txt", "a+")
data = f.read()
b = len(data)
if not len(data) % 2:
    f.write('the end')
else:
    f.write('bye')
f.seek(0)
data = f.read()
f.close()

print(data)

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

f = open("files/file_practice.txt", 'r')
data = f.read()
f.close()

half = round(len(data) / 2)
data = data[:half] + ' *some inserted text* ' + data[half:]

f = open("files/file_practice.txt", 'w')
f.write(data)
f.close()
