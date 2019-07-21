import re
import requests
import bs4
import os
import logging
import operator
import datetime


def getLink(topic):
    link = "https://ru.wikipedia.org/wiki/{}"
    return link.format(topic.capitalize())

def getTopicPage(topic):
    link = getLink(topic)
    htmlContent = requests.get(link).text

    soup = bs4.BeautifulSoup(htmlContent, 'html.parser')
    textContent = soup.get_text()

    words = re.findall('[а-яА-ЯёЁ\-\э]{3,}', htmlContent)

    rate = {}
    for word in words:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1

    rate_list = list(rate.items())
    rate_list.sort(key=lambda item: -item[1])
    return rate_list

#Реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
#Возможен следующий алгоритм решения задачи:
#1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup. Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
#2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
#3. Сложить все в один список.

def getLink(topic):
    link = "https://ru.wikipedia.org/wiki/{}"
    return link.format(topic.capitalize())

def getNeighbourPaiges(topic):
    result = None
    link = getLink(topic)
    htmlContent = requests.get(link).text
    soup = bs4.BeautifulSoup(htmlContent, 'html.parser')

    pattern = re.compile("^http[s]?://[\w+.]+[\w+]\/wiki\/*")
    links = soup.findAll('a', attrs={'href': pattern})
    wordsCollection = {}
    for link in links:
        url = link.get('href')
        linkContent = requests.get(url).text
        wordsList = getCommonWordsByPage(linkContent)
        wordsCollection[url] = wordsList
    
    return wordsCollection

def getCommonWordsByPage(htmlContent):
    soup = bs4.BeautifulSoup(htmlContent, 'html.parser')
    words = re.findall('[\w\-]{3,}', soup.getText())

    rate = {}
    for word in words:
        capWord = word.capitalize()
        if capWord in rate:
            rate[capWord] += 1
        else:
            rate[capWord] = 1

    rate_list = list(rate.items())
    rate_list.sort(key=lambda item: item[1], reverse=True)
    return rate_list[:10] # буду возвращать первые 10 и пусть меня за это не ругают ((

words = getNeighbourPaiges('дерево')
print(words)

#Реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
#Возможен следующий алгоритм решения задачи:
#1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup. Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
#2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
#3. Сложить все в один список.

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'log.txt')

def getLink(topic):
    link = "https://ru.wikipedia.org/wiki/{}"
    return link.format(topic.capitalize())

def getNeighbourPaiges(topic):
    result = None
    link = getLink(topic)
    htmlContent = requests.get(link).text
    soup = bs4.BeautifulSoup(htmlContent, 'html.parser')

    pattern = re.compile("^https://ru.\w+.\w+\/wiki\/*") #"^http[s]?://[\w+.]+[\w+]\/wiki\/*"
    links = soup.findAll('a', attrs={'href': pattern})
    wordsCollection = {}
    for link in links:
        url = link.get('href')
        linkContent = requests.get(url).text
        wordsList = getCommonWordsByPage(linkContent)
        wordsCollection[url] = wordsList
    
    return wordsCollection

def getCommonWordsByPage(htmlContent):
    soup = bs4.BeautifulSoup(htmlContent, 'html.parser')
    words = re.findall('[\w\-]{3,}', soup.getText())

    rate = {}
    for word in words:
        capWord = word.capitalize()
        if capWord in rate:
            rate[capWord] += 1
        else:
            rate[capWord] = 1

    rate_list = sorted(rate.items(), key=operator.itemgetter(1), reverse=True)
    #rate_list = list(rate.items())
    #rate_list.sort(key=lambda item: item[1], reverse=True)
    return rate_list[:10] # буду возвращать первые 10 и пусть меня за это не ругают ((

logging.info(u'Запуск программы')
words = getNeighbourPaiges('дерево')
fileName = 'words.txt'
with open(fileName, 'w', encoding='utf-8') as f:
    for strg in words.items():
        f.write(str(strg) + '\n')
    
logging.info(u'результат записан в файл {}'.format(fileName))