import enemies


class Dungeon:
    def __init__(self, name, level_diff, num_enemies):
        self.name = name
        self.level_diff = level_diff
        self.num_enemies = num_enemies

    def dungeon_1(self):
        self.name = "Cueva de las Brujas"
        self.level_diff = 1
        self.num_enemies = 3

    def dungeon_2(self):
        self.name = "La tumba de tus sueños"
        self.level_diff = 2
        self.num_enemies = 4

    def dungeon_3(self):
        self.name = "Orcos y sus demonios"
        self.level_diff = 3
        self.num_enemies = 5