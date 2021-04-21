"""
    Посчитать, сколько английских букв в введенной строке.
"""
import string


s = input("Введите строку: ")

count = 0
for i in s:
    if i in string.ascii_letters:
        count += 1

print(count)


"""
    Удалить повторяющиеся пробелы в строке.
"""

text = "Hello World  !  today is    a sunny  day :)"

# 1 Способ - с помощью split и join
splited_text = text.split()  # после split() по умолчанию получаем список строк
result = " ".join(splited_text)  # объединяем их в одну через 1 пробел
print(result)

# 2 способ - с помощью цикла
result = text.replace("  ", " ")
while "  " in result:
    result = result.replace("  ", " ")
print(result)
