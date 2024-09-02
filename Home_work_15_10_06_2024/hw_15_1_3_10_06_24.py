"""
Домашнее задание №10: Работа с датой и временем. Файлы и каталоги.
Задание №3.
Реализуйте программу, чтобы выбрать все воскресенья определенного года.
"""

import datetime


def get_all_sundays(year):
    """
    Функция находит все воскресенья в заданном году.

    Args:
        year (int): Год.

    Returns:
        list[datetime.date]: Список всех воскресений в году.
    """
    # Определяем 1-ый день года.
    date = datetime.date(year, 1, 1)

    # Переходим к первому воскресенью.
    date += datetime.timedelta(days=(6 - date.weekday()))
    #  Создаем пустой список воскресении.
    sundays = []

    # Определяем условие в котором будем собирать воскресенья.
    while date.year == year:
        # По мере выполнения условия, будем заполнять список, увеличивая каждый раз на 1 неделю.
        sundays.append(date)
        date += datetime.timedelta(weeks=1)
    # Функция возвращает список восресении.
    return sundays


if __name__ == "__main__":
    year = 2023
    sundays = get_all_sundays(year)
    # Выводим на печать каждое воскресенье из списка.
    for sunday in sundays:
        print(sunday.strftime("%d %B %Y"))
