"""
Домашнее задание №8: Сортировка, поиск, регулярные выражения.
2. Дан список целых чисел. Выведите все элементы этого списка в порядке не возрастания значений. Выведите новый список на экран.
"""

def selection_sort(A) -> list[int]:
    """
    Функция сортировки списка целых чисел в порядке не возрастания с использованием алгоритма сортировки выбором.

    Args:
    A (list[int]): Список целых чисел для сортировки.

    Return:
    list[int]: Новый отсортированный список.
    """
    sorted_list = []

    while A:
        # Находим индекс наибольшего элемента в списке A
        max_index = 0
        for i in range(1, len(A)):
            if A[i] > A[max_index]:
                max_index = i

        # Удаляем наибольший элемент из A и добавляем его в отсортированный список
        sorted_list.append(A.pop(max_index))

    return sorted_list


if __name__ == "__main__":
    # Пример ввода
    A = [1, 4, 2, 3, 4]

    # Сортировка списка
    sorted_A = selection_sort(A)

    # Вывод отсортированного списка
    print(" ".join(map(str, sorted_A)))
