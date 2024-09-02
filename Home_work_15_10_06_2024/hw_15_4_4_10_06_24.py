"""
Работа с файлами и каталогами
Задание №4
Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой 
файл.
"""


def remove_last_line(input_file, output_file):
    try:
        # Читаем все строки из исходного файла
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Если файл пустой, выводим сообщение и завершаем функцию
        if not lines:
            print("Файл пустой, невозможно удалить последнюю строку.")
            return

        # Удаляем последнюю строку
        lines.pop()

        # Записываем оставшиеся строки в новый файл
        with open(output_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(
            f"Последняя строка файла {input_file} удалена. Результат записан в {output_file}."
        )

    except Exception as e:
        print(f"Ошибка при удалении последней строки файла: {e}")


if __name__ == "__main__":
    input_file = "input_1.txt"  # Исходный файл
    output_file = "output_1.txt"  # Файл для записи результата

    # Вызываем функцию для удаления последней строки
    remove_last_line(input_file, output_file)
