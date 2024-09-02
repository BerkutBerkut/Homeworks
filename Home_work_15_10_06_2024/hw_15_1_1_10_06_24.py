""""
Домашнее задание №10: Работа с датой и временем. Файлы и каталоги.
Задание №1.
Реализуйте программу, чтобы получить номер недели.
Date: 2015, 6, 16
Output: 25
"""

import datetime
import time


def get_week_number(year, month, day):
    # Создание объекта даты
    date = datetime.date(year, month, day)

    # Определение первого дня года
    first_day_of_year = datetime.date(year, 1, 1)

    # Нахождение разницы в днях между датой и первым днем года
    day_of_year = (date - first_day_of_year).days + 1

    # Определение дня недели для первого дня года
    first_day_weekday = first_day_of_year.weekday()

    # Рассчет номера недели
    week_number = (day_of_year + first_day_weekday) // 7 + 1

    return week_number


if __name__ == "__main__":
    year = 2015
    month = 6
    day = 16

    week_number = get_week_number(year, month, day)
    print(f"Дата: {year}-{month:02d}-{day:02d}")
    print(f"Номер недели: {week_number}")
