import random

def turn_based_combat(player, allies, enemies):
    while True:
        # Turno del jugador
        if player.is_alive():
            while True:
                print("\nSelecciona una acción:")
                print("1. Atacar")
                print("2. Usar ítem")

                action_input = input("Selecciona el número de la acción: ")
                if action_input.isdigit():  # Verifica si la entrada es un número
                    action = int(action_input)
                else:
                    print("Entrada inválida. Por favor, ingresa un número.")
                    continue  # Regresa al inicio del ciclo

                if action == 1:
                    while True:  # Ciclo para permitir múltiples intentos de ataque
                        print("\nSelecciona un enemigo para atacar:")
                        for i, enemy in enumerate(enemies):
                            print(f"{i + 1}. {enemy.enemy_type} (Salud: {enemy.health})")

                        target_input = input("Selecciona el número del enemigo: ")
                        if target_input.isdigit():  # Verifica si la entrada es un número
                            target_index = int(target_input) - 1
                        else:
                            print("Entrada inválida. Por favor, ingresa un número.")
                            continue  # Regresa al inicio del ciclo

                        if 0 <= target_index < len(enemies):
                            target = enemies[target_index]
                            damage = player.strength
                            target.take_damage(damage)
                            print(f"{player.name} ataca a {target.enemy_type} causando {damage} de daño.")
                            if not target.is_alive():
                                print(f"{target.enemy_type} ha sido derrotado.")
                                enemies.remove(target)
                            break  # Salir del ciclo si el ataque es exitoso
                        else:
                            print("Selección inválida. Por favor, selecciona un enemigo válido.")
                    break  # Salir del ciclo de acción si la acción es válida

                elif action == 2:
                    if player.has_items():  # Verifica si hay ítems disponibles
                        while True:  # Ciclo para permitir múltiples intentos de usar ítem
                            print("\nSelecciona un ítem para usar:")
                            for i, item in enumerate(player.items):
                                print(f"{i + 1}. {item.name}")

                            item_input = input("Selecciona el número del ítem: ")
                            if item_input.isdigit():  # Verifica si la entrada es un número
                                item_index = int(item_input) - 1
                            else:
                                print("Entrada inválida. Por favor, ingresa un número.")
                                continue  # Regresa al inicio del ciclo

                            if 0 <= item_index < len(player.items):
                                item = player.items[item_index]
                                item.effect(player)
                                print(f"{player.name} usa {item.name}.")
                                player.items.remove(item)
                                break  # Salir del ciclo si el ítem se usa correctamente
                            else:
                                print("Selección inválida. Intenta de nuevo.")
                    else:
                        print(f"{player.name} no tiene ítems. Debes atacar.")

                else:
                    print("Selección inválida. Intenta de nuevo.")

        # Verificar si los enemigos han sido derrotados
        if not enemies:
            print("¡Has ganado la batalla!")
            return True

        # Turno de los aliados
        for ally in allies:
            if ally.is_alive() and enemies:
                target = random.choice(enemies)
                damage = ally.strength
                target.take_damage(damage)
                print(f"{ally.name} ataca a {target.enemy_type} causando {damage} de daño.")
                if not target.is_alive():
                    print(f"{target.enemy_type} ha sido derrotado.")
                    enemies.remove(target)

        # Verificar si los enemigos han sido derrotados
        if not enemies:
            print("¡Has ganado la batalla!")
            
            return True

        # Turno de los enemigos
        for enemy in enemies:
            if enemy.is_alive():
                target = random.choice(allies + [player])
                damage = enemy.strength
                target.take_damage(damage)
                print(f"{enemy.enemy_type} ataca a {target.name} causando {damage} de daño.")
                if not target.is_alive():
                    print(f"{target.name} ha sido derrotado.")
                    allies.remove(target)

        # Verificar si todos los personajes han sido derrotados
        if not any(ally.is_alive() for ally in allies) and not player.is_alive():
            print("¡Has perdido la batalla!")
            return False
        