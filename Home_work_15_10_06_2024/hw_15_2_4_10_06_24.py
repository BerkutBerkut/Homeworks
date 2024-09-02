"""
Задание №4
Реализуйте программу на Python, для создания HTML-календаря с данными за 
определенный год и месяц.
"""
import calendar
from datetime import datetime


def generate_html_calendar(year, month):
    """
    Функция создает HTML-календарь для заданного года и месяца.

    Args:
        year (int): Год.
        month (int): Месяц.

    Returns:
        str: HTML-код календаря.
    """
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = cal.formatmonth(year, month)

    return html_calendar


if __name__ == "__main__":
    year = int(input("Введите год: "))
    month = int(input("Введите месяц (1-12): "))

    # Проверка корректности ввода
    if month < 1 or month > 12:
        print("Месяц должен быть в диапазоне от 1 до 12.")
    else:
        html_calendar = generate_html_calendar(year, month)
        print(html_calendar)

        # Запись в файл
        with open("calendar.html", "w", encoding="utf-8") as f:
            f.write(html_calendar)
        print("HTML-календарь сохранен в файл 'calendar.html'.")
