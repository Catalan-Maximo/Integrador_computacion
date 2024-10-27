from constantes import ITEMS

class Item:
    def __init__(self, name):
        self.name = name  # Almacena el nombre del ítem
        self.effect_function = self.get_effect()  # Llama a 'get_effect' para obtener la función de efecto correspondiente al ítem

    def effect(self, player):
        self.effect_function(player)  # Aplica el efecto del ítem al jugador

    def get_effect(self):
        # Dependiendo del nombre del ítem, devuelve una función lambda que modifica el atributo del jugador
        if self.name == 'Poción de Salud':
            # Poción de Salud aumenta la salud del jugador en 20
            return lambda player: setattr(player, 'health', player.health + 20)
        elif self.name == 'Amuleto de Fuerza':
            # Amuleto de Fuerza aumenta la fuerza del jugador en 5
            return lambda player: setattr(player, 'strength', player.strength + 5)
        elif self.name == 'Escudo Mágico':
            # Escudo Mágico aumenta la defensa del jugador en 5
            return lambda player: setattr(player, 'defense', player.defense + 5)
        
        # Si el ítem no es reconocido, devuelve una función que no hace nada
        return lambda player: None
