import Player as pl
import Hamster as hm

hamsters_count = 4
gameon = True

class Game:
    player = None
    map = "****\n****\n****\n****"
    hamsters = []


    def __init__(self):
        newMap = self.map
        self.player = pl.Player()
        newMap = self.add_point(self.player.position, 'x', newMap)
        hmstrs = []
        for i in range(hamsters_count):
            hster = hm.Hamster(newMap, i+1)
            newMap = self.add_point(hster.position, str(hster.id), newMap)
            self.hamsters.append(hster)
        self.map = newMap


    def add_point(self, position, name, map):
        li = map.split('\n')
        y = position[1]
        row = li[y]
        x = position[0]
        row = row[:x] + name + row[x+1:]
        li[y] = row
        return '\n'.join(li)


    def render_map(self):
        result = self.add_point(self.player.position, 'x', self.map)
        for h in self.hamsters:
            if h.health > 0:
                result = self.add_point(h.position, str(h.id), result)
        return result


    def getHamsterAtPosition(self, pos):
        result = None
        hamsters = list(filter(lambda hmstr: hmstr.health > 0 and hmstr.position == pos, self.hamsters))
        if len(hamsters) > 0:
            result = hamsters[0]
        return result
        #for h in self.hamsters:
        #    if h.health > 0 and h.position == pos:
        #        return h
        


    def on_move(self, pos):
        global gameon
        result = True
        hmstr = self.getHamsterAtPosition(pos)
        if hmstr:
            self.player.was_hit(hmstr.id)
            if self.player.health <= 0:
                gameon = False
                print('Player RIP :(')
                return False
            hmstr.on_shot()
            result = hmstr.health == 0

        return result


    def move_player(self, destination):
        """ destination = w,a,s,d """
        newPos = self.player.position.copy()

        if destination == 's':
            if newPos[1] == len(self.map.split('\n')) - 1:
                return False
            newPos[1] += 1

        elif destination == 'a':
            if newPos[0] == 0:
                return False
            newPos[0] -= 1

        elif destination == 'w':
            if newPos[1] == 0:
                return False
            newPos[1] -= 1

        elif destination == 'd':
            if newPos[0] == len(self.map.split('\n')[0]) - 1:
                return False
            newPos[0] += 1

        if self.on_move(newPos):
            newMap = self.add_point(self.player.position, '*', self.map)
            self.map = newMap
            self.player.position = newPos


    def start(self):
        global gameon
        while gameon:
            if len(self.hamsters) > 0:
                hamstersAliveCount = filter(lambda hmstr: hmstr.health > 0, self.hamsters)

                if len(list(hamstersAliveCount)) == 0:
                    print('You won!')
                    gameon = False
                else:
                    print(self.render_map())
                    command = input('Insert command: -> ')
                    if command in ['a', 'w', 's', 'd']:
                        self.move_player(command)
                    elif command == 'e':
                        self.player.wait()
                    elif command == 'q':
                        gameon = False
                    else:
                        print('Incorrect key pressed')
