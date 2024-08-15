"""
Домашнее задание №11: Работа с комплексными файлами - excel, json, 
word. Git и Jira
а) Создайте json файл в операционной системе, заполните его данными с сайта 
https://jsonplaceholder.typicode.com/todos/
б) Прочитайте этот файл в массив python-словарей.
в) Запишите каждый из этих словарей в отдельный json-файл.
"""

import requests
import json

# Получение данных с сайта и сохранение их в JSON-файл
url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)
data = response.json()

with open("todos.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

# Чтение данных из JSON-файла в массив словарей
with open("todos.json", "r", encoding="utf-8") as json_file:
    todos_list = json.load(json_file)

# Запись каждого словаря в отдельный JSON-файл
for i, todo in enumerate(todos_list, start=1):
    filename = f"todo_{i}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(todo, json_file, indent=4)
