"""
Работа с файлами и каталогами
Задание №2
В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п. 
Переименуйте их переставив имя и фамилию местами.
"""

import os


def rename_files(directory):
    try:
        # Перебираем файлы в указанной директории
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                # Разделяем имя файла и расширение
                name, ext = os.path.splitext(filename)

                # Разделяем имя и фамилию
                first_name, last_name = name.split("_")

                # Формируем новое имя файла
                new_filename = f"{last_name}_{first_name}{ext}"

                # Полный путь к текущему и новому файлу
                current_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)

                # Переименовываем файл
                os.rename(current_path, new_path)

                print(f"Файл {filename} переименован в {new_filename}")

    except Exception as e:
        print(f"Ошибка при переименовании файлов: {e}")


if __name__ == "__main__":
    # Указываем текущую директорию
    current_directory = os.getcwd()

    # Вызываем функцию для переименования файлов
    rename_files(current_directory)
