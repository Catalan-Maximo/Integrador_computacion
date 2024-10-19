import random
from enemies import Enemy
from constantes import DUNGEONS, ENEMY_TYPES

class Dungeon:
    def __init__(self, name):
        self.name = name
        self.battles = self.create_battles()

    def create_battles(self):
        # Definimos las batallas de manera lineal
        return [
            [Enemy(random.choice(ENEMY_TYPES)) for _ in range(random.randint(3, 5))],  # Batalla 1
            [Enemy(random.choice(ENEMY_TYPES)) for _ in range(random.randint(3, 5))],  # Batalla 2
            [Enemy(random.choice(ENEMY_TYPES)) for _ in range(random.randint(3, 5))],  # Batalla 3
            [Enemy(random.choice(ENEMY_TYPES)) for _ in range(random.randint(3, 5))],  # Batalla 4
            [Enemy(random.choice(ENEMY_TYPES)) for _ in range(random.randint(3, 5))]   # Batalla 5
        ]

    def get_battles(self):
        return self.battles