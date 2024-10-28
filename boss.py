import random
from enemies import Enemy

class Boss(Enemy):
    def __init__(self, enemy_type):
        super().__init__(enemy_type)
        self.name = "Thrall"
        self.health = random.randint(150, 250)
        self.strength = random.randint(20, 30)
        self.defense = random.randint(9, 14)
