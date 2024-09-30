import random
from constantes import win, lose, start_combat

class Combat:
    def __init__(self, characters, enemies, allies=None):
        self.characters = characters            #Lista de Jugadores y Enemigos
        self.enemies = enemies
        self.allies = allies if allies is not None else []

def take_turn(self, participants, opponents, participant_type):
    for participant in participants:
        if participant.health > 0:
            if participant_type == "player":
                print(f"\nEs el turno de {participant.name}.")
                opponent = self.select_enemy()
            else:
                opponent = random.choice(opponents)
            
            damage = participant.attack(opponent)
            print(f"{participant.name} atacó a {opponent.name} y le hizo {damage} de daño.")
            
            if opponent.health <= 0:
                print(f"{opponent.name} ha sido derrotado!")
                opponents.remove(opponent)

    def start_battle(self):
        print(start_combat)
        while not self.is_battle_over():
            self.take_turn(self.characters, self.enemies, "player")
            if not self.is_battle_over() and self.allies:
                self.take_turn(self.allies, self.enemies, "ally")
            if not self.is_battle_over():
                self.take_turn(self.enemies, self.characters, "enemy")

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



#hacer una unica funcion y que cambie el parametro nomas porque se repite mucho el texto
