"""
Задание №2
Реализуйте программу, для вычисления количества дней между двумя датами
"""

from datetime import datetime


def days_between_dates(date1_str, date2_str):
    """
    Функция вычисляет количество дней между двумя датами.
    Args:
        date1_str (str): Первая дата в формате 'YYYY-MM-DD'.
        date2_str (str): Вторая дата в формате 'YYYY-MM-DD'.
    Returns:
        int: Количество дней между двумя датами.
    """
    date_format = "%Y-%m-%d"

    # Преобразуем строки в объекты datetime
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    # Вычисляем разницу между датами
    delta = date2 - date1

    return delta.days


if __name__ == "__main__":
    date1 = input("Введите первую дату в формате YYYY-MM-DD: ")
    date2 = input("Введите вторую дату в формате YYYY-MM-DD: ")

    days_between = days_between_dates(date1, date2)

    print(f"Количество дней между {date1} и {date2}: {days_between}")
