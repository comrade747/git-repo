def guide():
    print('Используйте символы "<", ">" и "=".')
n=0,100
x=set([i for i in range(n[0],n[1]+1)])
print (x)
user_input={'>', '<', '='}
print('Загадайте число от', n[0], 'до', n[1])
guide()

answer=""
while answer!="=":
    variant=(min(x)+max(x))//2
    print('Вы загадали '+str(variant)+"?")
    answer=input(" ")
    if answer not in user_input:
        guide()
        continue
    else:
        if answer==">":
            x=set([i for i in x if i>variant])
        elif answer=="<":
            x=set([i for i in x if i<variant])
        else:
            print('Число подобрано')
            break