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

    def attack(self, per):
        per_is_killed = False
        dmg = self.__calculate_damage(per)
        
        per.health -= dmg

        if per.health <= 0:
            per_is_killed = True

        return per_is_killed


    def __calculate_damage(self, per):
        return self.damage / per.armor


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)
        self.wins = 0
        self.lose = 0

    def choose_target(self, enemy_list):
        return int(input('Введите номер врага для атаки '))

class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)

class GameClass():

    def __init__(self, you):
        # self.__set_params()

        level = int(input(f"{player.name}, введите сложность от 1 до 3 "))
        game_is_over = False
        self.__enemys = [ Enemy(f'Enemy{e}', 60, 30, 2) for e in range(level)]
        self.__print_enemy_info()
        self.__enemys.append(you)

        while not game_is_over:
            for e in self.__enemys:
                if isinstance(e, Enemy):
                    game_is_over = e.attack(list(filter(lambda x: isinstance(x, Player), self.__enemys))[0])
                    print(you.health)
                    if game_is_over:
                        break
                else:
                    self.__print_enemy_info()
                    enem = self.__enemys[e.choose_target(list(filter(lambda x: isinstance(x, Enemy), self.__enemys)))]
                    if e.attack(enem):
                        self.__enemys.remove(enem)
                        if len(self.__enemys) == 1:
                            game_is_over = True
                            break

    def __print_enemy_info(self):
        print(f'\nПротив вас играют противники:')
        [print(f'{i}.   {e.name} , {e.health} жизней, {e.damage} урон, {e.armor} брони') 
            for i, e in enumerate(self.__enemys) if isinstance(e, Enemy)]


player = Player(input("Введите Ваше имя "), 100, 30, 5)

while True:
    GameClass(player)
    answer = ""
    if player.health <= 0:
        answer = input("Вас убили, еще сыграем еще раз? (y/n)")
    else:
        answer = input("Вы победили, сыграем еще раз? (y/n)")

    if answer != "y":
        break
    
    player.health = 100
