import random
user_response = None
number = random.randint(1, 100)
min_number = 1
max_number = 100
print(number)
user_response = input('Это верное число?')
print(user_response)
while user_response!= '=':
    if user_response == '>':
        min_number = number + 1
        number = random.randint(number,max_number)
        print(number)
        user_response = input('Это верное число?')
    elif user_response == '<':
        max_number = number - 1
        number = random.randint(min_number,number)
        print(number)
        user_response = input('Это верное число?')
else:
    print('Победа')