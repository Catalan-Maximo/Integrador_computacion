import random

class Player:
    def __init__(self, name, char_class, health, strength, defense, level=1):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = 0
        self.experience_to_next_level = 100
        self.inventory = []  # Inventario de ítems

    def attack(self, enemy):
        damage = max(0, self.strength - enemy.defense)
        enemy.health -= damage
        return damage

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} ganó {amount} puntos de experiencia.")
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        self.health += 12
        self.strength += 2
        self.defense += 2
        print(f"¡{self.name} subió al nivel {self.level}!")
        print(f"Nuevos atributos: Salud {self.health}, Fuerza {self.strength}, Defensa {self.defense}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} añadido al inventario de {self.name}.")

    def use_item(self, item):
        if item in self.inventory:
            item.apply(self)
            self.inventory.remove(item)
            print(f"{self.name} usó {item.name}.")
        else:
            print(f"{self.name} no tiene {item.name} en su inventario.")

    def __str__(self):
        return (f"{self.name} ({self.char_class}) - Nivel {self.level}: Salud {self.health}, "
                f"Fuerza {self.strength}, Defensa {self.defense}, Experiencia {self.experience}/"
                f"{self.experience_to_next_level}")

# Subclases Guerrero, Mago, Arquero
class Guerrero(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Guerrero: ")
        super().__init__(name, "Guerrero", 70, 15, 8)

class Mago(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Mago: ")
        super().__init__(name, "Mago", 50, 20, 6)

class Arquero(Player):
    def __init__(self):
        name = input("Ingrese el nombre de su Arquero: ")
        super().__init__(name, "Arquero", 60, 12, 4)

def player_selection():
    print("Selecciona tu personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    player_class = input("Elige una opción: ")

    if player_class == "1":
        player1 = Guerrero()
    elif player_class == "2":
        player1 = Mago()
    elif player_class == "3":
        player1 = Arquero()
    else:
        print("Opción inválida. Inténtalo de nuevo.")
    return player1

#clases en archivos diferentes