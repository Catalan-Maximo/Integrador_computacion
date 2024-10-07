from gamecontroller import game_flow

def main():
    try:
        game_flow()
    except Exception as e:
        print("Has perdido, vuelve a jugar otra vez e intenta vencer.")

if __name__ == "__main__":
    main()
