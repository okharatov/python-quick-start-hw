# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

def attack(person1, person2):
    person2['health'] -= person1['damage']

person = {
    'name': 'New Name',
    'health': float(100),
    'damage': float(50)
}

player = person.copy()
enemy = person.copy()

# player['name'] = input('Укажите имя игрока ')
# enemy['name'] =input('Укажите имя врага ')

# attack(player, enemy)
# print(enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import os.path
import json

# Во второй версии добавлены броня и статистика боев
person['armor'] = 1.2
person['wins'] = 0
person['loses'] = 0

#Функция, для попытки получить словарь из json'a
def get_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return {}
  return json_object

def attack_with_armor(person1, person2):
    damage = person1['damage'] / person2['armor']
    person2['health'] -= damage
    return damage

def write_in_file(person):
    with open(person['name'] + '.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(person))


# Функция, которая по имени пользователя поднимает профиль из файла
# или создает новый профиль и сохраняет его в файл
def get_person(name):
    obj = {}
    if os.path.exists(os.path.join(os.getcwd(),f'{name}.txt')):
        with open(name + '.txt', 'r', encoding='utf-8') as f:
            obj = get_json(str(f.read()))

    if not obj or len(obj.keys()) == 0:
        obj = person.copy()
        obj['name'] = name
        write_in_file(obj)
        

    return obj

# Функция для печати лога боя
def print_log(name1, name2, damage1, health2):
    print(f'{name1} наносит сокрушительный удар {name2}, на {damage1}')
    print(f'У {name2} осталось {health2} жизней\n')

def print_stat(person):
    print(f'Текущая статистика {person["name"]}:')
    print(f'Побед: {person["wins"]}')
    print(f'Поражений: {person["loses"]}\n')

def save_and_print_result(person1, person2):
    winner = person1 if person1['health'] > 0 else person2
    loser = person2 if person1['health'] > 0 else person1
    winner['wins'] += 1
    loser["loses"] += 1

    # Поздравление победителей
    print(f'Победу одержал {winner["name"]}')
    print(f'После схватки у него осталось {winner["health"]} здоровья')
    print_stat(winner)

    # Память павших
    print(f'{loser["name"]} пал на поле боя')
    print_stat(loser)
    
    winner['health'] = loser['health'] = person['health']
    write_in_file(winner)
    write_in_file(loser)

#Начало логики 
player_name = input('Укажите имя игрока ')
enemy_name =input('Укажите имя врага ')

player = get_person(player_name)
enemy = get_person(enemy_name)

while (player['health'] > 0 and enemy['health'] > 0):  
  print_log(player["name"], enemy["name"], attack_with_armor(player, enemy), enemy['health'])
  if enemy['health'] > 0:
    print_log(enemy["name"], player["name"], attack_with_armor(enemy, player), enemy['health'])

save_and_print_result(player, enemy)




  
    