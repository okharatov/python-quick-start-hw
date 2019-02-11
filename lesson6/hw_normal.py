# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.wins = 0
        self.lose = 0

    def attack(self, per):
        per_is_killed = False
        dmg = self.__calculate_damage(per)
        
        per.health -= dmg

        if per.health <= 0:
            per.lose += 1
            self.wins += 1
            per_is_killed = True

        return per_is_killed


    def __calculate_damage(self, per):
        return self.damage / per.armor


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)

class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)