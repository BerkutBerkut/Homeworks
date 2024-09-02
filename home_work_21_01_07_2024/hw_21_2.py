"""
Домашнее задание №16: Объектно-ориентированное программирование
Задание №2
Создайте класс Ship, который содержит информацию о корабле. С помощью механизма 
наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer 
(содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере). 
Каждый из классов должен содержать необходимые для работы методы. 
"""


# Основной класс Ship
class Ship:
    def __init__(self, name, displacement, speed):
        self.name = name
        self.displacement = displacement  # в тоннах
        self.speed = speed  # в узлах

    def info(self):
        return f"Name: {self.name}, Displacement: {self.displacement} tons, Speed: {self.speed} knots"


# Класс Frigate
class Frigate(Ship):
    def __init__(self, name, displacement, speed, num_missiles):
        super().__init__(name, displacement, speed)
        self.num_missiles = num_missiles  # количество ракет

    def launch_missile(self):
        if self.num_missiles > 0:
            self.num_missiles -= 1
            return "Missile launched!"
        else:
            return "No missiles left to launch!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Number of Missiles: {self.num_missiles}"


# Класс Destroyer
class Destroyer(Ship):
    def __init__(self, name, displacement, speed, num_torpedoes):
        super().__init__(name, displacement, speed)
        self.num_torpedoes = num_torpedoes  # количество торпед

    def launch_torpedo(self):
        if self.num_torpedoes > 0:
            self.num_torpedoes -= 1
            return "Torpedo launched!"
        else:
            return "No torpedoes left to launch!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Number of Torpedoes: {self.num_torpedoes}"


# Класс Cruiser
class Cruiser(Ship):
    def __init__(self, name, displacement, speed, num_guns):
        super().__init__(name, displacement, speed)
        self.num_guns = num_guns  # количество пушек

    def fire_gun(self):
        if self.num_guns > 0:
            return "Gun fired!"
        else:
            return "No guns left to fire!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Number of Guns: {self.num_guns}"

# Пример использования
if __name__ == "__main__":
    frigate = Frigate("USS Freedom", 3200, 30, 16)
    destroyer = Destroyer("USS Arleigh Burke", 9200, 35, 8)
    cruiser = Cruiser("USS Ticonderoga", 9800, 32, 6)

    # Вывод информации о каждом корабле
    print(frigate.info())
    print(destroyer.info())
    print(cruiser.info())

    # Использование методов кораблей
    print(frigate.launch_missile())
    print(frigate.info())
    print(destroyer.launch_torpedo())
    print(destroyer.info())
    print(cruiser.fire_gun())
    print(cruiser.info())
