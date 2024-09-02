from enemies import Goblin, Skeleton, Witch, Demon, Orco
from allies import aliado1, aliado2

class Dungeon:
    def __init__(self, name, level_diff, num_enemies, num_allies):
        self.name = name
        self.level_diff = level_diff
        self.num_enemies = num_enemies
        self.num_allies = num_allies
        self.enemies = []
        self.allies = []

    def generar_enemigos(self):
        import random
        # Selecciona enemigos según el nivel del dungeon
        posibles_enemigos = [] # Lista de posibles clases de enemigos
        if self.level_diff == 1:
            posibles_enemigos = [Goblin, Skeleton, Witch]
        elif self.level_diff == 2:
            posibles_enemigos = [Skeleton, Witch, Demon]
        elif self.level_diff == 3:
            posibles_enemigos = [Witch, Demon, Orco] 
        for _ in range(self.num_enemies):
            enemigo_clase = random.choice(posibles_enemigos)
            enemigo = enemigo_clase(self.level_diff)  # Pasa el nivel del dungeon al enemigo
            self.enemies.append(enemigo)
    
    def generar_aliados(self):
        import random
        # Selecciona aliados según el nivel del dungeon
        posibles_aliados = [] # Lista de posibles clases de aliados
        if self.level_diff == 1:
            pass
        elif self.level_diff == 2:
            posibles_aliados = [aliado1]
        elif self.level_diff == 3:
            posibles_aliados = [aliado1, aliado2]
            
        if self.level_diff == 3 and self.num_allies > 1:
        # Asegurarse de no seleccionar más aliados de los disponibles
            num_allies_to_generate = min(self.num_allies, len(posibles_aliados))
            aliados_seleccionados = random.sample(posibles_aliados, num_allies_to_generate)
        else:
            aliados_seleccionados = [random.choice(posibles_aliados) for _ in range(self.num_allies)]
    
        for aliado_clase in aliados_seleccionados:
            aliado = aliado_clase()  # No pasar el nivel del dungeon al aliado
            self.allies.append(aliado)