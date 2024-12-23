# Cоздать класс Pair (пара целых чисел); определить метод умножения на число
# и операцию сложения пар (а,b) + (с,d) = (а + b,с + d).
# Определить класс-наследник Money с полями: рубли и копейки.
# Переопределить операцию сложения и определить методы вычитания и деления
# денежных сумм.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    """Класс, представляющий пару целых чисел."""

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def multiply(self, number):
        """Метод умножения пары на число."""
        self.first *= number
        self.second *= number

    def __add__(self, other):
        """Операция сложения двух пар: (a, b) + (c, d) = (a + b, c + d)."""
        if isinstance(other, Pair):
            return Pair(self.first + self.second, other.first + other.second)
        raise ValueError("Операция сложения возможна только с объектом.")

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"


class Money(Pair):
    """Класс для работы с денежными суммами (рубли и копейки)."""

    def __init__(self, rubles, kopecks):
        # Нормализуем значения (переводим излишки копеек в рубли)
        rubles, kopecks = divmod(kopecks + rubles * 100, 100)
        super().__init__(rubles, kopecks)

    def __add__(self, other):
        """Переопределение операции сложения для денежных сумм."""
        if isinstance(other, Money):
            total_rubles = self.first + other.first
            total_kopecks = self.second + other.second
            return Money(total_rubles, total_kopecks)
        raise ValueError("Сложение возможно только с другим объектом Money.")

    def subtract(self, other):
        """Метод вычитания денежных сумм."""
        if isinstance(other, Money):
            total_rubles = self.first - other.first
            total_kopecks = self.second - other.second
            # Обрабатываем ситуацию, когда копейки уходят в минус
            if total_kopecks < 0:
                total_rubles -= 1
                total_kopecks += 100
            return Money(total_rubles, total_kopecks)
        raise ValueError("Вычитание возможно только с другим объектом Money.")

    def divide(self, divisor):
        """Метод деления денежной суммы на число."""
        if divisor != 0:
            total_kopecks = (self.first * 100 + self.second) // divisor
            rubles, kopecks = divmod(total_kopecks, 100)
            return Money(rubles, kopecks)
        raise ValueError("Деление на ноль невозможно.")

    def __repr__(self):
        return f"Money({self.first} руб., {self.second} коп.)"


# Пример использования классов
pair1 = Pair(3, 4)
pair2 = Pair(1, 2)
result_pair = pair1 + pair2
print(result_pair)  # Output: Pair(7, 3)

money1 = Money(5, 150)  # 5 руб. и 150 копеек = 6 руб. и 50 копеек
money2 = Money(3, 75)   # 3 руб. и 75 копеек
result_money = money1 + money2
print(result_money)  # Output: Money(10 руб., 25 коп.)

money3 = Money(10, 50)
money4 = Money(4, 75)
subtraction_result = money3.subtract(money4)
print(subtraction_result)  # Output: Money(5 руб., 75 коп.)

division_result = money3.divide(3)
print(division_result)  # Output: Money(3 руб., 50 коп.)
