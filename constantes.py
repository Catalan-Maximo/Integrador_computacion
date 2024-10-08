from allies import Ally
from enemies import Enemy

# Aliados
Ally_village = Ally("Aliado de la Aldea", 40, 10, 5, 1)
Ally_dungeon = Ally("Aliado de la Dungeon", 50, 15, 8, 1)

# Narrativa
Introduccion = """
   En un reino olvidado, las fuerzas del mal han despertado. 
   Eres parte de un grupo de héroes que ha sido convocado para detener a 
   las criaturas que están aterrorizando la tierra. Cada paso que des te acercará más 
   a la verdad detrás de esta oscuridad. ¡Prepárate para la aventura de tu vida!
"""

Capitulos = {
   1: "Capítulo 1: La llamada a la aventura\n\n"
      "Tu viaje comienza en la aldea de los aventureros. Aquí, te reunirás con "
      "otros héroes para planear tu travesía hacia la Cueva de las Brujas.",
   
   2: "Capítulo 2: Enfrentando a los muertos\n\n"
      "Después de superar la Cueva de las Brujas te encuentras una aldea "
      "donde un habitante se ofrece como ayuda. Luego te diriges a la Tumba de tus Sueños, "
      "donde los no-muertos te desafiarán en cada esquina.",
   
   3: "Capítulo 3: La batalla final\n\n"
      "Finalmente, has llegado al corazón de la oscuridad, "
      "ayudado por el habitante de la aldea y un explorador de la Cueva de las Brujas. "
      "Los Orcos y sus demonios te esperan en una batalla que decidirá el destino del mundo."
}

Final = "Has completado la historia. ¡Felicitaciones, héroe!"

# Items
Potion = {"name": "Poción de Salud", "effect": "heal"}
Sword = {"name": "Espada de Fuerza", "effect": "boost_strength"}
Amulet = {"name": "Amuleto de Defensa", "effect": "boost_defense"}

# Combate
Win = "¡Has ganado la batalla! Todos los enemigos han sido derrotados."
Lose = "Oh no, todos tus personajes han sido derrotados. Fin del juego."
Start_combat = "Te encontraste con un grupo de enemigos ¡comienza la batalla!"

# Enemigos
# Instancias de enemigos
Goblin_l1 = Enemy("Goblin", 10, 8, 5, 1)
Skeleton_l1 = Enemy("Skeleton", 15, 10, 7, 1)
Skeleton_l2 = Enemy("Skeleton", 25, 12, 9, 2)
Witch_l1 = Enemy("Witch", 20, 12, 7, 1)
Witch_l2 = Enemy("Witch", 25, 14, 9, 2)
Witch_l3 = Enemy("Witch", 30, 16, 11, 3)
Demon_l1 = Enemy("Demon", 35, 18, 12, 2)
Demon_l2 = Enemy("Demon", 40, 20, 14, 3)
Orco_l1 = Enemy("Orco", 50, 22, 16, 3)

#Dungeons
#dificultades
Easy = 1
Medium = 2
Hard = 3
from dungeons import Dungeon #Da error a la hora de ponerlo arriba
dungeon1 = Dungeon(name="Cueva de las Brujas", level_diff=1, num_enemies=3, num_allies=0)
dungeon2 = Dungeon(name="La tumba de tus sueños", level_diff=2, num_enemies=4, num_allies=1)
dungeon3 = Dungeon(name="Orcos y sus demonios", level_diff=3, num_enemies=5, num_allies=2)

#gamecontroller
interd2 = "Lamentablemente, ésta mazmorra no es como la anterior"
interd3_1 = "Esa solo fue la primera oleada de enemigos, preparate"
interd3_2 = "Habiendo sobrevivido a la segunda oleada, te enfrentas a la última, para salvar el mundo"
