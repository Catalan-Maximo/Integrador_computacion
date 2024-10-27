import random
from enemies import Enemy
from boss import Boss
from constantes import DUNGEON1_ENEMIES, DUNGEON2_ENEMIES, DUNGEON3_ENEMIES

# Definimos la clase 'Dungeon', que representa una mazmorra con varias batallas
class Dungeon:
    def __init__(self, name):
        self.name = name  # Nombre de la mazmorra
        self.battles = self.create_battles()  # Genera las batallas de la mazmorra

    # Método para crear las batallas de la mazmorra
    def create_battles(self):
        # Devuelve una lista de batallas donde cada batalla tiene un grupo de enemigos
        return [
            # Cada batalla tiene entre 3 y 5 enemigos seleccionados aleatoriamente de las listas de enemigos (DUNGEON1, 2 o 3)
            [Enemy(random.choice(DUNGEON1_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 1
            [Enemy(random.choice(DUNGEON1_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 2
            [Enemy(random.choice(DUNGEON2_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 3
            [Enemy(random.choice(DUNGEON2_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 4
            [Enemy(random.choice(DUNGEON3_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 5
            [Enemy(random.choice(DUNGEON3_ENEMIES)) for _ in range(random.randint(3, 5))],  # Batalla 6
            [Boss("Orc")]  # La batalla final siempre es contra un jefe, en este caso un "Orc"
        ]

    # Método que retorna la lista de batallas creadas
    def get_battles(self):
        return self.battles  # Retorna la lista de batallas generadas
