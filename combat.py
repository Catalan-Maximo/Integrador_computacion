import random
from constantes import win, lose, start_combat

class Combat:
    def __init__(self, characters, enemies, allies=None):
        self.characters = characters            #Lista de Jugadores y Enemigos
        self.enemies = enemies
        self.allies = allies if allies is not None else []

    def player_turn(self):
        for character in self.characters:
            if character.health > 0:
                print(f"\nEs el turno de {character.name}.")
                enemy = self.select_enemy()
                damage = character.attack(enemy)
                print(f"{character.name} le hizo {damage} de daño a {enemy.name}.")
                if enemy.health <= 0:
                    print(f"{enemy.name} ha sido derrotado!")
                    self.enemies.remove(enemy)

    def ally_turn(self):
        for ally in self.allies:
            if ally.health > 0:
                enemy = random.choice(self.enemies)
                damage = ally.attack(enemy)
                print(f"{ally.name} atacó a {enemy.name} y le hizo {damage} de daño.")
                if enemy.health <= 0:
                    print(f"{enemy.name} ha sido derrotado!")
                    self.enemies.remove(enemy)

    def enemy_turn(self):
        for enemy in self.enemies:
            if enemy.health > 0:
                character = random.choice(self.characters)
                damage = enemy.attack(character)
                print(f"{enemy.name} atacó a {character.name} y le hizo {damage} de daño.")
                if character.health <= 0:
                    print(f"{character.name} ha sido derrotado!")

    def select_enemy(self):
        print("Enemigos disponibles:")
        for i, enemy in enumerate(self.enemies):
            print(f"{i + 1}. {enemy.name} - Salud: {enemy.health}")
        choice = int(input("Elige un enemigo para atacar (1, 2, 3...): ")) - 1
        return self.enemies[choice]

    def is_battle_over(self):
        if all(enemy.health <= 0 for enemy in self.enemies):
            print(win)
            for character in self.characters:
                character.gain_experience(75)  # Dar experiencia por ganar ronda
            return True
        if all(character.health <= 0 for character in self.characters):
            print(lose)
            return True
        return False
    
    def start_battle(self):
        print(start_combat)
        while not self.is_battle_over():
            self.player_turn()
            if not self.is_battle_over() and self.allies:
                self.ally_turn()
            if not self.is_battle_over():
                self.enemy_turn()
