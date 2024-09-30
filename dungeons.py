from constantes import ally_dungeon, ally_village, goblin_l1, skeleton_l1, skeleton_l2, witch_l1, witch_l2, witch_l3, demon_l1, demon_l2, orco_l1

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
        if self.level_diff == 1:
            posibles_enemigos = [goblin_l1, skeleton_l1,witch_l1]
        elif self.level_diff == 2:
            posibles_enemigos = [skeleton_l2, witch_l2, demon_l1]
        elif self.level_diff == 3:
            posibles_enemigos = [witch_l3, demon_l2, orco_l1] 
        for _ in range(self.num_enemies):
            enemigo_clase = random.choice(posibles_enemigos)
            enemigo = enemigo_clase
            self.enemies.append(enemigo)
    
    def generar_aliados(self):
        import random
        posibles_aliados = []
        if self.level_diff == 1:
            pass
        elif self.level_diff == 2:
            posibles_aliados = [ally_village]
        elif self.level_diff == 3:
            posibles_aliados = [ally_village, ally_dungeon]
            
        if self.level_diff == 3 and self.num_allies > 1:
            num_allies_to_generate = min(self.num_allies, len(posibles_aliados))
            aliados_seleccionados = random.sample(posibles_aliados, num_allies_to_generate)
        else:
            aliados_seleccionados = [random.choice(posibles_aliados) for _ in range(self.num_allies)]
    
        for aliado in aliados_seleccionados:
            self.allies.append(aliado)
#preguntar a profe si meter como constantes los niveles de dificultad
#si y poner los valores de nivel 1 easy mediun y tatata