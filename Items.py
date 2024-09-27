class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply(self, character):
        if self.effect == "heal":
            character.health += 30
            print(f"{character.name} se curó 30 puntos de salud.")
        elif self.effect == "boost_strength":
            character.strength += 5
            print(f"La fuerza de {character.name} aumentó en 5 puntos.")
        elif self.effect == "boost_defense":
            character.defense += 5
            print(f"La defensa de {character.name} aumentó en 5 puntos.")

    def __str__(self):
        return f"{self.name} ({self.effect})"
