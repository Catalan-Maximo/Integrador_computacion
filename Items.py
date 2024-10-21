from constantes import ITEMS

class Item:
    def __init__(self, name):
        self.name = name
        self.effect_function = self.get_effect()

    def effect(self, player):
        self.effect_function(player)

    def get_effect(self):
        if self.name == 'Poción de Salud':
            return lambda player: setattr(player, 'health', player.health + 20)  # Asegura que la salud no exceda 100
        elif self.name == 'Amuleto de Fuerza':
            return lambda player: setattr(player, 'strength', player.strength + 5)
        elif self.name == 'Escudo Mágico':
            return lambda player: setattr(player, 'defense', player.defense + 5)
        return lambda player: None  # En caso de que no haya un efecto