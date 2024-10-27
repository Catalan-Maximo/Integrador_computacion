from gamecontroller import GameController

def main():
    game = GameController()  # Crea una instancia de GameController, que inicializa y configura el juego
    game.start_game()  # Llama al método start_game para comenzar el juego

# Comprueba si este archivo se está ejecutando como el programa principal
if __name__ == "__main__":
    main()  # Llama a la función main si el script es ejecutado directamente
