class A:
    a = None 
    b = None

a = A()
a.a = 10
a.b = 20

b = A()

#print(b.a + b.b)

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

