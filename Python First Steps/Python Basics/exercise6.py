import pickle
import os
import json

import sys
from stat import *

# https://docs.python.org/3.7/library/stat.html#module-stat
def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)

def processFile():
    f = open('first.txt', 'w')
    f.write('Hello')
    f.write('\n')
    f.write('World')
    f.flush
    f.close

    with open('first.txt', 'r') as f:
        for line in f:
            print(line.replace('\n', ''))

def stringEncoding():
    s = 'Hello World'
    sb = s.encode('utf-8')
    print(sb)
    s = sb.decode('utf-8')
    print(s)

def processFileBytes():
    with open('bytes.txt', 'wb') as f:
        f.write(b'hello World')

    with open('bytes.txt', 'r', encoding='ascii') as f:
        print(f.read())

    with open('bytes.txt', 'wb') as f:
        str = 'Привет мир'
        f.write(str.encode('utf-8'))

    with open('bytes.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def savePerson(person):
    result = None
    fullFileName = os.getcwd() + '\\person.txt'
    try:
        with open(fullFileName, 'wb') as f:
            name = person['name']
            f.write(f'{name}\n'.encode('utf-8'))
            phones=person['phones']

            for phone in phones:
                f.write(f'{phone}\n'.encode('utf-8'))

            f.flush()
        print('Объект записан')
    except:
        print('Объект записать не удалось')
    result = fullFileName
    return result

def readPerson(fileName):
    result = dict()
    try:
        with open(fileName, 'rb') as f:
            lines = f.readlines()

        result.update({'name': lines[0].decode('utf-8').replace('\n', '')})

        phones = []
        for phone in lines[1:]:
            phones.append(phone.decode('utf-8').replace('\n', ''))

        result.update({'phones': phones})
        print('Объект считан')
    except:
        print('Объект прочитать не удалось')

    return result

def savePersonViaPickle(person):
    result = None
    fullFileName = os.getcwd() + '\\person.dat'
    try:
        with open(fullFileName, 'wb') as f:
            pickle.dump(person, f)

        print('Объект записан')
    except:
        print('Объект записать не удалось')
    result = fullFileName
    return result

def readPersonViaPickle(fileName):
    result = dict()
    try:
        with open(fileName, 'rb') as f:
            result = pickle.load(f)

        print('Объект считан')
    except:
        print('Объект прочитать не удалось')

    return result

def savePersonViaJson(person):
    result = None
    fullFileName = os.getcwd() + '\\person.json'
    try:
        with open(fullFileName, 'w') as f:
            json.dump(person, f)

        print('Объект записан')
    except:
        print('Объект записать не удалось')
    result = fullFileName
    return result

def readPersonViaJson(fileName):
    result = dict()
    try:
        with open(fileName, 'r') as f:
            result = json.load(f)

        print('Объект считан')
    except:
        print('Объект прочитать не удалось')

    return dict(result)

import Lib.music_serialize as msr
import Lib.music_deserialize as mds

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016},{'name': 'Шапито','year': 2014}]
}

#1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
#С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. 
#Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

fileInfo_dat = msr.serialiseMusic(msr.saveViaPickle, my_favourite_group)
fileInfo_jsn = msr.serialiseMusic(msr.saveViaJson, my_favourite_group)

#2: Создать модуль music_deserialize.py.
#В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. 
#И получить объект: словарь из предыдущего задания.

groupInfo_dat = mds.deserialiseMusic(mds.loadFromPickle, fileInfo_dat)
print(groupInfo_dat)
groupInfo_jsn = mds.deserialiseMusic(mds.loadFromJson, fileInfo_jsn)
print(groupInfo_jsn)