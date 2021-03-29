"""
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
"""

string = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."
out = ''

my_string = input('Введите строку: ')
if len(my_string) > 20:
    out = my_string[:20]
else:
    out = my_string + '@' * (20 - len(my_string))
print(out)
