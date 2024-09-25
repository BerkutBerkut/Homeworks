"""
Домашнее задание №22: Сетевое программирование и веб-запросы. 
Парсинг данных
Выполните следующее задание:
Задание №1
а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку 
requests.
б) Сохраните циклом каждый в отдельный файл, в одну новую папку.
а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку 
aiohttp.
б) Сохраните циклом каждый в отдельный файл, в одну новую папку
"""

import os
import requests
import aiohttp
import asyncio
import json

# Синхронный метод
def requests_get_objekt_json(url):
    # Создание папки
    folder_name = "json_requests" 
    os.makedirs(folder_name, exist_ok=True)

    # Синхронная функция загрузки данных с сайта
    response = requests.get(url)
    data = response.json() # Преобразование ответа в json формат

    # Сохранение каждой загрузки в отдельный json файл
    for i, item in enumerate(data[:10]):  # Сохранение первых 10 записей
        file_name = os.path.join(folder_name, f"request-to-file_{i+1}.json")
        with open(file_name, "w") as f:
            json.dump(item, f, indent=4)
        print(f"Файл {file_name} сохранен")


# Ассинхронный метод
async def async_download_json(url):
    # Создание отдельной папки
    folder_name = "json_asyncio"
    os.makedirs(folder_name, exist_ok=True)

    # Ассинхронная функция для загрузки и сохранения данных
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()  # Получаем ответ в формате json.

            # Сохранение каждого объекта в отдельный файл
            for i, item in enumerate(data[:10]):  # Сохранение первых 10 записей
                file_name = os.path.join(folder_name, f"async-to-fail_{i+1}.json")
                with open(file_name, "w") as f:
                    json.dump(item, f, indent=4)
                print(f"Файл {file_name} сохранен")


if __name__ == "__main__":

    # Запуск синхронного метода
    requests_get_objekt_json("http://jsonplaceholder.typicode.com/todos")

    # Запуск ассинхронного метода
    asyncio.run(async_download_json("http://jsonplaceholder.typicode.com/todos"))
