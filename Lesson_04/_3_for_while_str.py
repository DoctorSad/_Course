"""
    Строки можно обойти циклом.

    1. Перебрать все элементы строки циклом for.
    2. Пройти по индексам элементов строки циклом for либо while.
"""

s = "Hello world!"

for i in s:
    print(i)


for i in range(len(s)):
    print(s[i])


i = 0
while i < len(s):
    print(s[i], end=", ")
    i += 1
