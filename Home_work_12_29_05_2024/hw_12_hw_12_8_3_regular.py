"""
Домашнее задание №8: Сортировка, поиск, регулярные выражения.
Регулярные выражения.
Задание №3. 
Напишите программу, в которой разбивается строка по нескольким разделителям.
"""

import re

def split_by_multiple_delimiters(text, delimiters) -> list[str]:
    """
    Функция для разбиения строки по нескольким разделителям.

    Args:
    text (str): Входной текст.
    delimiters (str): Строка с разделителями.

    Returns:
    list[str]: Список строк, разделённых по заданным разделителям.
    """
    # Создаём регулярное выражение с использованием заданных разделителей
    regex_pattern = "|".join(map(re.escape, delimiters))
    # Разбиваем текст по регулярному выражению
    result = re.split(regex_pattern, text)

    return result


if __name__ == "__main__":
    # Ввод текста
    input_text = input("Введите текст: ")
    # Ввод разделителей
    input_delimiters = input("Введите разделители (в одну строку без пробелов): ")

    # Разбиваем строку по заданным разделителям
    result = split_by_multiple_delimiters(input_text, input_delimiters)

    # Печать результата
    print("Результат разбиения строки:", result)
