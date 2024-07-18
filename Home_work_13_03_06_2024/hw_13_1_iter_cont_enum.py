"""
Домашнее задание №09: Итераторы, контейнеры и перечисления.
Cоздать генератор списка из исходного, который:
1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}
"""

# Исходный список
original_list = [1, 2, 3, 4, 5, 6, 7]

# Генератор словаря
result_dict = {x: x**3 for x in original_list if x % 2 != 0}

# Вывод результата
print(result_dict)
