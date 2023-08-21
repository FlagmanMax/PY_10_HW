# Hw_02
# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class Atm:

    default_operation_sum_div = 50
    default_interest_percent = float(1.5)
    default_interest_min = 30
    default_interest_max = 600

    default_rich_tax = 10
    default_rich_limit = 5_000_000

    default_bonus_counter = 3
    default_bonus = 3

    def print_total(self):
        print(f"Sum @ your account: {self.__total}")

    def __init__(self,
                 operation_sum_div=default_operation_sum_div,
                 interest_percent = default_interest_percent,
                 interest_min = default_interest_min,
                 interest_max = default_interest_max,
                 rich_tax=default_rich_tax,
                 rich_limit = default_rich_limit,
                 bonus_counter = default_bonus_counter,
                 bonus = default_bonus
                 ):

        self.__total = 0
        self.__counter = 0

        self.__operation_sum_div = operation_sum_div

        self.__interest_percent = interest_percent
        self.__interest_min = interest_min
        self.__interest_max = interest_max

        self.__rich_tax = rich_tax
        self.__rich_limit = rich_limit

        self.__bonus_counter = bonus_counter
        self.__bonus = bonus

    def put_money(self):
        value = int(input(f"Enter summ multiple {self.__operation_sum_div} y.e "))

        if value % self.__operation_sum_div == 0:
            self.__total += value
            self.__counter += 1
        else:
            print("Wong value!")

    def get_money(self):
        value_ = float(input(f"Enter summ multiple {self.__operation_sum_div} y.e. Attention: bank interest rate is {self.__interest_percent}% "))

        if value_ % self.__operation_sum_div == 0:

            interest = round(self.__interest_percent/100.0, 4) * value_
            print(f"{interest=}")
            if interest < self.__interest_min:
                interest = self.__interest_min
            elif interest > self.__interest_max:
                interest = self.__interest_max

            print(f"{interest=}")

            if self.__total < value_ + interest:
                print("Not enough money!")
            else:
                print('Take your money!')
                self.__total -= value_ + interest
                self.__counter += 1
        else:
            print("Wong value!")

    def bonus(self):
        if self.__counter >= self.__bonus_counter:
            self.__total *= (1 + round(self.__bonus/100.0, 4))
            self.__total = round(self.__total, 4)
            self.__bonus_counter = 0
            print(f"{self.__bonus}% - bonus for  {self.__bonus_counter} operations!")

    def rich_tax(self):
        if self.__total > self.__rich_limit:
            self.__total *= (1-self.__rich_tax)
            self.__total = round(self.__total, 4)
            print(f"Налог на богатство: -{self.__rich_tax}%! Сумма на счете {self.__total} ")

    def manager(self):

        operation_ = int(input("Choose operation: 1 - put; 2 - get; 3 - exit: "))

        self.rich_tax()

        if operation_ == 1:
            self.put_money()
        elif operation_ == 2:
            self.get_money()
        elif operation_ == 3:
            print("Goodbye!")
            exit(1)
        else:
            print('Wrong value!')
            pass

    def main(self):
        while True:
            self.print_total()
            self.manager()
            self.bonus()


atm_01 = Atm()
atm_01.main()
