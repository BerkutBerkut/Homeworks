"""
Домашнее задание №20: Многопоточное, асинхронное и мультипроцессорное программирование
Выполните следующее задание:
Задание №1
а) Напишите функцию, которая будет создавать файл и записывать в него рандомное 
число, с задержкой 1 секунду.
б) Запустите циклом 1000 таких функций, а также замерьте время.
в) Добавьте функционал мультипоточного (ПОЧЕМУ МУЛЬТИПОТОЧНОЕ? ХОТЯ ТЕМА УРОКА МУЛЬТИПРОЦЕССОРНОЕ ПРОГРАММИРОВАНИЕ!) 
запуска, с замером времени. Обязательно посмотрите нагрузку на ЦП в этот момент (через диспетчер задач).
В ЭТОМ ВАРИАНТЕ КОДА СРАВНИВАЮТСЯ ВСЕ ТРИ ВАРИАНТА.
"""

from time import time, sleep
from threading import Thread
import random
from multiprocessing import Pool


# Функция для создания файла
def create_file_with_random_number(file_index):
    sleep(1)  # Задержка 1 секунда
    random_number = random.randint(1, 100)  # Генерация случайного числа от 1 до 100
    filename = f"file_{file_index}.txt"
    with open(filename, "w") as file:
        file.write(str(random_number))


def main() -> None:
    """Точка запуска"""
    threads = []
    times = 1000
    # Проверка без многопоточного выполнения
    time_start = time()
    for i in range(times):
        create_file_with_random_number(i)
    print(f"Результат без многопоточности {time() - time_start} секунд")

    # Проверка с многопоточным выполнением
    time_start = time()
    for i in range(times):
        thread = Thread(target=create_file_with_random_number, args=(i,))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print(f"Результат c многопоточностью {time() - time_start} секунд")

    # Проверка с мультипроцессорным  выполнением
    start_time = time()

    with Pool() as pool:
        pool.map(create_file_with_random_number, range(times))

    end_time = time()
    print(
            f"Время выполнения с мультипроцессорностью: {end_time - start_time} секунд"
        )


if __name__ == "__main__":
    main()
