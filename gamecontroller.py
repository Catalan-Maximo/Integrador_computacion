import os
import time
import random
from player import Player
from allies import Ally
from combat import turn_based_combat
from dungeons import Dungeon
from narrative import Narrative
from Items import Item
from constantes import PLAYER_CLASSES, BATTLE_HISTORIES, INTRO_GAME, FINAL_NARRATIVE, TEXT_PLAYER_SELECT

class GameController:
    def __init__(self):
        os.system('cls')
        print(INTRO_GAME)
        self.player = self.create_player()
        self.allies = self.create_allies()
        self.dungeon = self.create_dungeon()
        self.narrative = Narrative()
        self.current_battle = 0  # Para llevar el control de los combates
        self.items = self.create_items()

    def create_player(self):
        player_name = input("Por favor, ingresa el nombre de tu personaje: ")
        
        print(TEXT_PLAYER_SELECT)

        class_choice = int(input("Selecciona el número de la clase: "))
        
        if class_choice == 1:
            player_class = "Guerrero"
        elif class_choice == 2:
            player_class = "Mago"
        elif class_choice == 3:
            player_class = "Arquero"
        else:
            print("Selección inválida. Se asignará la clase Guerrero por defecto.")
            player_class = "Guerrero"

        return Player(player_name, player_class)

    def create_allies(self):
        return [Ally("Aliado 1", random.choice(PLAYER_CLASSES)), Ally("Aliado 2", random.choice(PLAYER_CLASSES))]

    def create_dungeon(self):
        return Dungeon("Global Dungeon")

    def create_items(self):
        # Crear instancias de ítems
        return [
            Item("Poción de Salud"),
            Item("Amuleto de Fuerza"),
            Item("Escudo Mágico")
        ]

    def start_game(self):
        os.system('cls')
        print(self.narrative.story)
        self.start_battles()

    def start_battles(self):
        battles = self.dungeon.get_battles()  # Método que devuelve los enemigos de cada combate

        for index, enemies in enumerate(battles):
            time.sleep(7)
            os.system('cls')
            print(BATTLE_HISTORIES[index])  # Muestra la narrativa de la batalla correspondiente
            time.sleep(4)
            os.system('cls')
            print(f"¡Prepárate para la batalla {self.current_battle + 1}!")

            if not self.combat(enemies):
                print("¡Has perdido la batalla! Fin del juego.")
                return
            self.current_battle += 1

        time.sleep(1)
        print(FINAL_NARRATIVE)

    def combat(self, enemies):
        result = turn_based_combat(self.player, self.allies, enemies)
        if result:  # Si el jugador ganó la batalla
            self.reward_item()  # Llamar a la función para recompensar un ítem
        return result

    def reward_item(self):
        if random.randint(1, 100) < 35:  # 35% de probabilidad
            item = random.choice(self.items)  # Elegir un ítem aleatorio de la lista
            self.player.items.append(item)  # Agregar el ítem al inventario del jugador
            print(f"¡Has ganado un nuevo ítem: {item.name}!")
