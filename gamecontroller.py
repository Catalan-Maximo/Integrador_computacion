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

# Clase principal que controla el flujo del juego
class GameController:
    def __init__(self):
        os.system('cls')  # Limpia la pantalla
        print(GAME_TITLE)  # Muestra el título del juego
        time.sleep(5)  # Pausa de 5 segundos para que el jugador lo vea
        os.system('cls')  # Limpia la pantalla de nuevo
        print(INTRO_GAME)  # Muestra la introducción al juego
        self.player = self.create_player()  # Crea al personaje principal del jugador
        self.allies = self.create_allies()  # Crea los aliados del jugador
        self.dungeon = self.create_dungeon()  # Crea la mazmorra que el jugador debe atravesar
        self.narrative = Narrative()  # Instancia la narrativa del juego
        self.current_battle = 0  # Controla el progreso del jugador en los combates
        self.items = self.create_items()  # Crea los ítems que se pueden ganar durante el juego

    # Método para crear al personaje del jugador
    def create_player(self):
        player_name = input(PLNAME_CREATOR)  # Pide al jugador que ingrese su nombre
        print(TEXT_PLAYER_SELECT)  # Muestra las opciones de clase

        try:
            class_choice = int(input(CLASSSEL))  # Pide al jugador que seleccione una clase
            
            # Asigna una clase basada en la selección del jugador
            if class_choice == 1:
                player_class = "Guerrero"
            elif class_choice == 2:
                player_class = "Mago"
            elif class_choice == 3:
                player_class = "Arquero"
            else:
                print(INVALIDSELPLAYER)  # Si no selecciona correctamente, se le asigna "Guerrero"
                player_class = "Guerrero"
                time.sleep(2)

            return Player(player_name, player_class)  # Crea y retorna el personaje del jugador
        except ValueError:
            # Si se introduce un valor no numérico, se crea el jugador como "Guerrero"
            print(INVALIDSELPLAYER)
            time.sleep(2)
            return Player(player_name, "Guerrero")

    # Método para crear aliados que acompañan al jugador
    def create_allies(self):
        # Crea dos aliados con nombres predefinidos y clases aleatorias
        return [Ally("Aliado 1", random.choice(PLAYER_CLASSES)), Ally("Aliado 2", random.choice(PLAYER_CLASSES))]

    # Método para crear la mazmorra
    def create_dungeon(self):
        return Dungeon("Cripta del Olvido")  # La mazmorra tiene un nombre específico

    # Método para crear ítems que pueden ser obtenidos
    def create_items(self):
        # Crea instancias de ítems que se pueden ganar durante el juego
        return [
            Item("Poción de Salud"),
            Item("Amuleto de Fuerza"),
            Item("Escudo Mágico")
        ]

    # Método que inicia el juego
    def start_game(self):
        os.system('cls')  # Limpia la pantalla
        print(self.narrative.story)  # Muestra la narrativa del juego
        time.sleep(30)  # Pausa de 30 segundos para que el jugador lea la historia
        os.system('cls')  # Limpia la pantalla
        self.start_battles()  # Inicia las batallas

    # Método que maneja la secuencia de batallas
    def start_battles(self):
        battles = self.dungeon.get_battles()  # Obtiene la lista de batallas de la mazmorra

        # Recorre cada batalla
        for index, enemies in enumerate(battles):
            time.sleep(5)
            os.system('cls')  # Limpia la pantalla antes de cada batalla
            print(BATTLE_HISTORIES[index])  # Muestra la narrativa correspondiente a la batalla
            time.sleep(15)
            os.system('cls')
            print(f"¡Prepárate para la batalla {self.current_battle + 1}!")  # Anuncia la batalla actual

            # Si el jugador pierde una batalla, el juego termina
            if not self.combat(enemies):
                print(LOSECOMBAT)
                return
            self.current_battle += 1  # Avanza al siguiente combate

        time.sleep(5)
        os.system('cls')
        print(FINAL_NARRATIVE)  # Muestra la narrativa final después de todas las batallas

    # Método que ejecuta el combate por turnos
    def combat(self, enemies):
        result = turn_based_combat(self.player, self.allies, enemies)  # Llama a la función de combate por turnos
        if result:  # Si el jugador gana la batalla
            self.reward_item()  # Recompensa al jugador con un ítem
        return result  # Retorna el resultado de la batalla

    # Método que otorga un ítem como recompensa
    def reward_item(self):
        if random.randint(1, 100) < 35:  # Probabilidad del 35% de obtener un ítem
            item = random.choice(self.items)  # Selecciona un ítem aleatorio
            self.player.items.append(item)  # Agrega el ítem al inventario del jugador
            print(f"¡Has ganado un nuevo ítem: {item.name}!")  # Muestra el ítem ganado
