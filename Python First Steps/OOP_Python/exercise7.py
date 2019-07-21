class Foo(object):

    def __init__(self):
        self._prop = None

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self, value):
        self._prop = value

    @property
    def bar(self):
        return 5

    @bar.setter
    def bar(self, a):
        print(a)


class FooBar(Foo):

    @property
    def bar(self):
        # return the same value
        # as in the base class
        return Foo.bar.fget(self)

    @bar.setter
    def bar(self, value):
        # perform the same action
        # as in the base class
        Foo.bar.fset(self, value)

    @property
    def prop(self):
        value = super(FooBar, self).prop
        # do something with / modify value here
        return value

    @prop.setter
    def prop(self, value):
        # do something with / modify value here
        super(FooBar, self.__class__).prop.fset(self, value)

fb = FooBar()

fb.prop = 34
print(fb.prop)

print(fb.bar)
fb.bar = 7
print(fb.bar)

import Game as gm

#Созданная нами игра получилась цельной и завершенной, однако, как и в любом приложении, в ней есть баги. 
#Крупных бага, возникших в ходе разработки, три. Найдите и исправьте их.
#Подсказки:
#1. Попробуйте выйти за границы поля.
#2. У вас получается рождение под хомяком?
#3. Отличная концовка, не так ли?
#Опишите, что и где вы исправили в виде комментария в конце программы. Если вы нашли более трёх ошибок, исправьте и опишите все. Вы молодцы!

if __name__ == '__main__':

    gme = gm.Game()
    gme.start()

# скорректировал логику работы с картой
# добавил невозможность рождения под хомяком 
# изменил логику перемещения игрока, переписал логику функции getHamsterAtPosition