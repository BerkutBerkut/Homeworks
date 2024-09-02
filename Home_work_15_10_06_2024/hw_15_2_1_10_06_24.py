"""
Работа с датой и временем
Выполните следующие задания:
Задание №1
Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
"""

from datetime import datetime
import pytz


def get_current_times():
    """
    Функция возвращает текущее время по Гринвичу (UTC) и местное время.

    Returns:
        tuple: Время по Гринвичу (UTC) и местное время.
    """
    utc_time = datetime.now(pytz.utc)
    local_time = datetime.now()

    return utc_time, local_time


if __name__ == "__main__":
    utc_time, local_time = get_current_times()

    print(f"Текущее время по Гринвичу (UTC): {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Местное время: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
