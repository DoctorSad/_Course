"""
    Найти суму цифр двузначного целого числа, вводимого в клавиатуры.
    пр: 14 => 1 + 4 = 5
"""

a = int(input('Введите двузначное число: '))
res = a // 10 + a % 10
print(res)