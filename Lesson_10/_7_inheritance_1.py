"""
    Реулизуем класс, наследуясь от int
    дополнить его методом проверки простоты числа

    вместо CustomInt класс можно назвать int,
    но таким образом мы переопределим стандартный класс
"""


class CustomInt(int):
    def is_prime(self):
        if self < 2:
            return False
        elif self == 2:
            return True
        else:
            for i in range(2, self):
                if self % i == 0:
                    return False
            return True


a = CustomInt(17)
b = CustomInt(10)

print(a + b)  # 27

print(a.is_prime())  # True
print(b.is_prime())  # False
