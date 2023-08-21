# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

def auto_repr(*args, **kwargs):
    def decorator(cls):
        def custom_repr(cls):
            args_list = [repr(cls.__getattribute__(i)) for i in args]
            kwargs_list = [f"{i}={repr(cls.__getattribute__(i))}" for i in kwargs]
            result = f"{cls.__class__.__name__}({', '.join(args_list +kwargs_list)})"
            return result
        cls.__repr__ = custom_repr()
        return cls

    return decorator


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

# @auto_repr(level_id)
class Employee(Person):
    def __init__(self, firstname, lastname, age, gender, pers_id):
        if len(pers_id) != 6:
            raise ValueError('Wrong id length')

        super().__init__(firstname, lastname, age, gender)
        self.pers_id = pers_id
        self.level_id = int(pers_id) % 7

    def __str__(self):
        return f"\rИмя: {self.firstname}, Фамилия: {self.lastname}, ID: {self.pers_id}, Level: {self.level_id}"

e_01 = Employee('Вася','Иванов', 23, 'м', '123456')
# print(f'{e_01.full_name() = }')
# print(f'{e_01.level_id = }')

print(e_01)