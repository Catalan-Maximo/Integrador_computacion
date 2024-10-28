import os
import time
import random
from player import Player
from allies import Ally
from combat import turn_based_combat
from dungeons import Dungeon
from narrative import Narrative
from Items import Item
from constantes import *

class GameController:
    def __init__(self):
        os.system('cls')
        print(GAME_TITLE)
        time.sleep(5)
        os.system('cls')
        print(INTRO_GAME)
        self.player = self.create_player()
        self.allies = self.create_allies()
        self.dungeon = self.create_dungeon()
        self.narrative = Narrative()
        self.current_battle = 0
        self.items = self.create_items()

    def create_player(self):
        player_name = input(PLNAME_CREATOR)
        print(TEXT_PLAYER_SELECT)

        try:
            class_choice = int(input(CLASSSEL))
            if class_choice == 1:
                player_class = "Guerrero"
            elif class_choice == 2:
                player_class = "Mago"
            elif class_choice == 3:
                player_class = "Arquero"
            else:
                print(INVALIDSELPLAYER)
                player_class = "Guerrero"
                time.sleep(2)

            return Player(player_name, player_class)  # Crea y retorna el personaje del jugador
        except ValueError:
            print(INVALIDSELPLAYER)
            time.sleep(2)
            return Player(player_name, "Guerrero")

    def create_allies(self):
        return [Ally("Aliado 1", random.choice(PLAYER_CLASSES)), Ally("Aliado 2", random.choice(PLAYER_CLASSES))]

    def create_dungeon(self):
        return Dungeon("Cripta del Olvido")

    def create_items(self):
        return [
            Item("Poción de Salud"),
            Item("Amuleto de Fuerza"),
            Item("Escudo Mágico")
        ]

    def start_game(self):
        os.system('cls')
        print(self.narrative.story)
        time.sleep(30)
        os.system('cls')
        self.start_battles()

    def start_battles(self):
        battles = self.dungeon.get_battles()

        # Recorre cada batalla
        for index, enemies in enumerate(battles):
            time.sleep(5)
            os.system('cls')
            print(BATTLE_HISTORIES[index])  # Muestra la narrativa correspondiente a la batalla
            time.sleep(15)
            os.system('cls')
            print(f"¡Prepárate para la batalla {self.current_battle + 1}!")

            # Si el jugador pierde una batalla, el juego termina
            if not self.combat(enemies):
                print(LOSECOMBAT)
                return
            self.current_battle += 1

        time.sleep(5)
        os.system('cls')
        print(FINAL_NARRATIVE)

    # Método que ejecuta el combate por turnos
    def combat(self, enemies):
        result = turn_based_combat(self.player, self.allies, enemies)
        if result:
            self.reward_item()
        return result

    def reward_item(self):
        if random.randint(1, 100) < 35:  # Probabilidad del 35% de obtener un ítem
            item = random.choice(self.items)
            self.player.items.append(item)
            print(f"¡Has ganado un nuevo ítem: {item.name}!")
