import exercise8 as e8
import logging
import sys

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'log.txt')

#1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке разбирали на примере одной функции).
#2. Добавить возможность изменения текущей рабочей директории.
#3. Добавить возможность развлечения в процессе работы с менеджером. 
#Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

command = None

if len(sys.argv) < 2:
    helper()
else:
    command = sys.argv[1]

if command == 'list':
    print(e8.get_list(True))

elif command == 'create_file':
    if len(sys.argv) > 2:
        newInfo = sys.argv[2]

        if len(sys.argv) > 3:
            srtText = sys.argv[3]
            e8.create_file(newInfo, srtText)
        else:
            e8.create_file(newInfo)
    else:
        print('Не указано название нового файла')

elif command == 'create_folder':
    if len(sys.argv) > 2:
        newInfo = sys.argv[2]
        e8.create_folder(newInfo)
    else:
        print('Не указано название нового каталога')

elif command == 'delete':
    if len(sys.argv) > 2:
        newInfo = sys.argv[2]
        e8.delete_file(newInfo)
    else:
        print('Не указано название каталога, подлежащего удалению')

elif command == 'copy':
    if len(sys.argv) > 3:
        currInfo = sys.argv[2]
        newInfo = sys.argv[3]
        e8.copy_file(currInfo, newInfo)
    else:
        print('Не указаны названия коируемого и целевого каталога')

elif command == 'change_dir':
    if len(sys.argv) > 2:
        newInfo = sys.argv[2]
        e8.change_directory(newInfo)
    else:
        print('Не указано название целевого каталога')

elif command == 'guess_number':
    e8.guess_number()

elif command == 'help':
    helper()

def helper():
    print('Данной программой поддерживаются следующие комманды: ')
    print('list - просмотр файлов и директорий')
    print('create_file - создание файла')
    print('create_folder - создание директории')
    print('delete - удаление файла или директории')
    print('change_dir - смена текущего директории')
    print('guess_number - игра "Угадай число"')
