import random
class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        self.name = enemy_type
        self.health = random.randint(60, 120)
        self.strength = random.randint(11, 20)
        self.defense = random.randint(0, 7)

    def take_damage(self, damage):
        # Calcula el daño real infligido, restando la defensa del enemigo del daño recibido
        actual_damage = max(0, damage - self.defense)  # El daño no puede ser menor a 0
        self.health -= actual_damage
        return actual_damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Salud: {self.health})"
