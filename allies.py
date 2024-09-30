class Ally:
    def __init__(self, name, health, strength, defense, level):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level

    def attack(self, enemy):
        damage = max(0, self.strength - enemy.defense)
        enemy.health -= damage
        return damage

    def __str__(self):
        return (f"{self.name}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}")


#meter esto en player y que los ally herede de player
