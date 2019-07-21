#вариант 1 - нет стратегии
import random
a = 1
b = 100
i = random.randint(a, b)
print(i)
user_answer = 0

while user_answer != '=':
    user_answer = input('Введите подсказку: ')
    if user_answer == '>':
        a = i + 1
        i = random.randint(a, b)
        print(i)
    elif user_answer == '<':
        b = i - 1
        i = random.randint(a, b)
        print(i)
    elif user_answer == '=':
        break

print('Угадал')
print ('--------------------')

#вариант 2 - стратегия по среднему арифметическому
a = 1
b = 100
i = int((a + b) / 2)
print(i)
user_answer = 0

while user_answer != '=':
    user_answer = input('Введите подсказку: ')
    if user_answer == '>':
        a = i + 1
        i = int((a + b) / 2)
        print(i)

    elif user_answer == '<':
        b = i - 1
        i = int((a + b) / 2)
        print(i)
    elif user_answer == '=':
        break

print('Угадал')

