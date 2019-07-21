import math
from random import randint, choice, sample, shuffle

from Lib.testModule import get_person, greeting
from hospital.doctors.surgeons import get_surgeons as srgns
from hospital.doctors.nurses import get_nurses as nrs
from hospital.patients.patients import get_patients as ptnts

import hospital.hospital

r = 100
# вычисление длины окружности
print(2*r*math.pi) 
# вычисление площади окружности
print((r**2)*math.pi) 
print(math.pow(r, 2)*math.pi)

x1=10
y1=10
x2=50
y2=100
l = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(l)

f = math.factorial(5)
print(f)

print(randint(0, 100))

players = ['Max', 'Ron', 'Kate', 'Bill', 'Ivan']

print(choice(players))
print(sample(players, 3))

cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
shuffle(cards)
print(cards)

dictPers = dict(name='Leo', age=23, has_car=True)
get_person(**dictPers)

greeting('Hi', 'Kate', 'Leo', True)

srgns()
nrs()
ptnts()

import os
import sys

for parm in sys.argv:
    print(parm)

print(os.name)
print(os.getcwd())
new_path = os.path.join(os.getcwd(), 'newFolder')

if not os.path.exists(new_path):
    os.mkdir(new_path)

sys.displayhook(new_path)
print(sys.platform)

sys.path.append('C:\Temp')
from  myTest_exercise5 import test_exercise5 as te5

te5()

# sys.exit()

#3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
#Вызовите каждую функцию в main.py и проверьте что все работает как надо.

import Lib.moduleExercise5 as me5

#me5.makeDirectories()
#me5.dropDirectories()

me5.processDirectories(me5.makeDirectory)
print('Каталоги созданы')
me5.processDirectories(me5.dropDirectory)
print('Каталоги удалены')

checkList = [1, 2, 3, 4, 23, 34, 54, 65, 45]
elem = me5.chooseElement(checkList)
print(elem)