# Вариант с подсчетом итераций

right_level = 100
left_level = 1

mid_point=round((right_level-left_level)/2)
count = 1
print("Попытка № {} названа цифра {}".format(count,mid_point))

while True:
    sign = input("Названное число больще, меньше или равно загаданному? ")
    if sign == '=':
        print("Я угадал!!")
        break
    elif sign == '>':
        count +=1
        right_level=mid_point
        mid_point = round((right_level-left_level)/2)+left_level
    else:
        count += 1
        left_level = mid_point
        mid_point = round((right_level-left_level)/2+left_level)
    print("Попытка № {} названа цифра {}".format(count,mid_point))