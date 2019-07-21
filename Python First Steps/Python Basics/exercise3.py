import random

randNumber = random.randint(1, 100)
levels = [(1, 10), (2, 5), (3, 3)]
userNumber = None
count = 0
intLevel = None

while True:
    try:
        strLevel = input('Введите уровень сложности от 1 (лёгкий) до 3 (сложный): ')
        intLevel = int(strLevel)
        break
    except:
        print('Невозможно преобразовать {} в число'.format(strLevel))

max_count = levels[intLevel - 1][1]

while userNumber != randNumber:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    try:
        strNumber = input('Введите число: ')
        userNumber = int(strNumber)

        if userNumber > randNumber:
            print('Указанное число больше загаданного')
        elif userNumber < randNumber:
            print('Указанное число меньше загаданного')
    except:
        print('Невозможно преобразовать {} в число'.format(strNumber))
else:
    print('Победа')


print('Загадай число от 1 до 100.')
number_min = 0
number_max = 0
import random
number = random.randint(1, 100)
print('Ты загадал', number)
znak = input('Больше. меньш или равно? ')


if znak == '>':
    number_min = number + 1
    number_max = 100
    #print(number_min, number_max)
elif znak == '<':
    number_max = number - 1
    number_min = 1
    #print(number_min, number_max)
elif znak == '=':
    print('Победа')

number = random.randint(number_min, number_max)
print('Ты загадал', number)
znak = input('Больше. меньш или равно? ')

while True:
    if znak == '>':
        number_min = number + 1
        if number <= 100:
            number = number_max
            #print(number_min, number_max)
            number = random.randint(number_min, number_max)
            print('Ты загадал', number)
            znak = input('Больше. меньш или равно? ')
        else:
            #print(number_min, number_max)
            number = random.randint(number_min, number_max)
            print('Ты загадал', number)
            znak = input('Больше. меньш или равно? ')
    elif znak == '<':
        number_max = number - 1
        if number >= 1:
            number = number_min
            #print(number_min, number_max)
            number = random.randint(number_min, number_max)
            print('Ты загадал', number)
            znak = input('Больше. меньш или равно? ')
        else:
            #print(number_min, number_max)
            number = random.randint(number_min, number_max)
            print('Ты загадал', number)
            znak = input('Больше. меньш или равно? ')
    else:
        print('Победа')
        break


#1. В этой игре человек загадывает число, а компьютер пытается его угадать.
#В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. 
#Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. 
#Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. 
#Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”. 
#Игра продолжается до тех пор пока компьютер не отгадает число.

stepNo = 1
currentValue = None
startValue = 1
endValue = 100
hasFound = False

while True:
    is_ready = input('Загадайте число от 1 до 100. По готовности, нажмите y: ')
    if is_ready == 'y':
        break

print('обозначайте положение предлагаемого числа относительно загаданного символами <, > либо =')

while not hasFound:
    try:
        currentValue = endValue - (endValue - startValue) // 2
        direction = input('Шаг № {}. Это {} ? '.format(stepNo, currentValue)).strip()

        if direction == '>':
            print('Получается что {} > x'.format(currentValue))
            endValue = currentValue
        elif direction == '<':
            print('Получается что {} < x'.format(currentValue))
            startValue = currentValue
        elif direction == '=':
            print('Победа! x = {}'.format(currentValue))
            hasFound = True 
        stepNo += 1
    except:
        print('Что-то пошло не так :(')