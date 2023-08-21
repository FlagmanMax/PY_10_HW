# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle():
    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def get_square(self):
        return self.a * self.b

    def get_length(self):
        return 2 * (self.a + self.b)


rectangle1 = Rectangle(3)
print(f'{round(rectangle1.get_square(),2)=}')
print(f'{round(rectangle1.get_length(),2)=}')
