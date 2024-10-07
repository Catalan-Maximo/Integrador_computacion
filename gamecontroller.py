from player import Player  
from narrative import Narrative
from combat import Combat
from dungeons import Dungeon
from Items import Item
from constantes import Ally_dungeon, Ally_village

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

def game_flow():
    # Crear instancia de la narrativa
    narrativa = Narrative()

    # Mostrar introducción
    narrativa.display_introduction()
    player1 = player_selection()
    aliado_aldea = Ally_village
    aliado_dungeon = Ally_dungeon
    narrativa.display_current_chapter()

    while player1.health > 0:
        dungeon1 = Dungeon(name="Cueva de las Brujas", level_diff=1, num_enemies=3, num_allies=0)
        dungeon1.generar_enemigos()
        dungeon1.generar_aliados()
        combat = Combat(characters=[player1], enemies=dungeon1.enemies, player1=player1)
        combat.start_battle()
        if player1.health <= 0:
            break
        else:
            narrativa.advance_chapter()
            dungeon2 = Dungeon(name="La tumba de tus sueños", level_diff=2, num_enemies=4, num_allies=1)
            dungeon2.generar_enemigos()
            dungeon2.generar_aliados()
            combat = Combat(characters=[player1, aliado_aldea], enemies=dungeon2.enemies, player1=player1)
            combat.start_battle()
            if player1.health <= 0:
                break
            else:
                print("Lamentablemente, ésta mazmorra no es como la anterior")
                combat.start_battle()
                if player1.health <= 0:
                    break
                else:
                    narrativa.advance_chapter()
                    dungeon3 = Dungeon(name="Orcos y sus demonios", level_diff=3, num_enemies=5, num_allies=2)
                    dungeon3.generar_enemigos()
                    dungeon3.generar_aliados()
                    combat = Combat(characters=[player1, aliado_aldea, aliado_dungeon], enemies=dungeon3.enemies, player1=player1)
                    combat.start_battle()
                    if player1.health <= 0:
                        break
                    else:
                        print("Esa solo fue la primera oleada de enemigos, preparate")
                        combat.start_battle()
                        if player1.health <= 0:
                            break
                        else:
                            print("Habiendo sobrevivido a la segunda oleada, te enfrentas a la última, para salvar el mundo")
                            combat.start_battle()
                            if player1.health <= 0:
                                break
                            else:
                                narrativa.advance_chapter()
                                break

#que no se repitan tanta contidad de veces por eje los dunjeon, haciendo la modularidad con funcionesss
#hacer que si hay 2 enemigos(mismo tipo/nombre) solo ataque a 1
#hacer que no quede vida en negativo