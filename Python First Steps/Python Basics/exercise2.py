friends = 'Максим Леонид'

print(len(friends))

listFriends = friends.split()
print(listFriends[1])

strHello = 'Привет {}, тебе {} лет'.format(listFriends[0], 30)
print(strHello)

friends = []

friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
    }
friends.append(friend)

friend = {
    'name': 'Ivan',
    'age': 13,
    'has_car': False
    }
friends.append(friend)

for key in friend.keys():
    print(key)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(2))
print(f(33))

print(range(3, 6))
args = [3,6]
f = range(*args)
print(f)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda value: value[1])
print(pairs)

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a+b

fib(2000)

print ('Соревнования по Python')
intMembers = None
i = 0
listMembers = []

while True:
    try:
        strMembers = input('Укажите количество участников: ')
        intMembers = int(strMembers)
        break
    except:
        print('Невозможно преобразовать {} в число'.format(strMembers))

while i < intMembers:
    member_name = input('Укажите имя участника, занявшего {} место: '.format(i+1))
    listMembers.append(member_name)
    i += 1

result = listMembers[:3]

print('Победители {}, поздравляем'.format(result))
print('Победители ', result,', поздравляем')

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_set_1 = set(my_list_1)
my_set_2 = set(my_list_2)

print(my_set_1)
print(my_set_2)

my_set = my_set_1.difference(my_set_1.intersection(my_set_2))
print(my_set)

heroes1 = ['Batman','Superman','Wonder Woman','Flash','Aquaman','Cyborg','Batman']
heroes2 = ['Batman','Superman']
for element in heroes2:
    while element in heroes1:
        heroes1.remove(element)
print (heroes1)

#1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
my_list_1 = [4, 5, 12, 2, 8, 12, 2]
my_list_2 = [2, 7, 3]

for item in my_list_2:
    if item in my_list_1:
        cnt = my_list_1.count(item)
        i = 0
        while i < cnt:
            my_list_1.remove(item)
            i += 1

print (my_list_1)

#2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
#Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

listOnes = ['', 'первое ', 'второе ', 'третье ', 'четвертое ', 'пятое ', 'шестое ', 'седьмое ', 'восьмое ', 'девятое ', 'десятое ', 'одиннадцатое ', 'двеннадцатое ', 'триннадцатое ', 'четырнадцатое ', 'пятнадцатое ', 'шестнадцатое ', 'семнадцатое ', 'восемнадцатое ', 'девятнадцатое ']
listTwenties = ['', 'двадцатое', 'двадцать ', 'тридцать ']
listMonths = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

from datetime import date

intYear = None
intMonth = None
intDay = None

while True:
    try:
        strDate = input('Укажите дату в формате dd.MM.yyyy: ')
        listDate = strDate.split('.')
        
        intYear = int(listDate[2])
        intMonth = int(listDate[1])
        intDay = int(listDate[0])

        if intYear > 9999:
            print('Указанное в качестве года значение {} слишком велико - Должно быть не более 9999'.format(intYear))
            continue
        if intMonth > 12:
            print('Указанное в качестве месяца значение {} слишком велико - в году не может быть не более 12'.format(intMonth))
            continue
        if intDay > 31:
            print('Указанное в качестве дней месяца значение {} слишком велико - их количество не должно превышать 31'.format(intDay))
            continue
        if intDay > 29 and intMonth == 2:
            print('В феврале не может быть более 29 дней')
            continue

        dateDate = date(intYear, intMonth, intDay)
        break
    except:
        print('Не удаётся конвертировать {} в дату'.format(strDate))

daysOnes = dateDate.day % 10 # единицы дней
daysTwenties = dateDate.day // 10 # десятки дней

# адаптация общего подхода к особенностям русского языка 
if daysTwenties == 1:
    daysOnes += 10
    daysTwenties = 0
elif daysTwenties == 2 and daysOnes == 0:
    daysTwenties = 1

print ('{} {} {} {} года'.format(listTwenties[daysTwenties], listOnes[daysOnes], listMonths[dateDate.month-1], dateDate.year))

#3: Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result = []

for item in my_list_1:
    cnt = my_list_1.count(item)
    if cnt == 1:
        result.append(item)

print(result)
