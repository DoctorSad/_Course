"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "здесь_исходная_строка".
        Результат: "здесь_измененная_строка_после_выполненного_пункта".
    (Использовать форматирование строк f'{}')
"""

# можно заменить данную строку на input()
string = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."

# 1.
counter_l = counter_u = 0
for char in string:
    if char.islower():
        counter_l += 1
    elif char.isupper():
        counter_u += 1

if counter_l > counter_u:
    result = string.lower()
elif counter_l < counter_u:
    result = string.upper()
else:
    result = string.swapcase()

print(f'1. Исходная строка: "{string}".\nРезультат: "{result}".\n')


# 2.
if string.istitle():
    result = "done. " + string
else:
    result = "draft: " + string[5:]

print(f'2. Исходная строка: "{string}".\nРезультат: "{result}".\n')


# 3.
if len(string) > 20:
    result = string[:20]
else:
    result = string.ljust(20, "@")
    # or
    # result = string + "@" * (20 - len(string))

print(f'3. Исходная строка: "{string}".\nРезультат: "{result}".\n')
