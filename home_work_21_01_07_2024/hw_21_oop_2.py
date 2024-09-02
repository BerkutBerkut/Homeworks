"""
Домашнее задание №16: Объектно-ориентированное программирование
ООП. Множественное следование
Задание №2
Используя механизм множественного наследования разработайте класс “Автомобиль”. 
Должны быть классы «Колеса», «Двигатель», «Двери».
"""
# Класс Wheels
class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def show_wheels_info(self):
        print(f"У этого автомобиля {self.number_of_wheels} колеса.")


# Класс Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def show_engine_info(self):
        print(f"Мощность автомобиля {self.horsepower} л.с.")


# Класс Doors
class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def show_doors_info(self):
        print(f"Количество дверей у автомобиля {self.number_of_doors}")


# Класс Car
class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def show_car_info(self):
        self.show_wheels_info()
        self.show_engine_info()
        self.show_doors_info()
        print("Данный автомобиль полностью укомплектован.")

# Пример использования
if __name__ == "__main__":
    my_car = Car(number_of_wheels=4, horsepower=150, number_of_doors=4)
    my_car.show_car_info()


