import random
import copy
import math

name = 'Max' if 1 < 2 else 'Rom'
print(name)

# записать в список только положительные числа
numbers = [1, 2, 3, 4, 5, -1, -2, -3]

# классический способ
result = []
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

# через функцию filter 
result = filter(lambda number: number > 0, numbers)
print(list(result))

# при помощи генератора
result = [number for number in numbers if number > 0]
print(result)

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# классический способ
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)

# через генератор словаря
result = {pair[0]: pair[1] for pair in pairs}
print(result)

#создать список случайных чисел
import random

numbers = [random.randint(1, 100) for i in range(10)]
print (numbers)

# создать спсок квадратов чисел
numbers = [1, 2, 3, -4]

numbers = [number**2  for number in numbers]
print (numbers)

# создать список имён на букву а
names = ['Дмитрий', 'Руслан', 'Петр', 'Иван', 'Антон']

names = [name for name in names if name.startswith('А')]
print (names)

l = [1, 2, 3]
d = {1: 'a'}

# классический способ
if len(l) > 0 and len(d) > 0:
    print('список и словарь не пустые')
else: 
    print('список и словарь пустые')

# лексикон python
if l and d:
    print('список и словарь не пустые')
else: 
    print('список и словарь пустые')


if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет, потому что первое условие даёт "ложь"')

print([1] and [] and '' and 1)

print([1] and 1 and 20 and 1.1)

if 1 < 2 or math.sqrt(-1):
    print('Ошибки не будет, потому что первое условие даёт "истина"')

print(0 or [] or 8 or 5) # вернёт первое истинное

print(0 or [] or {} or () or 0) # вернёт последнее ложное

numbers = [1, 2, 3, 4, 5, 7, 9]
result = []

for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)

print(result)

result = filter(lambda number: math.sqrt(number) < 2, numbers)
print(list(result))

result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)


a = [1, 2, 3, 4, 5]

b = a[:]
b[1] = 100
print(a)
с = b.copy()
с[1] = 777
print(b)

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)
b[2][2] = 200
print(a)
print(b)

number = None
result = None
try:
    number = int(input('Введите число: '))
    result = 100 / number
except ZeroDivisionError as zde:
    print('деление на ноль')
except Exception as e: 
    print(e)
else:
    print('выполнение при отсутствии ошибок')
finally:
    print(result)

print('Начало')
raise NotImplementedError('что-то пошло не так')
print('Завершение')

###########################################################################################

fructs_list1 = ['яблоко', 'груша', 'слива', 'папайя', 'банан', 'персик']
fructs_list2 = ['груша', 'слива', 'банан', 'помело', 'яблоко', 'абрикос']

def numsGenerator():
    numbers_pos = [random.randint(1, 100) for i in range(10)]
    numbers_neg = [random.randint(1, 100)*(-1) for i in range(10)]
    return numbers_pos + numbers_neg

#1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

result = [fruct for fruct in fructs_list1 if fruct in fructs_list2]
print(result)

#2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
#a. Элемент кратен 3,
#b. Элемент положительный,
#c. Элемент не кратен 4.

numbers = numsGenerator()
print('\n\nОбщий список элементов')
print(numbers)

result = None
result = [number for number in numbers if number % 3 == 0]
print('Список элементов, кратных трём')
print(result)

result = None
result = [number for number in numbers if number > 0]
print('Список положительных элементов')
print(result)

result = None
result = [number for number in numbers if number % 4 > 0]
print('Список элементов, не кратных четырём')
print(result)

#3. Напишите функцию которая принимает на вход список. 
#Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное) 
#   и возвращает результат (желательно применить генератор и тернарный оператор при необходимости). 
#В результате работы функции исходный список не должен измениться.

print('\n\nИзначальный список элементов')
print(numbers)

def newListFunc(numsList):
    result = [math.sqrt(number) if number > 0 else number for number in numsList]
    return result

newList = newListFunc(numbers)
print('Преобразованный список элементов')
print(newList)

#4. Написать функцию которая принимает на вход число от 1 до 100. 
#Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
#Далее написать основной код программы. Пользователь вводит число. 
#Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция. 
#Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

def newFunction(num):
    result = None
    if num == 13:
        raise ValueError('аргументу присвоено недопустимое значение = 13')
    
    return math.pow(num, 2)

strArg = input('\n\nВведите число от 1 до 100: ')
number = None
result = None
try:
    number = int(strArg)
    result = newFunction(number)
except ValueError as ve:
    print(ve)
except Exception as e:
    print('Что-то пошло не так: {}'.format(e))
finally:
    print(result)
