"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
"""

# можно заменить данную строку на input()
string = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."

for _ in range(20):
    print('\n')
print('     *** Longest word ***     ')

my_string = input('Введите строку: ')
lower = 0
upper = 0
out = ''
for i in my_string:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
if lower > upper:
    print(my_string.lower())
elif upper > lower:
    print(my_string.upper())
elif upper == lower:
    for i in my_string:
        if i.islower():
            i = i.upper()
            out = out + i
            continue
        elif i.isupper():
            i = i.lower()
            out = out + i
            continue
        out = out + i
print(out)

