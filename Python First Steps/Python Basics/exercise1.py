from sys import getdefaultencoding
from sys import argv

arg0 = argv[1]
print (arg0)

print(getdefaultencoding())

name = "Hello world"
print (name)

age = input('Укажите свой возраст: ')
print(type(age))

encodedName = name.encode('ascii', 'ignore')
print (encodedName)

name = input('как Вас зовут? ')
print ('Привет, ', name)

if int(age) < 18:
    print ('Доступ запрещён, ', name)
    print ('Дополнительная строка')
elif int(age) == 18:
    print (name, ', Вам ровно 18 лет :))')
else:
    if int(age) % 5 == 0:
        print ('Поздравляем ', name,' у Вас юбилей')
    print ('Доступ предоставлен, ', name)
    print ('Дополнительная строка')

pythonCreatorName = input('Кто создатель Python?')
while pythonCreatorName != 'Гвидо':
    print ('НЕ верно, ', name, '\nПопробуй снова')
    pythonCreatorName = input('Кто создатель Python?')

print ('Совершенно верно, ', name, '\nМолодец')

#####################################

#1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. 
#Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

increment = 2

while True:
    inputArg = input('Укажите число: ')
    try:
        result = int(inputArg) + increment
        print(inputArg, '+', increment, '=', result)
        break
    except:
        print('Невозможно преобразовать', inputArg, ' в число')


#2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
#После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
#Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
#Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

exponent = 2

while True:
    inputArg = input('Укажите число в диапазоне от 1 до 9 включительно: ')
    try:
        inputArgAsInt = int(inputArg)
        if inputArgAsInt < 10 and inputArgAsInt > 0:
            result = inputArgAsInt ** exponent
            print(inputArgAsInt, 'в степени', exponent, '=', result)
            break
        else:
            print('Указанное число находится вне границ требуемого диапазона')
    except:
        print('Невозможно преобразовать', inputArg, ' в число')

#3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
#Выведите результат согласно которому:
#Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
#Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

name = input('Укажите Ваше имя: ')
surname = input('Укажите Вашу фамилию: ')

intWeight = None
intAge = None
goodWeightRange = None
badWeightRange = None

while True:
    strWeight = input('Укажите Ваш вес: ')
    try:
        intWeight = float(strWeight)
        goodWeightRange = intWeight > 50 and intWeight < 120
        badWeightRange = not goodWeightRange
        break
    except:
        print('Для указания веса доспустимо использовать только цифры c точкой')

while True:
    strAge = input('Укажите Ваш возраст: ')
    try:
        intAge = float(strAge)
        break
    except:
        print('Для указания возраста доспустимо использовать только цифры с точкой')

if intAge <= 30 and goodWeightRange:
    print('Пациент в хорошем состоянии')
elif intAge > 30 and intAge <= 40 and badWeightRange:
    print('Пациенту требуется заняться собой')
elif intAge > 40 and badWeightRange:
    print('Пациенту требуется врачебный осмотр')
else:
    print('not specified')
