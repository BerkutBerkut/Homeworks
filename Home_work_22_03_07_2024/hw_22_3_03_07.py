"""
Домашнее задание №17: Объектно-ориентированное программирование
Задание №3
Вам необходимо создать класс Airplane (самолет). 
С помощью перегрузки операторов реализовать: 
Проверка на равенство типов самолетов (операция = =); 
Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
Сравнение двух самолетов по максимально возможному количеству пассажиров на 
борту (операции > < <= >=).
"""

class Airplane:
    def __init__(self, plane, max_passeng, current_passeng):
        self.plane = plane # Тип самолета
        self.max_passeng = max_passeng # Вместимость самолета
        self.current_passeng = current_passeng # Текущее кол-во пассажиров

    # Перегрузка оператора == для проверки равенства типов самолетов
    def __eq__(self, other) -> bool:
        return self.plane == other.plane

    # Перегрузка оператора + для добавления пассажира
    def __add__(self, passeng):
        new_passeng = self.current_passeng + passeng 
        return Airplane(self.plane, self.max_passeng, new_passeng)  

    # Перегрузка оператора - для уменьшения пассажира
    def __sub__(self, passeng):
        new_passeng = self.current_passeng - passeng
        return Airplane(self.plane, self.max_passeng, new_passeng)

    # Перегрузка оператора +=
    def __iadd__(self, passeng):
        self.current_passeng += passeng
        return self

    # Перегрузка оператора -=
    def __isub__(self, passeng):
        self.current_passeng -= passeng
        return self

    # Перегрузка оператора > для сравнения макс-го кол-ва пассажиров
    def __gt__(self, other):
        return self.max_passeng > other.max_passeng

    # Перегрузка оператора < для сравнения макс-го кол-ва пассажиров
    def __lt__(self, other):
        return self.max_passeng < other.max_passeng

    # Перегрузка оператора >= для сравнения макс-го кол-ва пассажиров
    def __ge__(self, other):
        return self.max_passeng >= other.max_passeng

    # Перегрузка оператора <= для сравнения макс-го кол-ва пассажиров
    def __le__(self, other):
        return self.max_passeng <= other.max_passeng

    # Строковое представление самолета
    def __str__(self):
        return f"Тип самолета: {self.plane}, Макс кол-во пассажиров: {self.max_passeng}, Текущее кол-во пассажиров: {self.current_passeng}"


plane_1 = Airplane("Boing 777", 200, 120)
plane_2 = Airplane("Boing 777", 220, 130)
plane_3 = Airplane("Airbus A320", 280, 180)

# Проверка на равенство типов самолетов
print(plane_1 == plane_2)  
print(plane_1 == plane_3)  

# Увеличение и уменьшение количества пассажиров
plane_1 += 31  
print(plane_1) 

plane_2 -= 50 
print(plane_2) 

# Сравнение самолетов по максимальному количеству пассажиров
print (plane_1 < plane_2)  
print (plane_1 <= plane_3)  
