# game_controller.py

from player import Player
from allies import Ally
from combat import turn_based_combat
from dungeons import Dungeon
from narrative import Narrative

class GameController:
    def __init__(self):
        print("¡Bienvenido al juego de aventura!")
        self.player = self.create_player()
        self.allies = self.create_allies()
        self.dungeon = self.create_dungeon()
        self.narrative = Narrative()
        self.current_battle = 0  # Para llevar el control de los combates

    def create_player(self):
        player_name = input("Por favor, ingresa el nombre de tu personaje: ")
        
        print("Selecciona la clase de tu personaje:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Arquero")

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
        return [Ally("Aliado 1", "Guerrero"), Ally("Aliado 2", "Mago")]

    def create_dungeon(self):
        return Dungeon("Mazmorras de la Perdición")

    def start_game(self):
        print(self.narrative.story)
        self.start_battles()

    def start_battles(self):
        battles = self.dungeon.get_battles()  # Método que devuelve los enemigos de cada combate

        for enemies in battles:
            print(f"¡Prepárate para la batalla {self.current_battle + 1}!")
            if not self.combat(enemies):
                print("¡Has perdido la batalla! Fin del juego.")
                return
            self.current_battle += 1

        print("¡Has completado todas las batallas! Felicitaciones.")

    def combat(self, enemies):
        return turn_based_combat(self.player, self.allies, enemies)