def guide():
    print('Используйте символы "<", ">" и "=".')
n=0,100
x=list(range(1,101))
user_input={'>', '<', '='}
print('Загадайте число от', n[0], 'до', n[1])
guide()

answer=""
while answer!="=":
    variant=(min(x)+max(x))//2
    print('Вы загадали '+str(variant)+"?")
    answer=input("Введите символ: ")
    if answer not in user_input:
        guide()
        continue
    else:
        if answer==">":
            x=x[x.index(variant):]
        elif answer=="<":
            x = x[:x.index(variant)]
        else:
            print('Число подобрано')
            break