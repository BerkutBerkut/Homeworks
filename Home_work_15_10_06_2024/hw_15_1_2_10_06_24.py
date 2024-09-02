"""
Домашнее задание №10: Работа с датой и временем. Файлы и каталоги.
Задание №2.
Реализуйте программу, чтобы найти дату первого понедельника данной недели. 
Date: 2015, 50
Output: пн 14 декабря 00:00:00 2015
"""

import datetime


def find_first_monday(year, week_number):
    """
    Функция находит дату первого понедельника для заданного года и номера недели.

    Args:
        year (int): Год.
        week_number (int): Номер недели.

    Returns:
        datetime.date: Дата первого понедельника.
    """
    # Определяем дату первого дня года
    first_day_of_year = datetime.date(year, 1, 1)

    # Определяем день недели для первого дня года (0 - понедельник, 6 - воскресенье)
    first_day_weekday = first_day_of_year.weekday()

    # Определяем дату первого понедельника года
    if (
        first_day_weekday <= 3
    ):  # Если первый день года - понедельник, вторник, среда или четверг
        first_monday = first_day_of_year - datetime.timedelta(days=first_day_weekday)
    else:  # Если первый день года - пятница, суббота или воскресенье
        first_monday = first_day_of_year + datetime.timedelta(
            days=(7 - first_day_weekday)
        )

    # Находим дату первого понедельника нужной недели
    desired_monday = first_monday + datetime.timedelta(weeks=week_number - 1)

    return desired_monday


if __name__ == "__main__":
    year = 2015
    week_number = 50

    first_monday = find_first_monday(year, week_number)
    print(f"пн {first_monday.strftime('%d %B %H:%M:%S %Y')}")
