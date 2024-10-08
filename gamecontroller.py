from player import Player  
from narrative import Narrative
from combat import Combat
from constantes import Ally_village, Ally_dungeon, dungeon1, dungeon2, dungeon3, interd2, interd3_1, interd3_2

def player_selection():
    print("Selecciona tu personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    player_class = input("Elige una opción: ")

    if player_class == "1":
        name = input("Ingrese el nombre de su Guerrero: ")
        player1 = Player(name, "Guerrero", 70, 15, 8)
    elif player_class == "2":
        name = input("Ingrese el nombre de su Mago: ")
        player1 = Player(name, "Mago", 50, 20, 6)
    elif player_class == "3":
        name = input("Ingrese el nombre de su Arquero: ")
        player1 = Player(name, "Arquero", 60, 12, 4)
    else:
        print("Opción inválida. Inténtalo de nuevo.")
        return None

    return player1

def start_combat(player1, aliados, dungeon):
    dungeon.generar_enemigos()
    dungeon.generar_aliados()
    combat = Combat(characters=[player1] + aliados, enemies=dungeon.enemies, player1=player1)
    combat.start_battle()
    return player1.health > 0

def game_flow():
    # Crear instancia de la narrativa
    narrativa = Narrative()

    # Mostrar introducción
    narrativa.display_introduction()
    player1 = player_selection()
    aliado_aldea = Ally_village
    aliado_dungeon = Ally_dungeon
    narrativa.display_current_chapter()

    # Primera mazmorra
    dungeon = dungeon1
    if not start_combat(player1, [], dungeon):
        return

    narrativa.advance_chapter()

    # Segunda mazmorra
    dungeon = dungeon2
    if not start_combat(player1, [aliado_aldea], dungeon):
        return

    print(interd2)
    if not start_combat(player1, [aliado_aldea], dungeon):
        return

    narrativa.advance_chapter()

    # Tercera mazmorra
    dungeon = dungeon3
    if not start_combat(player1, [aliado_aldea, aliado_dungeon], dungeon):
        return

    print(interd3_1)
    if not start_combat(player1, [aliado_aldea, aliado_dungeon], dungeon):
        return

    print(interd3_2)
    start_combat(player1, [aliado_aldea, aliado_dungeon], dungeon)

    narrativa.advance_chapter()
