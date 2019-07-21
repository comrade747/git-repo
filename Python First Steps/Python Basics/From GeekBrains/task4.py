#Задание1:
# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def about_user (name, age, city):

# Функция принимает имя, возраст и город пользователя и возвращает форматированную строку с этими данными

    result = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
    return result

name = input('Привет! Укакжите свое имя, пожалуйста: ')
age = input('Укажите Ваш возраст: ')
city = input('Укажите город Вашего проживания: ')

result = about_user(name, age, city)
print(result)

# Задание2:
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(a, b, c):

# Функция принимает 3 числа и возвращает самое большое из них

  num_list = [a,b,c]
  max_num = (max(num_list))
  return max_num

num_1 = int (input('Введите значение первого числа: '))
num_2 = int (input('Введите значение второго числа: '))
num_3 = int (input('Введите значение третьего числа: '))

result = max_number(num_1, num_2, num_3)
print('Максимальное число из введеных вами: {}'.format(result))

# Задание3
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

import random

player = {'player': input('Введите имя игрока:'),
          'health': random.randint(50, 100),
          'damage': random.randint(25, 50)}

enemy = {'player': input('Введите имя врага:'),
         'health': random.randint(50, 100),
         'damage': random.randint(25, 50)}

print('Создан игрок: ', player)
print('Создан враг: ', enemy)


def attack(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage'])})
    return person2['health']


def game(step=1):
    while step>0:
        xwho = bool(random.getrandbits(1))
        if xwho:
            attack(enemy, player)
            print('Нанесён урон игроку {} : {}'.format(player['player'], player['health']))
        else:
            attack(player, enemy)
            print('Нанесён урон врагу {} : {}'.format(enemy['player'], enemy['health']))

        if player['health'] <=0 or enemy['health'] <= 0:
            print('Игра окончена')
            if player['health'] > enemy['health']:
                print('Победил игрок')
            elif enemy['health'] > player['health']:
                print('Победил враг')
            elif enemy['health'] == player['health']:
                print('Ничья')
            break
        step -= 1

game(10)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности,
# добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и
# возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон,
# вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt

# Напишите функцию, которая будет считывать файл игрока и его врага,
# получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям
# поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и
# количество оставшихся единиц здоровья.

print('****************' * 2)

player.update({
    'health': random.randint(50,100),
    'damage': random.randint(25,50),
    'armor': 1.2})
enemy.update({
    'health': random.randint(50,100),
    'damage': random.randint(25,50),
    'armor': 1.2})

print('Создан игрок: ', player)
print('Создан враг: ', enemy)


# Наносим повреждение игроку
def attack_armor(person1, person2):
    person2.update({'health': int(person2['health'] - person1['damage']/person1['armor'])})
    # print('attack_armor', person2['player'], person2['health'])
    return person2['damage']


# Наносим повреждение armor
def damage_armor(person1):
    person1.update({'armor': round(person1['armor'] - random.uniform(0,0.1),1)})
    if person1['armor'] < 1:
        person1.update({'armor':1})
    # print('damage_armor', person1['player'], person1['armor'])
    return person1['armor']


def game2(step=1):
    step1 = step
    while step > 0:
        xwho = bool(random.getrandbits(1))
        print('Шаг {}'.format(step1-(step-1)))
        if xwho:
            # enemy -> player
            if player['armor'] > 1:
                damage_armor(player)
                # attack_armor(enemy, player)
            else:
                attack_armor(enemy, player)
            print('Нанесён урон игроку {} : {} {} {}'
                  .format(player['player'], player['health'],
                          player['armor'], player['damage']))
            # print(player)
        else:
            if enemy['armor'] > 1:
                damage_armor(enemy)
                # attack_armor(player, enemy)
            else:
                attack_armor(player, enemy)
            print('Нанесён урон врагу {} : {} {} {}'
                  .format(enemy['player'], enemy['health'],
                          enemy['armor'], enemy['damage']))
            # print(enemy)
        if player['health'] <=0 or enemy['health'] <= 0:
            print('Игра окончена')
            if player['health'] > enemy['health']:
                print('Победил игрок, :), здоровье {}'.format(player['health']))
            elif enemy['health'] > player['health']:
                print('Победил враг, Ж(, здоровье {}'.format(enemy['health']))
            elif enemy['health'] == player['health']:
                print('Ничья, игрок {}, враг {}'.format(player['health'], enemy['health']))
            break
        step -= 1


game2(100)


def save_player(person):
    with open(person['player'] + '.txt', 'w', encoding='UTF-8') as f:
        f.write('{} {}\n'.format('player', person['player']))
        f.write('{} {}\n'.format('health', person['health']))
        f.write('{} {}\n'.format('damage', person['damage']))
        f.write('{} {}\n'.format('armor', person['armor']))


save_player(player)
save_player(enemy)

def read_player(person):
    p = {}
    with open(person['player'] + '.txt', 'r', encoding='UTF-8') as f:
        for i in f:
            j, k = i.split()
            print(j, k)
            p[j] = k
    p['health'] = int(p['health'])
    p['damage'] = int(p['damage'])
    p['armor'] = round(float(p['armor']),1)
    return p

# ***

player = {'player': input('Введите имя игрока:'),
          'health': random.randint(50, 100),
          'damage': random.randint(25, 50),
          'armor': 1.2}

enemy = {'player': input('Введите имя врага:'),
         'health': random.randint(50, 100),
         'damage': random.randint(25, 50),
         'armor': 1.2}


save_player(player)
save_player(enemy)

# ***


player = read_player(player)
enemy = read_player(enemy)

print('Создан игрок: ', player)
print('Создан враг: ', enemy)

# ***

game2(100)