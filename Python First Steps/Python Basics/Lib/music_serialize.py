import pickle
import json
import os

def getFileInfo(ext):
    result = os.getcwd() + '\\group.' + ext
    return result

def serialiseMusic(func, groupInfo):
    result = None
    try:
        fileInfo = func(groupInfo)
        print('Объект записан')
        result = fileInfo
    except:
        print('Объект записать не удалось')
    
    return result

def saveViaPickle(groupInfo):
    fileInfo = getFileInfo('pickle')
    with open(fileInfo, 'wb') as f:
        pickle.dump(groupInfo, f)
    
    return fileInfo

def saveViaJson1(groupInfo):
    fileInfo = getFileInfo('json')
    with open(fileInfo, 'wb') as f:
        json_string = json.dumps(groupInfo, ensure_ascii=False).encode('utf8')
        f.write(json_string)

    return fileInfo

def saveViaJson(groupInfo):
    fileInfo = getFileInfo('json')
    with open(fileInfo, 'w', encoding='utf-8') as f:
        json.dump(groupInfo, f)

    return fileInfo