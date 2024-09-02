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

# Clases específicas para cada tipo de enemigo
class Goblin(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Goblin", 10, 8, 5, level)
        else:
            raise ValueError("Nivel de Goblin fuera del rango permitido")

class Skeleton(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Skeleton", 15, 10, 7, level)
        elif level == 2:
            super().__init__("Skeleton", 25, 12, 9, level)
        else:
            raise ValueError("Nivel de Skeleton fuera del rango permitido")

class Witch(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Witch", 20, 12, 7, level)
        elif level == 2:
            super().__init__("Witch", 25, 14, 9, level)
        elif level == 3:
            super().__init__("Witch", 30, 16, 11, level)
        else:
            raise ValueError("Nivel de Witch fuera del rango permitido")

class Demon(Enemy):
    def __init__(self, level):
        if level == 2:
            super().__init__("Demon", 35, 18, 12, level)
        elif level == 3:
            super().__init__("Demon", 40, 20, 14, level)
        else:
            raise ValueError("Nivel de Demon fuera del rango permitido")

class Orco(Enemy):
    def __init__(self, level):
        if level == 3:
            super().__init__("Orco", 50, 22, 16, level)
        else:
            raise ValueError("Nivel de Orco fuera del rango permitido")
