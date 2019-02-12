# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class AnimalToy(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.toy_type = 'animal'

class MovieToy(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.toy_type = 'movie'

class Factory:
    def __buy_material(self):
        print('материал закуплен') 
        
    def __build(self):
        print('игрушка сшита') 
        
    def __paint(self):
        print('игрушка окрашена') 
        
    def make_toy(self, name, color, toy_type):
        self.__buy_material() 
        self.__build()
        self.__paint()
        
        if toy_type == 'movie':
            return MovieToy(name, color) 
        else:
            return AnimalToy(name, color)

f = Factory()
print(isinstance(f.make_toy('мишка', 'белый', 'animal'), AnimalToy))
print(isinstance(f.make_toy('покемон', 'желтый', 'movie'), MovieToy))