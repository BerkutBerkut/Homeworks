""""
Работа с файлами и каталогами
Задание №1
В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me 
и переложите туда содержимое указанных папок (сами папки класть не надо).
"""

import os
import shutil


def move_contents(source_dirs, destination_dir):
    try:
        # Создаем папку для перемещения содержимого, если её нет
        os.makedirs(destination_dir, exist_ok=True)

        # Перебираем исходные папки
        for source_dir in source_dirs:
            # Перебираем файлы и подпапки в исходной папке
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination_dir, file)

                    # Перемещаем файл в новую папку
                    shutil.move(source_path, destination_path)
                    print(f"Файл {file} перемещен в папку {destination_dir}")

    except Exception as e:
        print(f"Ошибка при перемещении файлов: {e}")


if __name__ == "__main__":
    # Указываем исходные и целевую папку
    source_directories = ["video", "sub"]
    destination_directory = "watch_me"

    # Вызываем функцию для перемещения содержимого
    move_contents(source_directories, destination_directory)
