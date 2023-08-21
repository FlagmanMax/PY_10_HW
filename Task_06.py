# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.



class Animal:
    def __init__(self, name, age, voice = 'groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def say(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print(' I am swimming')

    def get_info(self):
        print(f"Type: Fish, name = {self.name}, age = {self.age}, scales={self.scales}")

class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print(' I am barking')

class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    def fly(self):
        print(' I am flying')

if __name__ == "__main__":
    fish = Fish('Nemo', 2, 'silver', 'bul-bul')
    dog = Dog('Spark', 5, 'pitbull','bark')
    bird = Bird('Ravon', 6,'white','bravo!')

    animals = [fish, dog, bird]
    for animal in animals:
        animal.say()
    fish.swim()
    dog.bark()
    bird.fly()