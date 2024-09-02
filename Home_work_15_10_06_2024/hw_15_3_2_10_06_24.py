"""
Работа с датой и временем
Задание №2
Написать программу транслитерации с русского на английский и наоборот. Данные для 
транслитерации берутся из файла и записываются в другой файл. Направление перевода 
определяется через меню пользователя.
"""

def transliter_table(filename):
    """
    Загружает таблицу транслитерации из файла.

    Args:
        filename (str): Имя файла с таблицей транслитерации.

    Returns:
        dict: Словарь с таблицей транслитерации.
    """
    translit_table = {} # Создаем пустой словарь транслитерации
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():  # Пропускаем пустые строки
                rus_char, eng_char = line.strip().split(":") # Разделяем строку по двоеточию
                # Добавляем русскую и английскую буквы в словарь.
                translit_table[rus_char.strip()] = eng_char.strip()  
                
    return translit_table


def transliterate(text, translit_table):
    """
    Транслитерирует текст с помощью заданной таблицы транслитерации.

    Args:
        text (str): Исходный текст для транслитерации.
        translit_table (dict): Таблица транслитерации.

    Returns:
        str: Транслитерированный текст.
    """
    result = []
    for char in text:
        if char in translit_table:
            result.append(translit_table[char])
        else:
            result.append(char)
    return "".join(result)


def main():
    # Загрузка таблиц транслитерации
    rus_to_eng_table = transliter_table("rus_to_eng.txt")
    eng_to_rus_table = transliter_table("eng_to_rus.txt")

    # Меню выбора направления транслитерации
    print("Выберите направление транслитерации:")
    print("1. Русский -> Английский")
    print("2. Английский -> Русский")
    choice = input("Введите номер: ")

    if choice == "1":
        input_filename = "input_rus.txt"
        output_filename = "output_eng.txt"
        translit_table = rus_to_eng_table
    elif choice == "2":
        input_filename = "input_eng.txt"
        output_filename = "output_rus.txt"
        translit_table = eng_to_rus_table
    else:
        print("Некорректный выбор.")
        return

    # Транслитерация текста и запись результата в файл
    with open(input_filename, "r", encoding="utf-8") as infile:
        text = infile.read()

    transliterated_text = transliterate(text, translit_table)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(transliterated_text)

    print(f"Результат транслитерации сохранен в файл '{output_filename}'.")


if __name__ == "__main__":
    main()
