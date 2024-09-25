"""
Практическая работа №21: Многопоточное, асинхронное и 
мультипроцессорное программирование
Выполните следующие задания:
Задание №1
а) Напишите функцию, которая будет загружать данные с jsonplaceholder.
б) Запустите циклом 100 таких функций, а также замерьте время.
в) Добавьте функционал асинхронной работы, с замером времени.
"""

import requests
import time
import aiohttp
import asyncio

# Функция для синхронной загрузки данных
def download_data(url):
    response = requests.get(url)
    return response.json()


# Ассинхронная функция для загрузки данных
async def download_data_async(url, session):
    async with session.get(url) as response:
        return await response.json()


# Функция для синхронной загрузки 100 запросов
def run_download_data(urls):
    for url in urls:
        data = download_data(url)
        print(f"Синхронно загруженые данные с {url}: {data}")


# Ассинхронная функция для загрузки 100 запросов
async def asyncio_download_from_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(download_data_async(url, session))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        # Обрабатываем данные или выводим их, например:
        for url, data in zip(urls, results):
            print(f"Асинхронно загруженые данные с {url}: {data}")


def main():
    urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 101)]

    
    # Замер времени синхронной работы
    start_time = time.time()
    run_download_data(urls)
    print(f"Время выполнения синхронной задачи: \n{time.time() - start_time:.4f} секунд.")
    

    # Замер времени ассинхронной работы
    start_time = time.time()
    asyncio.run(asyncio_download_from_urls(urls))
    print(f"Время выполнения асинхронной задачи: \n{time.time() - start_time:.4f} секунд.")


if __name__ == "__main__":
    main()
