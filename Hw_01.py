# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from Task_06 import *
from typing import Any

class AnimalFactory:

    def __new__(cls, animal_type, *args, **kwargs) -> [Fish, Dog, Bird, Any]:
        try:
            animal = super().__new__(animal_type)
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as exc:
            # print(f'{exc.__class__.__name__()} {exc}')
            print(f'This animal type "{animal_type}" is not in product line, we will produce a default one)')
            return Animal('Chupacabra', 100)


def main():
    dog_01 = AnimalFactory(Dog, name="Rex", age=5, voice="Bow", breed="Doberman")
    dog_01.say()
    dog_01.bark()

    fish_01 = AnimalFactory(Fish, name="Dori", age=1, voice="Bul", scales="Rainbow" )
    fish_01.say()
    fish_01.swim()
    print(fish_01.get_info())

    something = AnimalFactory('Monkey', name="Abu", age=3)
    something.say()


main()
