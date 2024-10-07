
from constantes import Ally_dungeon, Ally_village, Goblin_l1, Skeleton_l1, Skeleton_l2, Witch_l1, Witch_l2, Witch_l3, Demon_l1, Demon_l2, Orco_l1, Easy, Medium, Hard
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
        posibles_enemigos = []
        if self.level_diff == Easy:
            posibles_enemigos = [Goblin_l1, Skeleton_l1, Witch_l1]
        elif self.level_diff == Medium:
            posibles_enemigos = [Skeleton_l2, Witch_l2, Demon_l1]
        elif self.level_diff == Hard:
            posibles_enemigos = [Witch_l3, Demon_l2, Orco_l1] 
        for _ in range(self.num_enemies):
            enemigo_clase = random.choice(posibles_enemigos)
            enemigo = enemigo_clase
            self.enemies.append(enemigo)
    
    def generar_aliados(self):
        import random
        posibles_aliados = []
        if self.level_diff == Easy:
            pass
        elif self.level_diff == Medium:
            posibles_aliados = [Ally_village]
        elif self.level_diff == Hard:
            posibles_aliados = [Ally_village, Ally_dungeon]
            
        if self.level_diff == Hard and self.num_allies > 1:
            num_allies_to_generate = min(self.num_allies, len(posibles_aliados))
            aliados_seleccionados = random.sample(posibles_aliados, num_allies_to_generate)
        else:
            aliados_seleccionados = [random.choice(posibles_aliados) for _ in range(self.num_allies)]
    
        for aliado in aliados_seleccionados:
            self.allies.append(aliado)
