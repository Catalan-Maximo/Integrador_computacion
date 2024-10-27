import random
from enemies import Enemy

# Definimos una nueva clase llamada 'Boss', que hereda de la clase 'Enemy'
class Boss(Enemy):
    
    # Método constructor de la clase 'Boss'
    # Recibe el parámetro 'enemy_type', que describe el tipo de enemigo (por ejemplo, un jefe de tipo demonio, orco, etc.)
    def __init__(self, enemy_type):
        # Llamamos al constructor de la clase padre 'Enemy' usando 'super()' para inicializar el tipo de enemigo
        super().__init__(enemy_type)
        
        # Asignamos un nombre específico al jefe, en este caso, siempre será "Thrall"
        self.name = "Thrall"
        
        # Asignamos a 'health' (salud) un valor aleatorio entre 150 y 250
        self.health = random.randint(150, 250)
        
        # Asignamos a 'strength' (fuerza) un valor aleatorio entre 20 y 30
        self.strength = random.randint(20, 30)
        
        # Asignamos a 'defense' (defensa) un valor aleatorio entre 9 y 14
        self.defense = random.randint(9, 14)
