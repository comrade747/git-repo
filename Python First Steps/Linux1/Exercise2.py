import os
import sys
import shutil
import first, second, common

def getFileName(name):
    #result = "/{}.py".format(name) # for Linux
    result = "\\{}.py".format(name) # for Windows
    return result

def moveFile(rootPath, fName):
    newPath = os.path.join(rootPath, fName)
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    
    fileName = getFileName(fName)
    if os.path.exists(rootPath + fileName) and not os.path.exists(newPath + fileName):
        shutil.move(rootPath + fileName, newPath + fileName)

    return newPath

if __name__ == '__main__':

    root_path = os.getcwd()
    fPath = moveFile(root_path, 'first')
    sPath = moveFile(root_path, 'second')

    fileName = getFileName('second')
    if not os.path.exists(fPath + fileName):
        shutil.move(sPath + fileName, fPath + fileName)

    if os.path.exists(sPath):
        os.rmdir(sPath)

    newPath = os.path.join(root_path, 'first_second')
    if os.path.exists(fPath) and not os.path.exists(newPath):
        os.rename(fPath, newPath)

    if os.path.exists(newPath):
        shutil.rmtree(newPath, ignore_errors=True)

    print(common.getYandexWeather())
