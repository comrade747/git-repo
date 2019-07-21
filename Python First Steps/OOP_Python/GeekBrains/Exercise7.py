from time import sleep
from random import randint, choice
#from humster import Hamster
#from player import Player


class Hamster:
    position = [0, 0]
    health = 3
    damage = 3
    state = True


    def __init__(self, hId, map):
        self.id = hId + 1
        self.health = randint(1, 20)
        self.position = self.clear_position(map)
        self.state = True
        self.damage = randint(1, 10)

    def on_shot(self, damage=1):
        self.health -= damage
        return self.health <= 0


    def clear_position(self, map):
        max_X = len(map.split('\n')[0])
        max_Y = len(map.split('\n'))
        while True:
            coord = [randint(0, max_X - 1), randint(0, max_Y - 1)]
            if map.split('\n')[coord[1]][coord[0]] == '*':
                return coord

class Player:
    name = ''
    health = 100
    default_damage = 10
    position = [0, 0]
    posion = randint(1, 3)

    def hit_by_hamster(self, damage):
        self.health -= damage

    def recovery(self):
        for i in range(3):
            print('������� ��������������' + '.' * (i + 1))
            sleep(1)
        self.health += randint(1, 2)
        self.posion -= 1
        print(f'������� ������ ������ �������� ����� {self.health}')
        print(f'������� {self.posion} ������� ��������������.')


hamstersCount = randint(1, 6)

class Game:
    mapDefault = '****\n****\n****\n****'
    humsterAlive = True

    def __init__(self):
        self.player = Player()
        self.humster = []
        for i in range(hamstersCount):
            self.humster.append(Hamster(i, self.full_map()))

    def hamster_alive(self):
        for i in range(hamstersCount):
            if self.humster[i].state == True:
                return True
            else:
                self.humsterAlive = False

    def player_alive(self):
        return False if self.player.health <= 0 else True

    def add_point(self, position, name, currentMap):
        currentString = currentMap.split('\n')
        currentRow = currentString[position[1]]
        currentRow = currentRow[:position[0]] + name + currentRow[position[0] + 1:]

        currentString[position[1]] = currentRow
        currentMap = '\n'.join(currentString)
        return currentMap

    def render_map(self):
        map = self.mapDefault
        map = self.add_point(self.player.position, 'x', map)
        for h in self.humster:
            if h.health > 0:
                map = self.add_point(h.position, str(h.id), map)
        print(map)

    def move_player(self, direction):
        if direction == 'w':
            if self.player.position[1] == 0:
                print('�� ����� �� ������� ����! ����������, �������� ������ �����������.')
                return False
            self.player.position[1] -= 1
        elif direction == 's':
            if self.player.position[1] == len(self.mapDefault.split('\n')) - 1:
                print('�� ����� �� ������� ����! ����������, �������� ������ �����������.')
                return False
            self.player.position[1] += 1
        elif direction == 'a':
            if self.player.position[0] == 0:
                print('�� ����� �� ������� ����! ����������, �������� ������ �����������.')
                return False
            self.player.position[0] -= 1
        elif direction == 'd':
            if self.player.position[0] == len(self.mapDefault.split('\n')[0]) - 1:
                print('�� ����� �� ������� ����! ����������, �������� ������ �����������.')
                return False
            self.player.position[0] += 1
        self.on_move(direction)

    def full_map(self):
        map = self.mapDefault
        map = self.add_point(self.player.position, 'x', map)
        for h in self.humster:
            map = self.add_point(h.position, str(h.id), map)
        return map

    def hamster_on_position(self, coord):
        map = self.mapDefault
        for h in self.humster:
            map = self.add_point(h.position, str(h.id), map)
        return map.split('\n')[coord[1]][coord[0]]

    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
    def on_move(self, direction):
        hamsterMeet = self.hamster_on_position(self.player.position)
        if not hamsterMeet == '*':
            print(f'���� ������ {int(hamsterMeet)} ����� {self.humster[int(hamsterMeet) - 1].damage}.')
            self.player.hit_by_hamster(self.humster[int(hamsterMeet) - 1].damage)
            if self.player_alive():
                print(f'������� ������ ������ �������� ����� {self.player.health}')
                killed = self.humster[int(hamsterMeet) - 1].on_shot(damage=self.player.default_damage)
                if not killed:
                    print(f'����� {int(hamsterMeet)} �����!')
                    print(f'������� �������� ������ {self.humster[int(hamsterMeet) - 1].id} - {self.humster[int(hamsterMeet) - 1].health}')
                    self.move_player(self.directions[direction])
                else:
                    #��������� ��� � �������������� ��������� � �������� ������
                    print(f'����� {int(hamsterMeet)} ���������!')
                    self.humster[int(hamsterMeet) - 1].state = False
                    self.humster[int(hamsterMeet) - 1].position[0] = 100




    def game_start(self):
        self.player.name = input('������� ��� ������: ')
        print(f'����� ���������� {self.player.name} � ��� ������� �������!')
        print('���� ���� - ���������� ������� �������. �� �������, ��� ���� �� ����� ������,�� � ����� ���� ���!!!')
        print('\t����� ����')
        self.render_map()
        print(f'������� ������ ������ �������� ����� {self.player.health}')
        print(f'������� {self.player.posion} ������� ��������������.')
        print("��� �������� ������� ���� �� ������ � Enter:\n 1) 'w' - �����; \n 2) 's' - ����;\n 3) 'a' - �����; \n 4) 'd' - ������; \n 5) 'i' - ������������ ��������; \n 6) 'e' - �����.\n")

        while self.humsterAlive:
            if self.player_alive():
                command = input("������� �������: ")
                if command == 'e':
                    print('����� ����!')
                    break
                elif command == 'i':
                    self.player.recovery()
                    print('\t����� ����')
                    self.render_map()
                elif command in ['a', 's', 'd', 'w']:
                    self.move_player(command)
                    print('\t����� ����')
                    self.render_map()
                else:
                    print('�� ����� �������� �������\n')
                    print("��� �������� ������� ���� �� ������ � Enter:\n 1) 'w' - �����; \n 2) 's' - ����;\n 3) 'a' - �����; \n 4) 'd' - ������; \n 5) 'i' - ������������ ��������; \n 6) 'e' - �����.\n")
            else:
                print('�� ���� ������� ����� �� ��������! ����� ����.')
                break
            self.humsterAlive = self.hamster_alive()
        else:
            print('�����������! �� ��������!')


newGame = Game()
newGame.game_start()

#��������� ��� � �������������� ��������� � �������� ������
#��������� ��� ������ �� ������� ����
