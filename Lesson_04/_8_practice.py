"""
    1. Вводим строку.

    Если длина строки больше 5, вывести первые три символа в верхнем регистре и
    последние три символа в нижнем регистре.

    Иначе вывести первый символ с измененным регистром столько раз,
    какова длина строки.
"""

# s = input('1. Enter some string: ')
s = "Hello woRlD"

if len(s) > 5:
    print(s[:3].upper(), s[-3:].lower())
else:
    print(s[0].swapcase() * len(s))


"""
    2. Определить, является ли строка палиндромом.
    aba == aba
    anna == anna
    python != nohtyp
"""

s = "anna"
# Сравниваем строку с перевернутой строкой
if s == s[::-1]:
    print("+")
else:
    print("-")


"""
    3. Удалить из строки повторяющиеся символы и пробелы.
"""

# s = input('3. Enter some string: ')
s = "Hello woR lD"
new_s = ""

for char in s:
    # если такого символа еще нет в новой строке и он не является пробелом
    if char not in new_s and char != " ":
        new_s += char

print(new_s)


"""
    4. Посчитать количество цифр, строчных и заглавных букв в строке.
"""

# s = input('4. Enter some string: ')
s = "pyth$on DjangO 123 %@#2020 Basic!"

# создаем переменные-счетчики для хранения количества символов
counter_d = counter_l = counter_u = 0

for char in s:
    # когда встречается нужный символ инкрементируем счетчик
    if char.isdigit():
        counter_d += 1
    elif char.islower():
        counter_l += 1
    elif char.isupper():
        counter_u += 1

print(counter_d, counter_l, counter_u)

"""
    5. Убрать из строки знаки препинания.
"""

# s = input('5. Enter some string: ')
s = "Hello World!  Lorem, Ipsum - is; simply, dummy!"

# Проходим циклов по тем знакам, которые нужно убрать и делаем replace()
for i in "!-;,.":
    s = s.replace(i, "")
