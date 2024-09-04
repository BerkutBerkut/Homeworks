"""
Домашнее задание №20: Многопоточное, асинхронное и мультипроцессорное программирование
Выполните следующее задание:
Задание №1
а) Напишите функцию, которая будет создавать файл и записывать в него рандомное 
число, с задержкой 1 секунду.
б) Запустите циклом 1000 таких функций, а также замерьте время.
в) Добавьте функционал мультипоточного (ПОЧЕМУ МУЛЬТИПОТОЧНОЕ? ХОТЯ ТЕМА УРОКА МУЛЬТИПРОЦЕССОРНОЕ ПРОГРАММИРОВАНИЕ) 
запуска, с замером времени. Обязательно посмотрите нагрузку на ЦП в этот момент (через диспетчер задач).
"""


import time
import random
from multiprocessing import Pool

# Функция для создания файла
def create_file_with_random_number(file_index):
    """Создает файл и записывает в него случайное число с задержкой 1 секунда."""
    time.sleep(1)
    random_number = random.randint(1, 100)
    filename = f"file_{file_index}.txt"
    with open(filename, "w") as file:
        file.write(str(random_number))

def main() -> None:

    times = 100

    # Запуск через for
    start_time = time.time()
    for i in range(times):
        create_file_with_random_number(i)
    print(f"Время выполнения: {time.time() - start_time} секунд")


    start_time = time.time()

    with Pool() as pool:
        pool.map(create_file_with_random_number, range(times))

    end_time = time.time()
    print(f"Время выполнения с мультипроцессорностью: {end_time - start_time} секунд")



if __name__ == "__main__":
    main()