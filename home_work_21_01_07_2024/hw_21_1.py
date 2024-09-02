"""
Домашнее задание №16: Объектно-ориентированное программирование
Выполните следующее задания:
Задание №1
Создайте класс Device, который содержит информацию об устройстве. С помощью 
механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о 
кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder 
(содержит информацию о мясорубке). Каждый из классов должен содержать необходимые 
для работы методы.
"""

# Основной класс Device
class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Power: {self.power}W"


# Класс CoffeeMachine
class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity, coffee_type):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity  # in liters
        self.coffee_type = coffee_type

    def make_coffee(self):
        return f"Making a cup of {self.coffee_type} coffee..."

    def info(self):
        base_info = super().info()
        return f"{base_info}, Water Capacity: {self.water_capacity}L, Coffee Type: {self.coffee_type}"


# Класс Blender
class Blender(Device):
    def __init__(self, brand, model, power, capacity, speed_settings):
        super().__init__(brand, model, power)
        self.capacity = capacity  # in liters
        self.speed_settings = speed_settings  # list of speed settings

    def blend(self, speed):
        if speed in self.speed_settings:
            return f"Blending at {speed} speed..."
        else:
            return "Invalid speed setting!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Capacity: {self.capacity}L, Speed Settings: {', '.join(map(str, self.speed_settings))}"


# Класс MeatGrinder
class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_material):
        super().__init__(brand, model, power)
        self.blade_material = blade_material

    def grind_meat(self):
        return "Grinding meat..."

    def info(self):
        base_info = super().info()
        return f"{base_info}, Blade Material: {self.blade_material}"


# Пример использования
if __name__ == "__main__":
    coffee_machine = CoffeeMachine("Nespresso", "X123", 1500, 1.2, "Espresso")
    blender = Blender("Philips", "HR3573", 700, 2.0, [1, 2, 3, 4, 5])
    meat_grinder = MeatGrinder("Bosch", "MFW45020", 1600, "Stainless Steel")

    # Вывод информации о каждом устройстве
    print(coffee_machine.info())
    print(blender.info())
    print(meat_grinder.info())

    # Использование методов устройств
    print(coffee_machine.make_coffee())
    print(blender.blend(3))
    print(meat_grinder.grind_meat())

