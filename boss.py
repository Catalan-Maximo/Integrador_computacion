import random

class Boss:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        self.health = random.randint(150, 200)
        self.strength = random.randint(20, 30)
        self.defense = random.randint(9, 14)

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage  # Retorna el daño real infligido

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.enemy_type} (Salud: {self.health})"