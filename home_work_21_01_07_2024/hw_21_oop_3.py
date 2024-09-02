"""
Домашнее задание №16: Объектно-ориентированное программирование
ООП. Множественное следование
Задание №3
Создайте базовый класс Shape для рисования плоских фигур. 
Определите методы: 
Show() — вывод на экран информации о фигуре; 
Save() — сохранение фигуры в файл; 
Load() — считывание фигуры из файла. 
Определите производные классы: 
Square — квадрат, который характеризуется координатами левого верхнего угла и 
длиной стороны; 
Rectangle — прямоугольник с заданными координатами верхнего левого угла и 
размерами; 
Circle — окружность с заданными координатами центра и радиусом; 
Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него 
прямоугольника со сторонами, параллельными осям координат, и размерами этого 
прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список 
и отобразите информацию о каждой из фигур.
"""


import json

# Базовый класс Shape
class Shape:
    def show(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод")

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


# Производные классы
class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(
            f"Квадрат: Коорд верхнего левого угла ({self.x}, {self.y}), Длина стороны {self.side_length}"
        )


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Прямоугольник: Коорд верхнего левого угла ({self.x}, {self.y}), Ширина {self.width}, Высота {self.height}"
        )


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        print(
            f"Окружность: Коорд центра ({self.center_x}, {self.center_y}), Радиус {self.radius}"
        )


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Эллипс: Коорд верхнего левого угла ({self.x}, {self.y}), Ширина {self.width}, Высота {self.height}"
        )

# Пример использования
if __name__ == "__main__":
    # Создаем список фигур
    shapes = [
        Square(0, 0, 10),
        Rectangle(1, 1, 20, 10),
        Circle(5, 5, 15),
        Ellipse(2, 2, 30, 20),
    ]

    # Сохраняем фигуры в файл
    for i, shape in enumerate(shapes):
        shape.save(f"shape_{i}.json")

    # Загружаем фигуры из файла в новый список
    loaded_shapes = []
    for i in range(len(shapes)):
        if i == 0:
            loaded_shapes.append(Square.load(f"shape_{i}.json"))
        elif i == 1:
            loaded_shapes.append(Rectangle.load(f"shape_{i}.json"))
        elif i == 2:
            loaded_shapes.append(Circle.load(f"shape_{i}.json"))
        elif i == 3:
            loaded_shapes.append(Ellipse.load(f"shape_{i}.json"))

    # Выводим информацию о каждой загруженной фигуре
    for shape in loaded_shapes:
        shape.show()
