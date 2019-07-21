
tel = {'jack': 4098, 'sape': 4139}
#Добавление новое значение по новому ключу
tel['guido'] = 4127
print(tel)
{'jack': 4098, 'sape': 4139, 'guido': 4127}
#получение значения по ключу (выдаст ошибку если такого ключа нет
print("Use key: ",tel['jack'])
#получение значения через метод get (НЕ выдаст ошибку если такого ключа нет
print("Metod get: ",tel.get('jack'))
#удаление пары по ключу
del tel['sape']
tel['irv'] = 4127
print(tel)

#Получение списка всех ключей в словаре
print(list(tel))
['jack', 'guido', 'irv']

#Получение списка всех ключей в словаре отсортированных по алфавиту
print(sorted(tel))

#проверка вхождения ключа в словать с помощью in
if 'guido' in tel:
    print('guido - есть в словаре')
else:
    print('guido - нет в словаре')
if 'jack' not in tel:
    print('jack - есть в словаре')
else:
    print('jack - нет в словаре')


#Варианты построения словарей используя конструкцию dict() или фигурные скобки {}
new_dict=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(new_dict)

new_dict1={x: x**2 for x in (2, 4, 6)}
print(new_dict1)

new_dict2=dict(sape=4139, guido=4127, jack=4098)
print(new_dict2)


#Циклы при работе со словарями
#Получение ключа и занчения в цикле
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#Сортировака словаря по ключу
#Создать список ключей словаря.
#Отсортировать его.
#В цикле for перебрать элементы списка, используя элемент списка как ключ словаря.

d = {'a': 10, 'c': 15, 'b': 4}
list_keys = list(d.keys())
print("keys list= ", list_keys)
print("sorter list= ",list_keys.sort())
for i in list_keys:
    print(i, ':', d[i])

#Отсортировать словарь по значениям сложнее, так как обращаться к элементам словаря можно только по ключам.
# Однако можно создать список кортежей ("ключ", "значение") и отсортировать его по вторым элементам пар.
# Далее в программе используется именно данная упорядоченная структура, а не сам оригинальный словарь.
#Вариант 1
d = {'a': 10, 'b': 15, 'c': 4}
list_d = list(d.items())
print('Сипсок кортежей из начального словаря = ',list_d)

list_d.sort(key=lambda i: i[1])
print("Список, отсортированный по значениям",list_d)

for i in list_d:
    print(i[0], ':', i[1])

#Сортировать словарь невозможно, только чтобы получить представление отсортированного словаря.
# Словари по своей природе беспорядочные, но другие типы, такие как списки и кортежи, - нет.
# Таким образом, вам нужен упорядоченный тип данных для представления отсортированных
# значений, который будет списком - вероятно, списком кортежей.
#Вариант 2
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print("Вариант 2")
print(type(sorted_x))
print(sorted_x)
sorted_x_dict=dict(sorted_x)
print(type(sorted_x_dict))
print(sorted_x_dict, end="\n\n")

#Вариант 3
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print("Вариант 3")
print(type(sorted_x))
print(sorted_x, end="\n\n")

#Вариант 4
import collections
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = collections.OrderedDict(sorted_x)
print("Вариант 4")
print(type(sorted_dict))
print(sorted_dict)