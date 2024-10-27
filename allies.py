from player import Player

# Definimos una nueva clase llamada 'Ally' que hereda de la clase 'Player'
class Ally(Player):
    
    # Método constructor de la clase 'Ally'
    # Se inicializa con los parámetros 'name' (nombre del aliado) y 'player_class' (clase o tipo del jugador)
    def __init__(self, name, player_class):
        # Llamamos al constructor de la clase padre 'Player' usando 'super()' para inicializar sus atributos
        # 'super().__init__(name, player_class)' se asegura de que los atributos de 'Player' se configuren correctamente
        super().__init__(name, player_class)
