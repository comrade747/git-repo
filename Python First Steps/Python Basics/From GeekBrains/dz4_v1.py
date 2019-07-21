print('Задание 1')
def anketa(name, age, city):
    return(f'{name} {age} год(а), проживает в городе {city}.')

print(anketa('Valen', '32', 'msk'))


print('')
print('')
print('Задание 2')

def biggest(x, y, z):
    xyz = [x, y, z]
    return(sorted(xyz, reverse=True)[0])

print('Из чисел 4, 5, 1 наибольшим является:', biggest(4, 5, 1))


print('')
print('')
print('Задание 3')


#player_name = input('Имя игока: ')

player = {
    'name': input('Имя игока1: '),
    'health': 100,
    'damage': 30
}

enemy = {
    'name': input('Имя игока2: '),
    'health': 100,
    'damage': 30
}



def attack(person1, person2):
    var_tmp1=(person1['damage'])
    var_tmp2=(person2['health'])
    var_tmp3=var_tmp2 - var_tmp1
    #print( var_tmp3)
    person2['health'] = var_tmp3



print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])
print('Игрок ', player['name'], 'отакует игрока ', enemy['name'])
attack(player, enemy)
print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])



print('')
print('')
print('Задание 4')

player['armor'] = 1.2
enemy['armor'] = 1.2


def attack2(person1, person2):
    var_tmp1 = person1['damage'] / person2['armor']
    var_tmp2 = person2['health']
    var_tmp3 = var_tmp2 - var_tmp1
    #print( var_tmp3)
    person2['health'] = var_tmp3
    return(var_tmp1)


print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])
print('Игрок ', player['name'], 'отакует по броне игрока ', enemy['name'])
print('Был нанесён урон в размере: ', attack2(player, enemy))
print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])



print('')
print('')
print('Задание 4 Вариант 2 согласно примечанию')



def attack3(person1, person2):
    def damage_diff(person_dd1, person_dd2):
        var_dd_tmp1 = person_dd1['damage'] / person_dd2['armor']
        return(var_dd_tmp1)
    var_tmp2 = person2['health']
    var_tmp1 = damage_diff(person1, person2)
    var_tmp3 = var_tmp2 - var_tmp1
    #print( var_tmp3)
    person2['health'] = var_tmp3
    return(var_tmp1)



print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])
print('Игрок ', player['name'], 'отакует по броне игрока ', enemy['name'])
print('Был нанесён урон в размере: ', attack3(player, enemy))
print('У игрока', enemy['name'], 'осталось жизни:', enemy['health'])
