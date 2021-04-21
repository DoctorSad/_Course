"""
    Создайте структуру с именем student, содержащую поля:
    фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов).

    Создать массив из десяти элементов такого типа,
    упорядочить записи по возрастанию среднего балла.

    Добавить возможность вывода фамилий и номеров групп студентов,
    имеющих оценки, равные только 4 или 5
"""


class Student:
    def __init__(self, surname: str, group: int, scores: list):
        """При инициализации обрабатываем аргументы и создает атрибуты"""
        self.surname = surname
        self.group = group
        self.scores = scores

    def __str__(self):
        return self.surname

    def __repr__(self):
        return f'<Student: surname="{self.surname}"'

    @property
    def avg_score(self):
        """Свойство возвращает средний балл студента"""
        return sum(self.scores) / len(self.scores)

    def is_excellent(self):
        """Метод для проверки успешности студента (оценки 4+)"""
        for score in self.scores:
            if score < 4:
                return False
        return True

    def show_info(self):
        """Отображает фамилию и группу студента, если у него высокие оценки"""
        if self.is_excellent():
            print(f"{self.surname}, {self.group}")


if __name__ == "__main__":
    # создаем список из объектов класса Student
    students = [
        Student("Jane A.", 15, [4, 5, 4, 5, 4]),
        Student("Max S.", 15, [3, 4, 3, 5, 4]),
        Student("John S.", 13, [2, 2, 2, 5, 4]),
    ]
    print(students)

    # сортируем по среднему баллу
    students.sort(key=lambda x: x.avg_score)

    # выводим фамилию и номер группы студентов с оценками 4 и 5
    for student in students:
        student.show_info()
