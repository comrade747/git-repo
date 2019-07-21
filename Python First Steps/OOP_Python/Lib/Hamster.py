from random import randint

class Hamster:
    _health = 2
    damage = 2
    position = [0, 0]
    id = 0

    @property
    def health(self):
        return self._prop

    @health.setter
    def health(self, value):
        self._health = value


    def __init__(self, map, id):
        #self.health = randint(1, 4)
        self.health = 2
        self.id = id
        self.position = self.get_clear_position(map)
        

    def on_shot(self):
        self.health -= 1
        if self.health == 0:
            print(self.id, '\'ve been killed')

    def get_clear_position(self, map):
        li = map.split('\n')
        while True:
            posNo = randint(0, len(li[0]) - 1)
            rowNo = randint(0, len(li) - 1)
            if li[rowNo][posNo] == '*':
                return [posNo, rowNo]
