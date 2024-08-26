import random

class Combat:
    def __init__(self, characters, enemies):
        self.characters = characters            #Lista de Jugadores y Enemigos
        self.enemies = enemies

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
                    character.gain_experience(50)  # Dar experiencia por derrotar a un enemigo

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
            print("¡Has ganado! Todos los enemigos han sido derrotados.")
            return True
        if all(character.health <= 0 for character in self.characters):
            print("Oh no, todos tus personajes han sido derrotados. Fin del juego.")
            return True
        return False

    def start_battle(self):
        while not self.is_battle_over():
            self.player_turn()
            if not self.is_battle_over():
                self.enemy_turn()
