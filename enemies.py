import random

# Definimos la clase 'Enemy' que representa a un enemigo
class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type  # Tipo de enemigo (por ejemplo, Goblin, Esqueleto, etc.)
        self.name = enemy_type  # El nombre del enemigo será el mismo que su tipo
        self.health = random.randint(60, 120)  # Salud inicial del enemigo, un valor aleatorio entre 60 y 120
        self.strength = random.randint(11, 20)  # Fuerza del enemigo, un valor aleatorio entre 11 y 20
        self.defense = random.randint(0, 7)  # Defensa del enemigo, un valor aleatorio entre 0 y 7

    # Método para calcular el daño recibido por el enemigo
    def take_damage(self, damage):
        # Calcula el daño real infligido, restando la defensa del enemigo del daño recibido
        actual_damage = max(0, damage - self.defense)  # El daño no puede ser menor a 0
        self.health -= actual_damage  # Resta el daño a la salud del enemigo
        return actual_damage  # Retorna el daño real que recibió

    # Método que verifica si el enemigo sigue vivo
    def is_alive(self):
        return self.health > 0  # El enemigo está vivo si su salud es mayor a 0

    # Método que devuelve una representación en cadena del enemigo
    def __str__(self):
        # Devuelve el nombre del enemigo y su salud actual
        return f"{self.name} (Salud: {self.health})"
