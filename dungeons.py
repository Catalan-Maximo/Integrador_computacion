import random
from enemies import Enemy
from boss import Boss
from constantes import DUNGEON1_ENEMIES, DUNGEON2_ENEMIES, DUNGEON3_ENEMIES

#La clase 'Dungeon' representa una mazmorra con varias batallas
class Dungeon:
    def __init__(self, name):
        self.name = name
        self.battles = self.create_battles()

    def create_battles(self):
        return [
            # Cada batalla tiene entre 3 y 5 enemigos seleccionados aleatoriamente de las listas de enemigos
            [Enemy(random.choice(DUNGEON1_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 1
            [Enemy(random.choice(DUNGEON1_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 2
            [Enemy(random.choice(DUNGEON2_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 3
            [Enemy(random.choice(DUNGEON2_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 4
            [Enemy(random.choice(DUNGEON3_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 5
            [Enemy(random.choice(DUNGEON3_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 6
            [Boss("Orc")]
        ]

    def get_battles(self):
        return self.battles
