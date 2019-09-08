import re
import requests
import bs4
import os
import logging
import operator
import datetime

#Реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
#Возможен следующий алгоритм решения задачи:
#1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup. 
#   Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
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

import re
import os
import bs4
import requests

import zipfile
import os

import exercise7
import ExcelSample


def getHtmlFile(path):
    text = None
    try: 
        with open('Additional\{}'.format(path), 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError as fnfe:
        print('В каталоге Additional отсутствует файл {}'.format(path))
    return text


def exercise5():
    text = getHtmlFile('rbc_start_page.html')
    soup = bs4.BeautifulSoup(text, 'html.parser')
    result = soup.prettify()
    result = soup.get_text()
    result = soup.title.string
    result = soup.div['class']


def exercise1():
    d = 'c:\\Users\\andre\\source\\repos\\Lesson1\\OOP_Python\\Lib'

    os.chdir(os.path.dirname(d))
    with zipfile.ZipFile(d + '.zip', "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for root, _, filenames in os.walk(os.path.basename(d)):
            for name in filenames:
                name = os.path.join(root, name)
                name = os.path.normpath(name)
                zf.write(name, name)

