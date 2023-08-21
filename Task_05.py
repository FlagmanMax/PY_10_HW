# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.



class Fish:
    def __init__(self, name, age, scales):
        self.name = name
        self.age = age
        self.scales = scales

    def swim(self):
        print(' I am swimming')

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(' I am barking')

class Bird:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def fly(self):
        print(' I am flying')

