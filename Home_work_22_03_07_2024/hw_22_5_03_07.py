"""
Домашнее задание №17: Объектно-ориентированное программирование
Создайте класс Roman (РимскоеЧисло), представляющий римское число и 
поддерживающий операции +, -, *, /.
При реализации класса:
операции +, -, *, / реализуйте как специальные методы 
методы преобразования как статические методы
"""


class Roman:
    _roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    _int_to_roman = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            self.value = self.roman_to_int(value)
        else:
            raise ValueError("Value must be an integer or a valid Roman numeral string")

    @staticmethod
    def roman_to_int(roman: str) -> int:
        result = 0
        prev_value = 0
        for char in reversed(roman):
            current_value = Roman._roman_to_int[char]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value
        return result

    @staticmethod
    def int_to_roman(number: int) -> str:
        result = []
        for value, numeral in Roman._int_to_roman:
            while number >= value:
                result.append(numeral)
                number -= value
        return "".join(result)

    def __str__(self):
        return self.int_to_roman(self.value)

    # Перегрузка оператора +
    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        return NotImplemented

    # Перегрузка оператора -
    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        return NotImplemented

    # Перегрузка оператора *
    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        return NotImplemented

    # Перегрузка оператора /
    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)  
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Roman):
            return self.value == other.value
        return NotImplemented


# Примеры использования:
roman1 = Roman("X")  
roman2 = Roman("V")  
roman3 = Roman(15)  

# Операции с римскими числами
print(roman1 + roman2)  
print(roman1 - roman2)  
print(roman1 * roman2)  
print(roman1 / roman2)  

# Проверка равенства
print(roman1 == roman2)  # False
print(roman3 == Roman("XV"))  # True
