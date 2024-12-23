# В некой игре-стратегии есть солдаты и герои. У всех есть свойство,
# содержащее уникальный номер объекта, и свойство, в котором хранится
# принадлежность команде. У солдат есть метод "иду за героем", который
# в качестве аргумента принимает объект типа "герой". У героев есть метод
# увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды.
# В цикле генерируются объекты-солдаты. Их принадлежность команде определяется
# случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится
# на экран. У героя, принадлежащего команде с более длинным списком,
# увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите
# на экран идентификационные номера этих двух юнитов.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный базовый класс для всех игровых персонажей."""

    def __init__(self, unit_id, team):
        self.id = unit_id
        self.team = team

    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения информации о единице."""
        pass


class Hero(Unit):
    """Класс Герой с уникальным номером, принадлежностью к команде, уровнем."""

    def __init__(self, hero_id, team):
        super().__init__(hero_id, team)
        self.level = 1

    def increase_level(self):
        """Увеличение уровня героя на 1."""
        self.level += 1
        print(
            f"Герой {self.id} из команды {self.team} "
            f"повысил уровень до {self.level}."
        )

    def get_info(self):
        """Получение информации о герое."""
        return f"Герой {self.id}, команда {self.team}, уровень {self.level}"


class Soldier(Unit):
    """Класс Солдат с уникальным номером и принадлежностью к команде."""

    def follow_hero(self, hero):
        """Солдат начинает следовать за героем."""
        print(
            f"Солдат {self.id} из команды {self.team} "
            f"следует за героем {hero.id} из команды {hero.team}."
        )

    def get_info(self):
        """Получение информации о солдате."""
        return f"Солдат {self.id}, команда {self.team}"


def main():
    """Основная программа."""
    # Создаем по одному герою для каждой команды
    hero_team1 = Hero(1, "NAVI")
    hero_team2 = Hero(2, "Astralis")

    # Списки для солдат каждой команды
    soldiers_team1 = []
    soldiers_team2 = []

    # Генерация солдат для каждой команды (10 солдат)
    for i in range(10):
        team = random.choice(["NAVI", "Astralis"])
        soldier = Soldier(i + 1, team)

        if team == "NAVI":
            soldiers_team1.append(soldier)
        else:
            soldiers_team2.append(soldier)

    # Выводим размеры списков солдат
    print(f"Количество солдат в команде NAVI: {len(soldiers_team1)}")
    print(f"Количество солдат в команде Astralis: {len(soldiers_team2)}")

    # Определяем, у какой команды больше солдат, и увеличиваем уровень героя
    if len(soldiers_team1) > len(soldiers_team2):
        hero_team1.increase_level()
    elif len(soldiers_team2) > len(soldiers_team1):
        hero_team2.increase_level()
    else:
        print("Количество солдат в обеих командах одинаково.")

    # Отправляем одного солдата из команды NAVI следовать за героем NAVI
    if soldiers_team1:
        soldier = soldiers_team1[0]
        soldier.follow_hero(hero_team1)

    # Выводим идентификационные номера солдата и героя
    print(f"Солдат {soldier.id} следует за героем {hero_team1.id}.")


if __name__ == "__main__":
    main()
