from gamecontroller import game_flow
from constantes import Lose

def main():
    try:
        game_flow()
    except Exception as e:
        print(Lose)

if __name__ == "__main__":
    main()
