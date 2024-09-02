"""
Домашнее задание №16: Объектно-ориентированное программирование
ООП. Множественное наследование
Задание №1
Используя понятие множественного наследования, разработайте класс «Окружность, 
вписанная в квадрат». 
"""
# Класс Square
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return 4 * self.side_length

    def info(self):
        return f"Квадрат со сторонами {self.side_length}"


# Класс Circle
class Circle:
    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return 3.14159 * self.radius**2

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def info(self):
        return f"Окружность с радиусом {self.radius}"


# Класс CircleInSquare
class CircleInSquare(Square, Circle):
    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(
            self, side_length
        )  # Диаметр круга равен длине стороны квадрата

    def info(self):
        square_info = Square.info(self)
        circle_info = Circle.info(self)
        return f"{square_info} и {circle_info} (круг вписанный в квадрат)"


# Пример использования
if __name__ == "__main__":
    side_length = 10
    inscribed_circle_square = CircleInSquare(side_length)

    print(inscribed_circle_square.info())
    print(f"Площадь квадрата: {inscribed_circle_square.area()}")
    print(f"Перимметр квадрата: {inscribed_circle_square.perimeter()}")
    print(f"Площадь окружности: {inscribed_circle_square.area()}")
    print(f"Длина окружности: {inscribed_circle_square.circumference()}")
