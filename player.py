import random

class Player:
    def __init__(self, name, player_class):
        self.name = name  # Inicializa el nombre del jugador
        self.player_class = player_class  # Inicializa la clase del jugador (Guerrero, Mago o Arquero)
        self.health = 120  # Salud inicial del jugador
        self.strength = 12  # Fuerza inicial del jugador
        self.defense = 8  # Defensa inicial del jugador
        self.level = 1  # Nivel inicial del jugador
        self.experience = 0  # Experiencia acumulada inicial
        self.xp_objetive = 100  # Objetivo de experiencia para subir de nivel
        self.items = []  # Lista para almacenar los ítems del jugador

        # Ajustes de estadísticas según la clase elegida
        if player_class == 'Guerrero':
            self.strength += 6  # Aumenta la fuerza del Guerrero
            self.defense += 5   # Aumenta la defensa del Guerrero
        elif player_class == 'Mago':
            self.strength += 3  # Aumenta la fuerza del Mago
            self.health += 30    # Aumenta la salud del Mago
        elif player_class == 'Arquero':
            self.strength += 4  # Aumenta la fuerza del Arquero
            self.defense += 3   # Aumenta la defensa del Arquero

    def level_up(self):
        self.level += 1  # Aumenta el nivel del jugador
        self.health = self.health * 1.15  # Aumenta la salud en un 15%
        self.strength = self.strength * 1.15  # Aumenta la fuerza en un 15%
        self.defense = self.defense * 1.15  # Aumenta la defensa en un 15%
        print(f"{self.name} ha subido al nivel {self.level}!")  # Mensaje de nivelación
        print(f"Tus nuevas estadisticas son: Salud: {self.health}, Fuerza: {self.strength}, Defensa: {self.defense}")  # Muestra las nuevas estadísticas

    def add_experience(self, amount):
        self.experience += amount  # Aumenta la experiencia acumulada
        # Comprueba si la experiencia acumulada supera el objetivo
        while self.experience >= self.xp_objetive:
            self.experience -= self.xp_objetive  # Resta el objetivo de experiencia
            self.level_up()  # Llama al método level_up para aumentar el nivel
            self.xp_objetive = (self.xp_objetive * 1.2)  # Aumenta el objetivo de experiencia en un 20% para el siguiente nivel

    def take_damage(self, damage):
        # Calcula el daño real restando la defensa del daño recibido
        self.health -= max(0, damage - self.defense)  # Asegura que la salud no sea negativa

    def has_items(self):
        return len(self.items) > 0  # Devuelve True si el jugador tiene ítems, False si no

    def is_alive(self):
        return self.health > 0  # Devuelve True si el jugador está vivo (salud > 0)

    def __str__(self):
        return f"{self.name} (Salud: {self.health})"  # Representación en forma de cadena del jugador
