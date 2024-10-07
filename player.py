import random

class Player:
    def __init__(self, name, char_class, health, strength, defense, level=1):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = 0
        self.experience_to_next_level = 100
        self.inventory = []  # Inventario de ítems

    def attack(self, enemy):
        damage = max(0, self.strength - enemy.defense)
        enemy.health -= damage
        return damage

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} ganó {amount} puntos de experiencia.")
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        self.health += 12
        self.strength += 2
        self.defense += 2
        print(f"¡{self.name} subió al nivel {self.level}!")
        print(f"Nuevos atributos: Salud {self.health}, Fuerza {self.strength}, Defensa {self.defense}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} añadido al inventario de {self.name}.")

    def use_item(self, item):
        if item in self.inventory:
            item.apply(self)
            self.inventory.remove(item)
            print(f"{self.name} usó {item.name}.")
        else:
            print(f"{self.name} no tiene {item.name} en su inventario.")

    def __str__(self):
        return (f"{self.name} ({self.char_class}) - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}, Experiencia {self.experience}/"
                f"{self.experience_to_next_level}")
