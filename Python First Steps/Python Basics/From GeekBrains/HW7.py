import math
fruits = ['Груша', 'Банан', 'Апельсин', 'Инжир', 'Персик', 'Ананас']
my_fruits = ['Яблоко', 'Банан', 'Апельсин', 'Ананас']
numbers = [1, 3, 2, -4, 4, -7, 3, 13, -9, 21, 16, 10, 4, 2, -2, 8, 6, 12]

# Задание №1
result = [fruit for fruit in fruits[:] if fruit in my_fruits]
print(result)
# Задание №2
result = [number for number in numbers[:] if number > 0 and number % 3 == 0 and number % 4 != 0]
print(result)
# Задание №3


def sqr_above_zero(list_of_numbers):
    new_numbers = list_of_numbers.copy()
    for number in new_numbers:
        new = round(math.sqrt(number)) if number > 0 else number
        result.append(new)
    return result


print(sqr_above_zero(numbers))
# Задание №4


def i_fear_13(my_number):
    try:
        raise ValueError if my_number == 13 else None
    except ValueError:
        print('i_fear_13')
    finally:
        my_new_number = my_number ** 2 if my_number != 13 and (my_number > 0) and (my_number <= 100) else None
        return my_new_number


print(i_fear_13(13))
print(i_fear_13(23))
