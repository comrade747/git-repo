from random import choice

class Player:
    health = 10
    max_health = 10
    damage = 10
    position = [0, 0]


    def was_hit(self, damage):
        self.health -= choice(range(damage))
        print('Player\'s health:', self.health)


    def wait(self):
        if self.health < self.max_health:
            self.health += 1
        
        print('Player\'s health:', self.health)