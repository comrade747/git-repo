import sys
import os

#1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
#В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
#Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

def getNewDirectoryPath(i):
    dirName = 'dir_{}'.format(i)
    return os.path.join(os.getcwd(), dirName)

def makeDirectories():
    for i in range(1, 10):
        newPath = getNewDirectoryPath(i)
        if not os.path.exists(getNewDirectoryPath(i)):
            try:
                os.mkdir(newPath)
            except:
                print('Не удаётся создать папку {}'.format(dirName))

def dropDirectories():
    for i in range(1, 10):
        newPath = getNewDirectoryPath(i)
        if os.path.exists(getNewDirectoryPath(i)):
            try:
                os.rmdir(newPath)
            except:
                print('Не удаётся удалить папку {}'.format(dirName))

def processDirectories(func):
    for i in range(1, 10):
        newPath = getNewDirectoryPath(i)
        func(newPath)

def dropDirectory(path):
    if os.path.exists(path):
        try:
            os.rmdir(path)
        except:
            print('Не удаётся удалить папку {}'.format(path))

def makeDirectory(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            print('Не удаётся создать папку {}'.format(path))

#2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
#Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

from random import choice

def chooseElement(elems):
    result = None
    if len(elems) > 0:
        result = choice(elems)

    return result

