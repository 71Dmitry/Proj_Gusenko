'''
7 Создание базового класса "Транспортное средство" и его наследование для создания
классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
общие свойства, такие как максимальная скорость и количество колес, а
классы- наследники будут иметь свои уникальные свойства и методы.
'''
class Transport:
    def __init__(self, max_speed, num_wheels, color):
        self.max_speed = max_speed
        self.num_wheels = num_wheels
        self.color = color

class Car(Transport):
    def __init__(self, max_speed, num_wheels, color, brand):
        super().__init__(max_speed, num_wheels, color)
        self.brand = brand

    def honk(self):
        return "Beep beep!"

class Motorcycle(Transport):
    def __init__(self, max_speed, num_wheels, color, type):
        super().__init__(max_speed, num_wheels, color)
        self.type = type

    def wheelie(self):
        return "Doing a wheelie!"

# Пример использования
car = Car(200, 4, "Red", "Toyota")
print(car.max_speed)  # Выводит: 200
print(car.honk())  # Выводит: Beep beep!

motorcycle = Motorcycle(180, 2, "Blue", "Sport")
print(motorcycle.color)  # Выводит: Blue
print(motorcycle.wheelie())  # Выводит: Doing a wheelie!
