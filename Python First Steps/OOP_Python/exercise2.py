import re
import os
import bs4
import requests


def getHtmlFile(path):
    text = None
    try: 
        with open('Additional\{}'.format(path), 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError as fnfe:
        print('В каталоге Additional отсутствует файл {}'.format(path))
    return text

def exercise3():
    resp = requests.get("https://yandex.ru")
    #text = getHtmlFile('yandex_start_page.html')

    strPattern = '<a class="home-link home-link_black_yes(?:[ weather__grade]{0,})" aria-label="([^\"]+)" href='
    pattern = re.compile(strPattern)
    result = pattern.findall(resp.text)
    print(result)

def exercise4():

    text = getHtmlFile('rbc_start_page.html')
    #try: 
    #    with open('Additional\\rbc_start_page.html', 'r', encoding='utf-8') as f:
    #        text = f.read()
    #except FileNotFoundError as fnfe:
    #    print('В каталоге Additional отсутствует файл rbc_start_page.html')

    comments = re.compile('<!--.*?-->', re.DOTALL)
    result = comments.sub('', text)

    scripts = re.compile('<script.*?script>', re.DOTALL)
    result = scripts.sub('', result)

    tags = re.compile('<[^<]*>')
    tags = re.compile('<href.*?href>')
    result = tags.sub('', result)

    result = re.sub('[ ]+', ' ', result) # удаление пробелов
    result = re.sub('(?:\s+){2,}', '\n', result) # удаление лишних переносов строки (и других непечатных символов)

    print(result)

def exercise5():
    text = getHtmlFile('rbc_start_page.html')

    soup = bs4.BeautifulSoup(text, 'html.parser')
    result = soup.prettify()
    result = soup.get_text()
    result = soup.title.string
    result = soup.div['class']

    items = soup.find_all('a')
    for item in items:
        print(item.get('href', ''))

#Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта geekbrains.ru.
#Решите задачу двумя способами:
#a) используя регулярные выражения (библиотеку re),
#b) используя библиотеку BeautifulSoup.
#Примечание: Чтобы увидеть количество учеников, вам надо зайти на главную страницу сайта без залогинивания 
#   (нажмите 3 точки в правом верхнем углу экрана рядом с вашей фотографией и выберите пункт меню «Выход»). 
#   Вы окажетесь на главной странице, где вверху увидите логотип, количество человек (то, что нам нужно) и кнопку «Войти».

import re
from bs4 import BeautifulSoup as bs

def getHtmlFile(path):
    text = None
    try: 
        with open('Additional\{}'.format(path), 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError as fnfe:
        print('В каталоге Additional отсутствует файл {}'.format(path))
    return text

def getCurrentResult(text):
    result = re.findall('([\d+ ]+\W)', text)[0]
    return result.strip()

def exercise1():
    text = getHtmlFile('gb_start_page.html')

    strPattern = '<span class="total-users">(.*)</span>'
    pattern = re.compile(strPattern)
    result = pattern.findall(text)[0]

    return getCurrentResult(result)

def exercise2():
    text = getHtmlFile('gb_start_page.html')
    result = None
    soup = bs(text, 'html.parser')

    spans = soup.find_all('span')
    for span in spans:
        spanClass = span.get('class', '')
        if spanClass[0] == 'total-users':
            result = span.contents[0]
            break

    return getCurrentResult(result)

text = None

print('Задание 1')
text = exercise1()
print(text)

print('\nЗадание 2')
text = exercise2()
print(text)