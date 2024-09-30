class Enemy:
    def __init__(self, name, health, strength, defense, level):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level

    def attack(self, player):
        damage = max(0, self.strength - player.defense)
        player.health -= damage
        return damage

    def __str__(self):
        return (f"{self.name} - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}")


#hacer lo mismo que en aliados, pasarlo a player