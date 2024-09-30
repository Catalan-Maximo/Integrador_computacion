from allies import Ally
from enemies import Enemy

# Aliados
ally_village = Ally("Aliado de la Aldea", 40, 10, 5, 1)
ally_dungeon = Ally("Aliado de la Dungeon", 50, 15, 8, 1)

# Narrativa
introduccion = """
    En un reino olvidado, las fuerzas del mal han despertado. 
    Eres parte de un grupo de héroes que ha sido convocado para detener a 
    las criaturas que están aterrorizando la tierra. Cada paso que des te acercará más 
    a la verdad detrás de esta oscuridad. ¡Prepárate para la aventura de tu vida!
"""

capitulos = {
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

final = "Has completado la historia. ¡Felicitaciones, héroe!"

# Items
potion = {"name": "Poción de Salud", "effect": "heal"}
sword = {"name": "Espada de Fuerza", "effect": "boost_strength"}
amulet = {"name": "Amuleto de Defensa", "effect": "boost_defense"}

# Combate
win = "¡Has ganado la batalla! Todos los enemigos han sido derrotados."
lose = "Oh no, todos tus personajes han sido derrotados. Fin del juego."
start_combat = "Te encontraste con un grupo de enemigos ¡comienza la batalla!"

#Enemigos
# Instancias de enemigos
goblin_l1 = Enemy("Goblin", 10, 8, 5, 1)
skeleton_l1 = Enemy("Skeleton", 15, 10, 7, 1)
skeleton_l2 = Enemy("Skeleton", 25, 12, 9, 2)
witch_l1 = Enemy("Witch", 20, 12, 7, 1)
witch_l2 = Enemy("Witch", 25, 14, 9, 2)
witch_l3 = Enemy("Witch", 30, 16, 11, 3)
demon_l1 = Enemy("Demon", 35, 18, 12, 2)
demon_l2 = Enemy("Demon", 40, 20, 14, 3)
orco_l1 = Enemy("Orco", 50, 22, 16, 3)

#Dungeons
#dificultades
Easy = 1
Medium = 2
Hard = 3


#nombre de todas las constantes en MAYUSCULAS
