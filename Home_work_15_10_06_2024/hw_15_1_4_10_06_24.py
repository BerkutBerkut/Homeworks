"""Задание №4.
Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить 
новую дату.
Example: (addYears - это имя пользовательской функции)
print (addYears (datetime.date (2015,1,1), -1))
print (addYears (datetime.date (2015,1,1), 0))
print (addYears (datetime.date (2015,1,1), 2))
печати (addYears (datetime.date (2000,2,29), 1))
Output:
2014-01-01
2015-01-01
2017-01-01
2001-03-01
"""

from datetime import date, timedelta


def addYears(input_date, years):
    """
    Функция добавляет указанное количество лет к заданной дате.

    Args:
        date (datetime): Исходная дата.
        years (int): Количество лет, которое нужно добавить.

    Returns:
        datetime: Новая дата после добавления лет.
    """
    try:
        return input_date.replace(year=input_date.year + years)
    except ValueError:
        # Это произойдет, если мы попытаемся заменить 29 февраля на несуществующую дату в невисокосном году.
        return input_date + (
            input_date.replace(year=input_date.year + years, month=1, day=1)
            - input_date.replace(month=1, day=1)
        )


if __name__ == "__main__":
    print(addYears(date(2015, 1, 1), -1))
    print(addYears(date(2015, 1, 1), 0))
    print(addYears(date(2015, 1, 1), 2))
    print(addYears(date(2000, 2, 29), 1))
