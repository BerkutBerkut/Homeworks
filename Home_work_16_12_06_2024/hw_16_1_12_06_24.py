""" Домашнее задание №11: Работа с комплексными файлами - excel, json, 
word. Git и Jira
Задание №1
а) Прочитайте из трёх excel файлов (заранее создайте их, внутри 1111, 2222, 3333).
б) Отсортируйте полученную матрицу в порядке убывания.
в) Запишите это в один файл, изменив шрифт и обернув в границы.

"""

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

# Создание трех Excel файлов
df1 = pd.DataFrame([1111555])
df2 = pd.DataFrame([2222777])
df3 = pd.DataFrame([3333999])

df1.to_excel("file1.xlsx", index=False, header=False)
df2.to_excel("file2.xlsx", index=False, header=False)
df3.to_excel("file3.xlsx", index=False, header=False)

# Чтение данных из файлов
df1 = pd.read_excel("file1.xlsx", header=None)
df2 = pd.read_excel("file2.xlsx", header=None)
df3 = pd.read_excel("file3.xlsx", header=None)

# Объединение данных в одну матрицу
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Сортировка данных в порядке убывания
sorted_df = combined_df.sort_values(by=0, ascending=False).reset_index(drop=True)

# Создание итогового Excel файла
wb = Workbook()
ws = wb.active

# Запись отсортированных данных в файл
for r in dataframe_to_rows(sorted_df, index=False, header=False):
    ws.append(r)

# Изменение шрифта и добавление границ
font = Font(name="Arial", size=12, bold=True)
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

for row in ws.iter_rows():
    for cell in row:
        cell.font = font
        cell.border = thin_border

# Сохранение итогового файла
wb.save("sorted_combined.xlsx")
