"""
Домашнее задание №17: Объектно-ориентированное программирование
Задание №4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
Проверка на равенство площадей квартир (операция ==);
Проверка на неравенство площадей квартир (операция !=);
Сравнение двух квартир по цене (операции > < <= >=).
"""


class Flat:
    def __init__(self, area, price):
        self.area = area  # Площадь квартиры в квадратных метрах
        self.price = price  # Цена квартиры

    # Перегрузка оператора == для проверки равенства площадей квартир
    def __eq__(self, other):
        return self.area == other.area

    # Перегрузка оператора != для проверки неравенства площадей квартир
    def __ne__(self, other):
        return self.area != other.area

    # Перегрузка оператора > для сравнения по цене
    def __gt__(self, other):
        return self.price > other.price

    # Перегрузка оператора < для сравнения по цене
    def __lt__(self, other):
        return self.price < other.price

    # Перегрузка оператора >= для сравнения по цене
    def __ge__(self, other):
        return self.price >= other.price

    # Перегрузка оператора <= для сравнения по цене
    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return f"Квартира: Площадь = {self.area} кв.м, Цена = {self.price} руб."


# Примеры использования
flat1 = Flat(50, 5000000)
flat2 = Flat(75, 7500000)
flat3 = Flat(50, 5500000)

# Проверка на равенство и неравенство площадей квартир
print(flat1 == flat2)  # False
print(flat1 == flat3)  # True
print(flat1 != flat3)  # False

# Сравнение по цене
print(flat1 > flat2)  # False
print(flat1 < flat2)  # True
print(flat2 >= flat3)  # True
print(flat3 <= flat1)  # False
