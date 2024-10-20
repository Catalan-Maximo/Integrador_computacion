# player.py

import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.strength = 10
        self.defense = 5
        self.level = 1
        self.experience = 0
        self.items = []

        if player_class == 'Guerrero':
            self.strength += 5
            self.defense += 5
        elif player_class == 'Mago':
            self.strength += 2
            self.health += 20
        elif player_class == 'Arquero':
            self.strength += 3
            self.defense += 2

    def level_up(self):
        self.level += 1
        self.health += random.randint(5, 10)
        self.strength += random.randint(2, 5)
        self.defense += random.randint(1, 3)

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def has_items(self):
        return len(self.items) > 0

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (Salud: {self.health})"