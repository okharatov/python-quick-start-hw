# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def print_info_for_test(self):
        print(self.speed, self.color, self.name, self.is_police)


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)

my_car = TownCar(60, "red", "ласточка")
my_car.print_info_for_test()
my_car.turn("left")
my_car.go()
my_car.stop()

my_car = PoliceCar(60, "red", "бобик")
my_car.print_info_for_test()
my_car.turn("left")
my_car.go()
my_car.stop()