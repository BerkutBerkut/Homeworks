"""
Домашнее задание №17: Объектно-ориентированное программирование
Задание №2
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации арифметических операций по 
работе с комплексными числами (операции +, -, *, /).
"""

class Complex:
    def __init__(self, real, imag):
        """Инициализация комплексного числа."""
        self.real = real  # Действительная часть
        self.imag = imag  # Мнимая часть

    def __add__(self, other):
        """Перегрузка оператора + для сложения комплексных чисел."""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Перегрузка оператора - для вычитания комплексных чисел."""
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Перегрузка оператора * для умножения комплексных чисел."""
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        """Перегрузка оператора / для деления комплексных чисел."""
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо!")
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __str__(self):
        """Строковое представление комплексного числа."""
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


# Примеры использования:
c1 = Complex(3, 2)
c2 = Complex(1, 7)

# Сложение комплексных чисел
c3 = c1 + c2
print(f"{c1} + {c2} = {c3}")  # 3 + 2i + 1 + 7i = 4 + 9i

# Вычитание комплексных чисел
c4 = c1 - c2
print(f"{c1} - {c2} = {c4}")  # 3 + 2i - 1 + 7i = 2 - 5i

# Умножение комплексных чисел
c5 = c1 * c2
print(f"{c1} * {c2} = {c5}")  # 3 + 2i * 1 + 7i = -11 + 23i

# Деление комплексных чисел
c6 = c1 / c2
print(
    f"{c1} / {c2} = {c6}"
)  # 3 + 2i / 1 + 7i = 0.41379310344827586 - 0.4482758620689655i
