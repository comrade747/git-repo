def get_person(**kwargs): # передаётся словарь
    for k, v in kwargs.items():
        print(k, v)

dict1 = dict(name='Leo', age=23, has_car=True)
get_person(**dict1)

def greeteing(say='Hello', *args): # передаётся кортеж
    print(say, who)

greeteing('Hi', 'Kate', 'Leo', True)

#args = [3]
args = [1,6,2]
f = range(*args)
print(list(f))

f = range(1,9)
print(list(f))

def my_filter(numbers, f):
    result = []
    for number in numbers:
        if f(number):
            result.append(number)
    return result

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 != 0

numbers = tuple(range(1,9))
print(numbers)

r = my_filter(numbers, is_even)
print(r)

r = my_filter(numbers, is_not_even)
print(r)

r = my_filter(numbers, lambda arg: arg % 2 == 0) # вместо функции is_even используем лямбда выражение
print(r)

print(sorted(numbers))
print(sorted(numbers, reverse=True))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda value: value[1])
print(pairs)

cities = [('Москва', 1000), ('Эр Рияд', 10000), ('Лондон', 2000), ('Токио', 4000), ('Нью-Йорк', 8000)]
print(sorted(cities))
cities.sort(key=lambda val: val[1])
print(cities)
print(list(filter(lambda arg: len(arg[0]) > 5, cities)))

numbers = [6, 5, 7, 8, 3, 2, 1, 9, 6, 4, 9]
print(list(map(lambda arg: arg**2, numbers)))
print(list(map(lambda arg: str(arg), numbers)))


#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
#Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def printContact(name, age, town):
    result = '{}, {} год(а), проживает в городе {}'.format(name, age, town)
    return result

strContact = printContact ('Василий', 21, 'Москва')
print(strContact)

#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def maxValue(n1, n2, n3):
    my_list = [n1, n2, n3]
    return max(my_list)

mVal = maxValue(23, 32, 34)
print(mVal)

#3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#name - строка полученная от пользователя,
#health = 100,
#damage = 50. 
#### Поэкспериментируйте с значениями урона и жизней по желанию. 
#### Теперь надо создать функцию attack(person1, person2). 
#Примечание: имена аргументов можете указать свои. 
#### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
#### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
#Функция должна сама работать со словарями и изменять их значения.

player = dict(name='Ivan', health=100, damage=50)
enemy = dict(name='Kate', health=80, damage=35)

# enemy.health - player.damage

def attack(attacker, attacked): #атакующий и атакуемый
    enemyHealth = attacked['health'] - attacker['damage']
    return dict(name=attacked['name'], health=enemyHealth, damage=attacked['damage'] )

enemy = attack(player, enemy)
print (enemy)

#4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#Наносит урон. Это улучшенная версия функции из задачи 3.
#Вычисляет урон по отношению к броне.
#Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

player = dict(name='Ivan', health=100, damage=50, armor=1.5)
enemy = dict(name='Kate', health=80, damage=35, armor=2)

def attack(attacker, attacked): #атакующий и атакуемый
    enemyHealth = getHealth(attacked['health'], attacker['damage'], attacked['armor'])
    attacked.update({'health': enemyHealth})
    return dict(name=attacked['name'], health=enemyHealth, damage=attacked['damage'] )

def getHealth(health, damage, armor):
    return round(health - damage / armor, 0)

enemy1 = attack(player, enemy)
print (enemy)
print (enemy1)

player = attack(enemy, player)
print (player)
