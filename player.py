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
        self.xp_objetive = 100
        self.items = []

        # Ajustes de estadísticas según la clase elegida
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
        self.health = self.health * 1.15
        self.strength = self.strength * 1.15
        self.defense = self.defense * 1.15
        print(f"{self.name} ha subido al nivel {self.level}!")
        print(f"Tus nuevas estadisticas son: Salud: {self.health}, Fuerza: {self.strength}, Defensa: {self.defense}")

    def add_experience(self, amount):
        self.experience += amount  # Aumenta la experiencia acumulada
        while self.experience >= self.xp_objetive:
            self.experience -= self.xp_objetive
            self.level_up()
            self.xp_objetive = (self.xp_objetive * 1.2)

    def take_damage(self, damage):
        # Calcula el daño real restando la defensa del daño recibido
        self.health -= max(0, damage - self.defense)  # Asegura que la salud no sea negativa

    def has_items(self):
        return len(self.items) > 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Salud: {self.health})"
