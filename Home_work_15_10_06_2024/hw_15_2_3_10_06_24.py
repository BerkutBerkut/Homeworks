"""
Задание №3
Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и 
секунды

"""
from datetime import datetime


def difference_in_time(date1_str, date2_str):
    """
    Функция вычисляет разницу между двумя датами в днях, часах, минутах и секундах.

    Args:
        date1_str (str): Первая дата в формате 'YYYY-MM-DD HH:MM:SS'.
        date2_str (str): Вторая дата в формате 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        dict: Словарь с разницей в днях, часах, минутах и секундах.
    """
    date_format = "%Y-%m-%d %H:%M:%S"

    # Преобразуем строки в объекты datetime
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    # Вычисляем разницу между датами
    delta = abs(date2 - date1)

    # Извлекаем дни, часы, минуты и секунды из разницы
    days = delta.days
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}


if __name__ == "__main__":
    date1 = input("Введите первую дату в формате 'YYYY-MM-DD HH:MM:SS': ")
    date2 = input("Введите вторую дату в формате 'YYYY-MM-DD HH:MM:SS': ")

    diff = difference_in_time(date1, date2)

    print(
        f"Разница между {date1} и {date2}: {diff['days']} дней, {diff['hours']} часов, {diff['minutes']} минут, {diff['seconds']} секунд"
    )
