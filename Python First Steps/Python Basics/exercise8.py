import os, sys
import shutil
import datetime
import logging
from stat import *

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'log.txt')

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
        logging.info( u'был создан файл {}'.format(name) )

def create_folder(name):
    try:
        os.mkdir(name)
        logging.info( u'был создан каталог {}'.format(name) )
    except FileExistsError as fee:
        print('Такой каталог уже существует')

def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = filter(lambda folder: os.path.isdir(folder), result)
        #result = [folder for folder in result if os.path.isdir(folder)]

    return list(result)

def delete_file(curPath):
    is_dir = os.path.isdir(curPath);
    try:
        if is_dir:
            os.rmdir(curPath)
        else:
            os.remove(curPath)
        logging.info( u'{} был удален {}'.format('каталог' if is_dir else 'файл', curPath) )
    except Exception as e:
        strText = u'что-то пошло не так: {}'.format(e)
        print(strText)
        logging.error(strText)

def copy_file(curPath, newPath):
    is_dir = os.path.isdir(curPath);
    if not os.path.exists(curPath):
        strText = u'исходный {} с таким именем не существует'.format('каталог' if is_dir else 'файл')
        print(strText)
        logging.error(strText)
    elif curPath == newPath:
        strText = u'копирование {} самого в себя недопустимо'.format('каталогa' if is_dir else 'файлa')
        print(strText)
        logging.error(strText)
    elif os.path.exists(newPath):
        strText = u'целевой {} с таким именем уже существует'.format('каталог' if is_dir else 'файл')
        print(strText)
        logging.error(strText)
    else:
        try:
            if is_dir:
                shutil.copytree(curPath, newPath)
            else:
                shutil.copy(curPath, newPath)

            logging.info( u'{} был скопирован {} в {}'.format('каталог' if is_dir else 'файл', curPath, newPath) )
        except Exception as e:
            strText = u'что-то пошло не так: {}'.format(e)
            print(strText)
            logging.error(strText)

def deprecated_saveInfo(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def change_directory(newPath):
    if os.path.exists(newPath):
        os.chdir(newPath)
        logging.info( u'был сменен текущий рабочий каталог на {}'.format(newPath) )
    else:
        strText = u'при смене каталога был указан несуществующий путь'
        print(strText)
        logging.error(strText)

def guess_number():
    stepNo = 1
    currentValue = None
    startValue = 1
    endValue = 100
    hasFound = False

    while True:
        is_ready = input('Загадайте число от 1 до 100. По готовности, нажмите y: ')
        if is_ready == 'y':
            break

    print('обозначайте положение предлагаемого числа относительно загаданного символами <, > либо =')

    while not hasFound:
        try:
            currentValue = endValue - (endValue - startValue) // 2
            direction = input('Шаг № {}. Это {} ? '.format(stepNo, currentValue)).strip()

            if direction == '>':
                print('Получается что {} > x'.format(currentValue))
                endValue = currentValue
            elif direction == '<':
                print('Получается что {} < x'.format(currentValue))
                startValue = currentValue
            elif direction == '=':
                print('Победа! x = {}'.format(currentValue))
                hasFound = True 
            stepNo += 1
        except Exception as e:
            strText = u'что-то пошло не так: {}'.format(e)
            print(strText)
            logging.error(strText)

#https://docs.python.org/3.7/library/stat.html#module-stat
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