"""
Домашнее задание №09: Итераторы, контейнеры и перечисления.
Выполните следующее задание:
Создать генератор списка из исходного, который:
2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}
"""

# Исходный список
original_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

# Генератор множества
result_set = {x for x in set(original_list) if x % 2 == 0}

# Вывод результата
print(result_set)
