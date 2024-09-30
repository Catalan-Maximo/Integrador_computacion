from player import Player

class Enemy(Player):
    def __init__(self, name, health, strength, defense, level):
        super().__init__(name, "Enemy", health, strength, defense, level)

    def __str__(self):
        return (f"{self.name} - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}")