import random
from Items import Item
from constantes import Win, Lose, Start_combat, Sword, Potion, Amulet

class Combat:
    def __init__(self, characters, enemies, player1, allies=None):
        self.characters = characters
        self.enemies = enemies
        self.player1 = player1
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
        print(Start_combat)
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
            print(Win)
            for character in self.characters:
                character.gain_experience(75)  # Dar experiencia por ganar ronda
                if character.name == self.player1.name and random.randint(1, 100) <= 20:  # 20% de probabilidad de obtener un ítem solo para player1
                    item = random.choice([Potion, Sword, Amulet])
                    print(f"{character.name} ha recibido un {item['name']}!")
                    character.add_item(Item(item["name"], item["effect"]))
            return True
        if all(character.health <= 0 for character in self.characters):
            print(Lose)
            return True
        return False
