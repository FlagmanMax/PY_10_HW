# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = int(age)
        self.gender = gender

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.lastname} {self.firstname} {self.gender}'

    def get_age(self):
        return self.__age

person = Person('Иван', 'Иванов', 23, 'м')
print(f'{person.full_name() = }')
print(f'{person.get_age() = }')
print(f'{person.birthday() = }')
print(f'{person.get_age() = }')

# print(f'{person.__age}')
print(f'{person._Person__age}')
