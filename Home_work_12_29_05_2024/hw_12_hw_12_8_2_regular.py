""" 
Домашнее задание №8: Сортировка, поиск, регулярные выражения.
Регулярные выражения.
Задание №2. 
Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву.
"""

import re

def extract_vowel_words(text) -> list[str]:
    """
    Функция для извлечения слов, начинающихся на гласную букву.

    Args:
    text (str): Входной текст.

    Returns:
    list[str]: Список слов, начинающихся на гласную букву.
    """
    # Разбиваем текст на слова
    words = re.findall(r"\b\w+\b", text)
    # Гласные буквы
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
    # Фильтруем слова, которые начинаются на гласную букву
    vowel_words = [word for word in words if word[0] in vowels]

    return vowel_words

if __name__ == "__main__":
    # Ввод текста
    input_text = input("Введите текст: ")

    # Извлечение слов, начинающихся на гласную букву
    result = extract_vowel_words(input_text)

    # Печать результата
    print("Слова, начинающиеся на гласную букву:", result)
