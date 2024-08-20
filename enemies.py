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
            super().__init__("Goblin", 20, 6, 3, level)
        elif level == 2:
            super().__init__("Goblin", 30, 8, 5, level)
        elif level == 3:
            super().__init__("Goblin", 40, 10, 7, level)
        else:
            raise ValueError("Nivel de Goblin fuera del rango permitido")

class Skeleton(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Skeleton", 30, 18, 5, level)
        elif level == 2:
            super().__init__("Skeleton", 40, 20, 7, level)
        elif level == 3:
            super().__init__("Skeleton", 50, 22, 9, level)
        else:
            raise ValueError("Nivel de Skeleton fuera del rango permitido")

class Witch(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Witch", 40, 20, 7, level)
        elif level == 2:
            super().__init__("Witch", 50, 22, 9, level)
        elif level == 3:
            super().__init__("Witch", 60, 24, 11, level)
        else:
            raise ValueError("Nivel de Witch fuera del rango permitido")

class Demon(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Demon", 50, 22, 11, level)
        elif level == 2:
            super().__init__("Demon", 60, 24, 14, level)
        elif level == 3:
            super().__init__("Demon", 70, 26, 17, level)
        else:
            raise ValueError("Nivel de Demon fuera del rango permitido")

class Orco(Enemy):
    def __init__(self, level):
        if level == 1:
            super().__init__("Orco", 60, 26, 17, level)
        elif level == 2:
            super().__init__("Orco", 70, 28, 20, level)
        elif level == 3:
            super().__init__("Orco", 80, 30, 22, level)
        else:
            raise ValueError("Nivel de Orco fuera del rango permitido")
