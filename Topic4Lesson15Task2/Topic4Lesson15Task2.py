class Transport: # материнский класс
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity): # метод материнского класса
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport): # создаем дочерний класс
    def __init__(self, name, max_speed, mileage, seating_capacity=50): # переобределяем материнский класс добавляя атрибут вместимость и присваеваем ему значение 50
        super().__init__(name, max_speed, mileage) # определяем значения материнского класса
 
    def seating_capacity(self, capacity=50): # переменной вместимость даем значение 50
        return f'Вместимость одного автобуса {self.name}: {capacity} пассажиров'
 
busVariable = Autobus('Renaul Logan', 180, 12) # передаем значения в дочерний класс
print(busVariable.seating_capacity())
