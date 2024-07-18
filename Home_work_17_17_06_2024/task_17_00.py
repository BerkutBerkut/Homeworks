from functools import reduce 

# Запрос числа у Пользователя
call_numbers = input("Введите числа через пробел: ")

# Конвертация строки чисел в список целых чисел
list_numbers = list(map(int, call_numbers.split()))
print(list_numbers)

# Суммирование списка чисел
sum_numbers = lambda lst : sum(lst)
print(sum_numbers(list_numbers))

# Перемножение списка чисел
mult_numbers = reduce((lambda x, y: x*y), list_numbers)
print(mult_numbers)





