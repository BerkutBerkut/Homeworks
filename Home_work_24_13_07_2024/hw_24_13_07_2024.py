"""
Домашнее задание №19: 
Задание №1
а) Напишите функцию, которая будет создавать файл, с задержкой 1 секунду.
б) Запустите циклом 100 таких функций, а также замерьте время.
в) Добавьте функционал многопоточного запуска, с замером времени.
"""

from time import time, sleep
from threading import Thread


# Функция для создания файла
def create_file(filename):
    sleep(1)  # Задержка 1 секунда
    with open(filename, "w") as file:
        file.write("Hello, World!")


def main() -> None:
    """Точка запуска"""
    threads = []
    times = 10
    # Проверка без многопоточного выполнения
    time_start = time()
    for i in range(times):
        create_file(f"file_{i}.txt")
    print(f"Результат без многопоточности {time() - time_start:.4f}")

    # Проверка с многопоточным выполнением
    time_start = time()
    for i in range(times):
        thread = Thread(target=create_file, args=(f"file_{i}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Результат c многопоточностью {time() - time_start:.4f}")


if __name__ == "__main__":
    main()
