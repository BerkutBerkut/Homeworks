"""
Работа с файлами и каталогами
Задание №3
В текущей папке лежит файл list.tsv, в котором с новой строки написаны имена 
некоторых других файлов этой папки. Создайте папку list и переложите в неё данные файлы.
"""

import os
import shutil


def move_files_to_list_folder(list_file, destination_folder):
    try:
        # Создаем папку для перемещения файлов, если её нет
        os.makedirs(destination_folder, exist_ok=True)

        # Открываем файл list.tsv для чтения
        with open(list_file, "r") as f:
            # Читаем имена файлов из list.tsv
            file_names = f.read().splitlines()

        # Перебираем имена файлов
        for file_name in file_names:
            # Формируем полные пути к текущему и целевому файлам
            source_path = os.path.join(os.getcwd(), file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Перемещаем файл в папку list
            shutil.move(source_path, destination_path)
            print(f"Файл {file_name} перемещен в папку {destination_folder}")

    except Exception as e:
        print(f"Ошибка при перемещении файлов: {e}")


if __name__ == "__main__":
    # Указываем путь к файлу list.tsv и целевую папку
    list_file_path = "list.tsv"
    destination_folder = "list"

    # Вызываем функцию для перемещения файлов
    move_files_to_list_folder(list_file_path, destination_folder)
