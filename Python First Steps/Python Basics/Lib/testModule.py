import exercise6 as e6
import logging

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'log.txt')

# Сообщение отладочное
#logging.debug( u'This is a debug message' )
# Сообщение информационное
#logging.info( u'This is an info message' )
# Сообщение предупреждение
#logging.warning( u'This is a warning' )
# Сообщение ошибки
#logging.error( u'This is an error message' )
# Сообщение критическое
#logging.critical( u'FATAL!!!' )

def get_person(**kwargs): # передаётся словарь
    for k, v in kwargs.items():
        print(k, v)

def greeting(say='Hello', *args): # передаётся кортеж
    print(say, args)

if __name__ == '__main__':
    print('Я выполняюсь всегда')
    print('Когда меня импортруют')
    print('Ну или почти всегда')

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


processFile()
e6.stringEncoding()
e6.processFileBytes()

person = dict(name='Mike', phones=[123, 456])
print(person)
fileName =  e6.savePerson(person)
person1 = e6.readPerson(fileName)
print(person1)

person.update({'age': 34})
fileName =  e6.savePersonViaPickle(person)
person1 = e6.readPersonViaPickle(fileName)
print(person1)

friends = [
    {'name': 'Max', 'age': 23, 'phone': [123, 456]},
    {'name': 'Leo', 'age': 34}
    ]

fileName =  e6.savePersonViaJson(friends[0])
person2 = e6.readPersonViaJson(fileName)
print(person2)
    