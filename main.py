from narrative import Narrative
from combat import Combat
from dungeons import Dungeon
import enemies 
from Items import Item
from player import Guerrero, Mago, Arquero, player_selection
import random
from allies import aliado1, aliado2


def main():
    # Crear instancia de la narrativa
    narrativa = Narrative()

    # Mostrar introducción
    narrativa.display_introduction()
    player1 = player_selection()
    aliado_aldea = aliado1()
    aliado_dungeon = aliado2()
    narrativa.display_current_chapter()

    dungeon1 = Dungeon(name="Cueva de las Brujas", level_diff=1, num_enemies=3, num_allies=0)
    dungeon1.generar_enemigos()
    dungeon1.generar_aliados()

    # Combate
    combat = Combat(characters=[player1], enemies=dungeon1.enemies)
    combat.start_battle()
    
    # Avanzar al siguiente capítulo
    narrativa.advance_chapter()

    dungeon2 = Dungeon(name="La tumba de tus sueños", level_diff=2, num_enemies=4, num_allies=1)
    dungeon2.generar_enemigos()
    dungeon2.generar_aliados()

    combat = Combat(characters=[player1, aliado_aldea], enemies=dungeon2.enemies)
    combat.start_battle()
    combat.start_battle()

    narrativa.advance_chapter()

    dungeon3 = Dungeon(name="Orcos y sus demonios", level_diff=3, num_enemies=5, num_allies=2)
    dungeon3.generar_enemigos()
    dungeon3.generar_aliados()

    combat = Combat(characters=[player1, aliado_aldea, aliado_dungeon], enemies=dungeon3.enemies)
    combat.start_battle()
    combat.start_battle()
    combat.start_battle()

    narrativa.advance_chapter()

if __name__ == "__main__":
    main()
