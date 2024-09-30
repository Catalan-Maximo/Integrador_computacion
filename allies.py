from player import Player

class Ally(Player):
    def __init__(self, name, health, strength, defense, level):
        super().__init__(name, "Ally", health, strength, defense, level)

    def __str__(self):
        return (f"{self.name} (Aliado) - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}")
    