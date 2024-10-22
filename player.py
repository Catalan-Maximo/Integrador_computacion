import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 120  
        self.strength = 12  
        self.defense = 8  
        self.level = 1
        self.experience = 0
        self.items = []

        if player_class == 'Guerrero':
            self.strength += 6
            self.defense += 5
        elif player_class == 'Mago':
            self.strength += 3
            self.health += 30
        elif player_class == 'Arquero':
            self.strength += 4
            self.defense += 3

    def level_up(self):
        self.level += 1
        self.health += random.randint(8, 13)
        self.strength += random.randint(4, 7)
        self.defense += random.randint(2, 5)
        print(f"{self.name} ha subido al nivel {self.level}!")
        print(f"Tus nuevas estadisticas son: Salud: {self.health}, Fuerza: {self.strength}, Defensa: {self.defense}")

    def add_experience(self, amount):
        self.experience += amount
        while self.experience >= 100:
            self.experience -= 100
            self.level_up()

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def has_items(self):
        return len(self.items) > 0

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (Salud: {self.health})"