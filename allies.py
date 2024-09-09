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
    
class aliado1(Ally):
    def __init__(self) :
        super().__init__("Aliado de la Aldea", 40, 10, 5, 1)

class aliado2(Ally):
    def __init__(self):
        super().__init__("Aliado de la Dungeon", 50, 15, 8, 1)
 #instancias para aliados