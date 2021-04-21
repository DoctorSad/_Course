num1 = 3.141592653589793
num2 = 10 / 3
num3 = 15

print(num1, num2, num3)

# Отображение округленных значений
print(round(num1, 2), round(num2, 2), round(num3, 2))
print(" ".join(str(round(i, 2)) for i in [num1, num2, num3]))
print(" ".join(map(lambda x: str(round(x, 2)), [num1, num2, num3])))

# Отображение значений с фиксированным количеством знаков после запятой
print(f"{num1:.02f} {num2:.02f} {num3:.02f}")

print("{:.02f} {:.02f} {:.02f}".format(num1, num2, num3))

print(
    "{var1:.02f} {var2:.02f} {var3:.02f}".format(
        var1=num1, var2=num2, var3=num3
    )
)
