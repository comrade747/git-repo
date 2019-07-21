import pickle
import json

def deserialiseMusic(func, fileInfo):
    result = None
    try:
        result = func(fileInfo)
        print('Объект считан')
    except:
        print('Объект прочитать не удалось')

    return result


def loadFromPickle(fileInfo):
    result = None
    with open(fileInfo, 'rb') as f:
        result = pickle.load(f)

    return result

def loadFromJson(fileInfo):
    result = None
    with open(fileInfo, 'r', encoding='utf-8') as f:
        result = json.load(f)

    return result