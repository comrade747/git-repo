import re
import os
from urllib.parse import urlparse

text = """
Привет! отправь, пожалуйста, письмо нашим коллегам: vladamir@v.ru, vladimir2@v.ru; про Оксану и Ольгу не забудь: oksana@v.ru, olga@v.ru
отошли копию партнерам adidas@abc.ru и nike@cba.com

спасибо! @@твой босс
"""

items = text.split()
#emails = filter(lambda item: '@' in item, items)
emails = [item for item in items if '@' in item]
print(list(emails))

li = re.findall('vlad.mir', text)
print(li)

li = re.findall('\w+@\w+\.\w+', text)
print(li)

pattern_string = "(\W|^)[\w.\-]{0,25}@(yahoo|hotmail|gmail)\.com(\W|$)"
pattern = re.compile(pattern_string)
emails1 = pattern.findall(text)
print(emails1)

text = """В деле задержанных накануне сотрудников ФСБ фигурирует ст. 210.55% УК (организация преступного сообщества), рассказал РБК источник в ФСБ,, информацию подтвердил собеседник, близкий к службе....
По версии следствия, задержанных сотрудников ФСБ подозревают в создании организованного преступного сообщества, грабежей (ст. 162,8% УК), мошенничестве (ст. 1% УК) и превышение должностных полномочий (ст. 286 УК).
'Сотрудники УСБ разрабатывали группу силовиков в течение года', — отметил источник в службе. Задержанных проверяют на причастность к совершению от пяти до 12,009% эпизодов...
"""

li1 = re.findall('\d+.?\d*', text)

li2 = re.findall('[0123456789,]+', text)

li3 = re.findall('[0-9,]+', text)

li4 = re.findall('[а-я,]+', text)

li5 = re.findall('\d+[,\.]?\d*%', text)

li6 = re.findall('(\d+,?\d*|\d+\.?\d*)%', text)

li7 = re.findall('(\w+)[,\.]{1,3}', text)

li8 = re.findall('(\w+)[,\.]{2,3}[^\.,]', text)

text = """
Франция одержала победу над хорватами в финале чемпионата мира по футболу 2018 года и стала победителем турнира. Об этом сообщает корреспондент «Ленты.ру».
Матч состоялся на стадионе «Лужники» и завершился со счетом 4:2. Опять французы вышли вперед на 18-й минуте благодаря автоголу нападающего соперника Марио Манджукича. На 28-й минуте полузащитник хорватов Иван Перишич сравнял счет. На 38-й минуте в ворота Хорватии был назначен пенальти, который реализовал форвард Антуан Гризманн.
Во втором тайме преимущество сборной Франции увеличили хавбек Поль Погба (59-я минута) и нападающий Килиан Мбаппе (65-я минута). На 69-й минуте Манджукич сократил отставание сборной Хорватии.
Сборная Франции, считавшаяся фаворитов матча с хорватами, во второй раз выиграла мундиаль. До этого команда побеждала на домашнем чемпионате мира 1998 года.
"""

text1 = re.sub('Французы', 'Россияне', text)

pattern_string = "Франц"
pattern = re.compile(pattern_string)
text2 = re.sub(pattern, 'Росс', text)
print(text2)

text3 = re.sub('\d+', 'число', text)

pattern_string = '\d{1,2}\-[ия]'

text4 = re.sub(pattern_string, 'n', text)

pattern = re.compile(pattern_string)
text5 = pattern.findall(text)



#1. Получите текст из файла.
#Примечание: Можете взять свой текст или воспользоваться готовым из материалов к уроку. 
#Вспомните операции с чтением файлов и не забудьте сохранить текст в переменную по аналогии с видеоуроками.

text = None
try: 
    with open('exercise1_1.txt', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError as fnfe:
    print('В текущем каталоге отсутствует файл exercise1_1.txt')
print('Задание №1')
print(text)

#2. Разбейте полученные текст на предложения.
#Примечание: Напоминаем, что в русском языке предложения заканчиваются на ., ! или ?.

print('\nЗадание №2')
strPattern = '[!\.\?]'
result = re.split(strPattern, text)
print(result)

#3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
#Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”, 2)].

print('\nЗадание №3')
strPattern = '\w{4,}'
result = re.findall(strPattern, text)
print(result)

items = re.findall('\w+', text)
pairs = []
result = None
for item in items:
    cnt = len(re.findall(item, text))
    pairs.append((item, cnt))
result = list(set(pairs))

result.sort(key=lambda pair: pair[1], reverse=True)
print(result[:10])

#4. Отберите все ссылки.
#Примечание: Для поиска воспользуйтесь методом compile, в который вы вставите свой шаблон для поиска ссылок в тексте.

text = None
try: 
    with open('exercise1_2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError as fnfe:
    print('В текущем каталоге отсутствует файл exercise1_2.txt')

print('\nЗадание №4')
pattern = re.compile('http[s]?://\S+')
result = pattern.findall(text)
print(result)

#5. Ссылки на страницы какого домена встречаются чаще всего?
#Напоминаем, что доменное имя — часть ссылки до первого символа «слеш». Например в ссылке вида travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru.
#Подсчет частоты сделайте по аналогии с заданием 3, но верните только одну самую частую ссылку.

print('\nЗадание №5')
#(?<=\.)([^.]+)(?:\.(?:com|ua|ru|us|[^.]+(?:$|\n))) не получается выделить 
pattern = re.compile('http[s]?://\S+')
urls = pattern.findall(text)

i = 0
urlObj = None
siteList = []
for url in urls:
    urlObj = urlparse(url) # использована специальная функция из пакета urllib.parse для удобного разбора url-адресов

    pair = [item for item in siteList if item[0] == urlObj.hostname]
    if not pair:
        siteList.append((urlObj.hostname, 1))
    else:
        oldPair = pair[0]
        newPair = (pair[0][0], pair[0][1] + 1)
        siteList.remove(oldPair)
        siteList.append(newPair)
    
siteList.sort(key=lambda pair: pair[1], reverse=True)
print(siteList[:1])

# или так

i = 0
urlObj = None
siteList = {}
for url in urls:
    urlObj = urlparse(url) # использована специальная функция из пакета urllib.parse для удобного разбора url-адресов
    i += 1
    if urlObj.hostname in siteList:
        siteList[urlObj.hostname] += 1
    else:
        siteList[urlObj.hostname] = 1

sites = list(siteList.items())
sites.sort(key=lambda pair: pair[1], reverse=True)
print(sites[:1])

#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

print('\nЗадание №6')
text = pattern.sub('«Ссылка отобразится после регистрации»', text)
print(text)



