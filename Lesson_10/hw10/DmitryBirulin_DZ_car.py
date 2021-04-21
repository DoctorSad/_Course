"""
    1. Реализуйте класс Car с атрибутами:
    - brand (марка)
    - model (модель)
    - engine (объем двигателя)
    - year (год выпуска)
    2. Создайте метод get_info, который возвращает инфо "Ford Focus v2.3"
    3. Создайте список из 5 объектов класса Car.
    4. Отсортируйте список объектов по year
    5. Выведите на экран результат метода get_info для каждого объекта списка
"""


class Car:
    def __init__(self, brand: str, model: str, engine: float, year: int, *args, **kwargs):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year

    def get_info(self):
        list_ = [
            self.brand.title(),
            self.model.title(),
            'v' + str(self.engine)
        ]
        return " ".join(list_)

    def dict_car(self):
        return {'brand': self.brand, 'model': self.model, 'engine': self.engine, 'year': self.year}

    def __repr__(self):
        return self.get_info()

# 3. Создайте список из 5 объектов класса Car.
list_of_car = []
list_of_car.append(Car('mitsubishi', 'colt', 1.3, 2008))
list_of_car.append(Car('mitsubishi', 'Galant', 2.0, 2000))
list_of_car.append(Car('Audi', 'TT', 2.4, 2005))
list_of_car.append(Car('Opel', 'astra', 1.5, 1998))
list_of_car.append(Car('Toyota', 'corolla', 1.4, 2003))

# 4. Отсортируйте список объектов по year
print(sorted(list_of_car, key=lambda x: x.year))

# 5. Выведите на экран результат метода get_info для каждого объекта списка
print('\n')
for i in list_of_car:
    print(i.get_info() + ': ', i.dict_car())
