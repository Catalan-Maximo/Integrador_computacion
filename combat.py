import random
from Items import Item
from constantes import Win, Lose, Start_combat, Sword, Potion, Amulet

class Combat:
    def __init__(self, characters, enemies, player1, allies=None):
        self.characters = characters
        self.enemies = enemies
        self.player1 = player1
        self.allies = allies if allies is not None else []

    def take_turn(self, participants, opponents, turn_type):
        for participant in participants:
            if participant.health > 0:
                if turn_type == "player":
                    print(f"Es el turno de {participant.name}")
                    while True:
                        action = input("Elige una acción: 1. Atacar 2. Usar ítem: ")
                        if action == "1":
                            while True:
                                try:
                                    enemy = self.select_enemy()
                                    break
                                except (IndexError, ValueError):
                                    print("Selección no válida. Por favor, elige de nuevo.")
                            damage = participant.attack(enemy)
                            print(f"{participant.name} atacó a {enemy.name} y le hizo {damage} de daño.")
                            if enemy.health <= 0:
                                print(f"{enemy.name} ha sido derrotado!")
                                opponents.remove(enemy)
                            break
                        elif action == "2":
                            while True:
                                if participant.inventory:  # Verificar si hay ítems en el inventario
                                    item = participant.choose_item_to_use()  # Seleccionar ítem
                                    if item:  # Verificar si se seleccionó un ítem válido
                                        participant.use_item(item)  # Usar el ítem
                                        break
                                    else:
                                        print("Selección inválida.")
                                else:
                                    print("No tienes items, por favor ataca.")
                                break
                        else:
                            print("Acción no válida. Por favor, elige de nuevo.")
                    
                elif turn_type == "enemy" or "ally": #preguntar profe, aliado no ataca automatico
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
                if character.name == self.player1.name:
                    character.gain_experience(75)  # Dar experiencia por ganar ronda
                else:
                    pass
                if character.name == self.player1.name and random.randint(1, 100) <= 20:  # 20% de probabilidad de obtener un ítem solo para player1
                    item = random.choice([Potion, Sword, Amulet])
                    print(f"{character.name} ha recibido un {item['name']}!")
                    character.add_item(Item(item["name"], item["effect"]))
                else:
                    pass
            return True
        if all(character.health <= 0 for character in self.characters):
            print(Lose)
            return True
        return False
    
#hacer que si hay 2 enemigos(mismo tipo/nombre) solo ataque a 1
#preguntar profe, aliado no ataca automatico
