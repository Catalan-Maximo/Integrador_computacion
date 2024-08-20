class Player:
    def __init__(self, name, char_class, health, strength, defense, level=1):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = 0
        self.experience_to_next_level = 100  # Experiencia necesaria para subir de nivel

    def attack(self, enemy):
        damage = max(0, self.strength - enemy.defense)
        enemy.health -= damage
        return damage

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} ha ganado {amount} puntos de experiencia.")
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)  # Incrementa la experiencia necesaria
        self.health += 12
        self.strength += 2
        self.defense += 2
        print(f"{self.name} ha subido al nivel {self.level}!")
        print(f"Nuevos atributos: Salud {self.health}, Fuerza {self.strength}, Defensa {self.defense}")

    def __str__(self):
        return (f"{self.name} ({self.char_class}) - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}, Experiencia {self.experience}/"
                f"{self.experience_to_next_level}")

# Subclases Guerrero, Mago, Arquero
class Guerrero(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Guerrero: ")
        super().__init__(name, "Guerrero", 100, 15, 10)

class Mago(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Mago: ")
        super().__init__(name, "Mago", 70, 20, 5)

class Arquero(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Arquero: ")
        super().__init__(name, "Arquero", 80, 12, 8)