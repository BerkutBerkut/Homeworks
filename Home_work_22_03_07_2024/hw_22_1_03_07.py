"""
Домашнее задание №17: Объектно-ориентированное программирование
Задание №1
Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных 
операторов:
Проверка на равенство радиусов двух окружностей (операция = =);
Сравнения длин двух окружностей (операции >, <, <=,>=);
Пропорциональное изменение размеров окружности, путем изменения ее радиуса 
(операции + - += -=).
"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.radius

    # Перегрузка оператора сравнения ==
    def __eq__(self, other):
        return self.radius == other.radius

    # Перегрузка оператора сравнения <
    def __lt__(self, other):
        return self.circumference() < other.circumference()

    # Перегрузка оператора сравнения >
    def __gt__(self, other):
        return self.circumference() > other.circumference()

    # Перегрузка оператора сравнения <=
    def __le__(self, other):
        return self.circumference() <= other.circumference()

    # Перегрузка оператора сравнения >=
    def __ge__(self, other):
        return self.circumference() >= other.circumference()

    # Перегрузка оператора +
    def __add__(self, value):
        return Circle(self.radius + value)

    # Перегрузка оператора -
    def __sub__(self, value):
        return Circle(self.radius - value)

    # Перегрузка оператора +=
    def __iadd__(self, value):
        self.radius += value
        return self

    # Перегрузка оператора -=
    def __isub__(self, value):
        self.radius -= value
        return self

    def __str__(self):
        return f"Circle with radius: {self.radius}"


# Примеры использования:
circle1 = Circle(5)
circle2 = Circle(7)

# Проверка на равенство радиусов
print(circle1 == circle2)  # False

# Сравнение длин окружностей
print(circle1 < circle2)  # True
print(circle1 > circle2)  # False
print(circle1 <= circle2)  # True
print(circle1 >= circle2)  # False

# Пропорциональное изменение размеров окружности
circle3 = circle1 + 3
print(circle3)  # Circle with radius: 8

circle1 += 2
print(circle1)  # Circle with radius: 7

circle2 -= 1
print(circle2)  # Circle with radius: 6
