from enemies import Goblin, Skeleton, Witch, Demon, Orco

class Dungeon:
    def __init__(self, name, level_diff, num_enemies):
        self.name = name
        self.level_diff = level_diff
        self.num_enemies = num_enemies
        self.enemies = []

    def dungeon_1(self):
        self.name = "Cueva de las Brujas"
        self.level_diff = 1
        self.num_enemies = 3

    def dungeon_2(self):
        self.name = "La tumba de tus sueños"
        self.level_diff = 2
        self.num_enemies = 4

    def dungeon_3(self):
        self.name = "Orcos y sus demonios"
        self.level_diff = 3
        self.num_enemies = 5

    def generar_enemigos(self):
        import random
        # Selecciona enemigos según el nivel del dungeon
        posibles_enemigos = [Goblin, Skeleton, Witch, Demon, Orco]  # Lista de posibles clases de enemigos
        for _ in range(self.num_enemies):
            enemigo_clase = random.choice(posibles_enemigos)
            enemigo = enemigo_clase(self.level_diff)  # Pasa el nivel del dungeon al enemigo
            self.enemies.append(enemigo)
    