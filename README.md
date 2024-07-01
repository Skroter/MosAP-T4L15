<h1 align="center">Урок №15. ООП<a href="https://daniilshat.ru/" target="_blank"></a>
<h1 align="center">Задание No1<p>
<p align="justify">Есть родительский класс:
class Transport:
def __init__(self, name, max_speed, mileage):
self.name = name
self.max_speed = max_speed
self.mileage = mileage
Создайте объект Autobus, который унаследует все переменные и методы
родительского класса Transport и выведете его.
Ожидаемый результат вывода:
Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12</p>
</p>
<h1 align="center">Задание No2<p>
<p align="justify">Создайте класс Autobus, который наследуется от класса Transport.
Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
Используйте переопределение метода.
Используйте следующий код для родительского класса транспортного
средства:
class Transport:
def __init__(self, name, max_speed, mileage):
self.name = name
self.max_speed = max_speed
self.mileage = mileage
def seating_capacity(self, capacity):
return f"Вместимость одного автобуса {self.name} {capacity}
пассажиров"
Ожидаемый результат вывода:
Вместимость одного автобуса Renaul Logan: 50 пассажиров</p>
</p></a>
