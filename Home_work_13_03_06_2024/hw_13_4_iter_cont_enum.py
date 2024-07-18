"""
Домашнее задание №09: Итераторы, контейнеры и перечисления.
Выполните следующее задание:
4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7, в диапазоне от 0 до n.
"""

# Функция-генератор для задания 
def divisible_by_7_generator(n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i


n = 50
gen = divisible_by_7_generator(n)
print(f"Числа, которые деляться на 7 в списке из {n} чисел:")
for num in gen:
    print(num, end=" ")


