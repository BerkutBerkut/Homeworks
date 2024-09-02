"""
Работа с датой и временем
Задание №1
Дан текстовый файл. Необходимо создать новый файл убрав из него все неприемлемые 
слова. Список неприемлемых слов находится в другом файле.
"""

def load_unacceptable_words(filename):
    """
    Загружает список неприемлемых слов из файла.

    Args:
        filename (str): Имя файла со списком неприемлемых слов.

    Returns:
        set: Множество неприемлемых слов.
    """
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    return set(words)


def remove_unacceptable_words(
    input_filename, output_filename, unacceptable_words_filename
):
    """
    Удаляет неприемлемые слова из исходного текстового файла и сохраняет результат в новый файл.

    Args:
        input_filename (str): Имя исходного текстового файла.
        output_filename (str): Имя выходного текстового файла.
        unacceptable_words_filename (str): Имя файла со списком неприемлемых слов.
    """
    # Загружаем список неприемлемых слов
    unacceptable_words = load_unacceptable_words(unacceptable_words_filename)

    with open(input_filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for line in lines:
            words = line.split()
            cleaned_words = [
                word for word in words if word.lower() not in unacceptable_words
            ]
            cleaned_line = " ".join(cleaned_words)
            outfile.write(cleaned_line + "\n")


if __name__ == "__main__":
    input_filename = "input_15_3.txt"  # Имя исходного файла
    output_filename = "output_15_3.txt"  # Имя выходного файла
    unacceptable_words_filename = (
        "unacceptable_words_15_3.txt"  # Имя файла со списком неприемлемых слов
    )

    remove_unacceptable_words(
        input_filename, output_filename, unacceptable_words_filename
    )
    print(f"Файл {output_filename} успешно создан с удалением неприемлемых слов.")
