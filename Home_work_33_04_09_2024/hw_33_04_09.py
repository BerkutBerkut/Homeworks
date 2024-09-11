"""
Домашнее задание №30: Работа с базой данных. Big data
Выполните следующее задание:
Задание №1
а) Реализуйте запросы на чтение из созданной таблицы: Чтение всех строк.
б) Реализуйте запросы на чтение из созданной таблицы: Чтение одной строки.
в) Реализуйте запросы на запись в созданную таблицу.
г) Реализуйте запросы на удаление строки из созданной таблицы.
"""

import mysql.connector
from mysql.connector import Error


# Подключение к базе данных
connection = mysql.connector.connect(
    host="localhost", 
    user="root",  
    password="кщще", 
    database="MyFirstDB",  # База данных созданная на уроке
)

cursor = connection.cursor()


# Чтение всех строк
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()

for row in rows:
    print(row)  # Вывод каждой строки

# Чтение одной строки
cursor.execute("SELECT * FROM Employees WHERE id = 3")
row = cursor.fetchall()
print(row)

# Запись новой строки в таблицу
insert_query = """INSERT INTO Employees (name, position, selary) VALUES (%s, %s, %s)"""
records = ("Jack Sparrow", "Captain", 99000)
cursor.execute(insert_query, records)
connection.commit()  # Подтверждение изменения
print(f"Добавлена {cursor.rowcount} строка.")


# Удвление из строки по id
sql_delete = "DELETE FROM Employees WHERE id = %s"
cursor.execute(sql_delete, (6,))
connection.commit()  # Подтверждение изменения
print(f"Удалена {cursor.rowcount} строка.")


# Закрываем курсор и соединение
cursor.close()
connection.close()
print("Соединение с MySQL закрыто.")
