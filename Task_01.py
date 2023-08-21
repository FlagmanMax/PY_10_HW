# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:
    def __init__(self, r: float):
        self._r = r

    def get_length(self):
        return 2 * math.pi * self._r

    def get_square(self):
        return math.pi * self._r ** 2


cicrle = Circle(10)
print(f'{round(cicrle.get_length(),2)=}')
print(f'{round(cicrle.get_square(),2)=}')
