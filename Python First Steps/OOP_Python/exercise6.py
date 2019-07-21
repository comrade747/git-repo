import exercise5 as ex5

class Chicken (ex5.Bird):
    type = 'chicken'
    __step = 1

    def __init__(self, steps):
        self.distance = steps
        return super().__init__('Hen', 20)

    def __str__(self):
        return 'my name is ' + self.name #super().__str__()


chkn1 = Chicken(50)
print(chkn1)
print(chkn1.type)

chkn2 = ex5.Bird('Eagle', 400)
print(chkn1 < chkn2)

#Это задание продолжает практическое задание прошлого урока. За основу возьмите свой код с классами Word и Sentence. 
#   Выполним с ним следующие преобразования:
#1. Создайте новые классы Noun (существительное) и Verb (глагол).
#2. Настройте наследование новых классов от класса Word.
#3. Добавьте в новые классы свойство grammar («Грамматические характеристики»). 
#   Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное), а для Verb — «гл» (сокращение от глагол). 
#   Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
#4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
#   Подсказка: теперь в нём не нужно хранить части речи.
#   words = []
#   words.append(Noun("собака"))
#   words.append(Verb("ела"))
#   words.append(Noun("колбасу"))
#   words.append(Noun("кот"))
#   По желанию добавьте ещё несколько глаголов и существительных.
#5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
#6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
#7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
#   Подсказка: ранее part был свойством класса Word, а теперь это метод классов Noun и Verb.

import Lib.Sentence as st
import Lib.Word as wd
import Lib.Noun as nn
import Lib.Verb as vb
import Lib.Adverb as dv
import Lib.Adjective as dj

if __name__ == '__main__':

    wd1 = nn.Noun('собака')
    wd2 = vb.Verb('ела')
    wd3 = nn.Noun('колбасу')
    wd4 = dv.Adverb('вечером')
    wd5 = dj.Adjective('голодная')

    words = [wd1, wd2, wd3, wd4, wd5]

    args = (4, 0, 1, 3, 2)
    st1 = st.Sentence(*args)

    stse = st1.show(words)
    print(stse)

    stse = st1.show_parts(words)
    print(stse)