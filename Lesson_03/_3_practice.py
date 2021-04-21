"""
    Найти факториал числа n.

    !0 = 1
    !1 = 1

    !4 = 1 * 2 * 3 * 4 = 24

    !4 = 4 * 3 * 2 * 1 = 24
"""

number = int(input("Enter n: "))
result = 1

tmp = number
while tmp > 1:
    result *= tmp
    tmp -= 1

print("!", number, " = ", result, sep="")
