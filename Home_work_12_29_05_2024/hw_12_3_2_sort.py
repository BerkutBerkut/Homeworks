"""
Домашнее задание №8: Сортировка, поиск, регулярные выражения.
Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к 
элементам массива такой новый элемент, чтобы сумма элементов с положительными 
значениями стала бы равна модулю суммы элементов с отрицательными значениями.
"""

def adjust_array(arr) -> list[int]:
    """
    Функция для добавления нового элемента в массив, чтобы сумма положительных элементов
    стала равна модулю суммы отрицательных элементов.

    Args:
    arr (list[int]): Список чисел.

    Returns:
    list[int]: Обновленный список чисел.
    """
    sum_positive = sum(x for x in arr if x > 0)
    sum_negative = sum(x for x in arr if x < 0)

    needed_element = abs(sum_negative) - sum_positive

    arr.append(needed_element)

    return arr


if __name__ == "__main__":
    # Ввод массива
    array = [-3, -2, 1, 2, 3, 4]

    # Печать начального массива и суммы
    print("Initial array:", array)
    sum_positive = sum(x for x in array if x > 0)
    sum_negative = sum(x for x in array if x < 0)
    print("Sum of positive elements:", sum_positive)
    print("Sum of negative elements:", sum_negative)

    # Печать необходимого элемента
    needed_element = abs(sum_negative) - sum_positive
    print("Needed element:", needed_element)

    # Обновление массива
    updated_array = adjust_array(array)

    # Печать обновленного массива
    print("Updated array:", updated_array)
