"""
    1. Если в строке буква 's' встречается один раз, вывести ее индекс,
    если 2 и более - вывести индекс ее первого и последнего вхождения.
"""

# string = input("1. Введите строку: ")
string = "expressions"

if string.count("s") == 1:
    print(string.index("s"))
elif string.count("s") >= 2:
    print(string.index("s"))
    print(string.rindex("s"))


"""
    2. В строке заменить цифры словами
    0 - zero
    1 - one
    2 - two
    3 - three
    4 - four

    Для теста:
    '2 + 2 = 4'
    '1,2,3,4,5'
    'He11o W0rld'
"""

s = "2 + 2 = 4"

s = (
    s.replace("0", "zero")
    .replace("1", "one")
    .replace("2", "two")
    .replace("3", "three")
    .replace("4", "four")
    .replace("5", "five")
)

"""
    3. Удалить из строки все запятые.
"""

s = "Secure, shy, favour length, all twenty, denote."
s = s.replace(",", "")

"""
    4. Заменить пробелы символом '*'.
    Если встречается подряд несколько пробелов,
    то их следует заменить одним символом '*'.
    Пробелы в начале и конце строки удалить.
"""
