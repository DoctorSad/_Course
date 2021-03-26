"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.
    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

year = input('Введите год: ')
if not year.isdigit():
    exit('Год не был введен в виде числа')
year = int(year)

if not year % 400:
    print('Введенный год', year, 'является високосным')
elif not year % 100:
    print('Введенный год', year, 'не является високосным')
elif not year % 4:
    print('Введенный год', year, 'является високосным')
else:
    print('Введенный год', year, 'не является високосным')
