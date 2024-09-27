from allies import Ally

# Aliados
aliado_village = Ally("Aliado de la Aldea", 40, 10, 5, 1)
aliado_dungeon = Ally("Aliado de la Dungeon", 50, 15, 8, 1)

# Introducción de la historia
introduccion = """
    En un reino olvidado, las fuerzas del mal han despertado. 
    Eres parte de un grupo de héroes que ha sido convocado para detener a 
    las criaturas que están aterrorizando la tierra. Cada paso que des te acercará más 
    a la verdad detrás de esta oscuridad. ¡Prepárate para la aventura de tu vida!
"""

# Capítulos de la historia
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

# Items
potion = {"name": "Poción de Salud", "effect": "heal"}
sword = {"name": "Espada de Fuerza", "effect": "boost_strength"}
amulet = {"name": "Amuleto de Defensa", "effect": "boost_defense"}





#falta terminar de pasar las constantes de dungeons, combate y items, no lo termine porque se me quedo sin bateria la compu :)
