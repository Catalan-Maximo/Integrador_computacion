import random 
import os 
import time 
from constantes import *


def turn_based_combat(player, allies, enemies):
    heroes = [player] + allies
    total_enemies = len(enemies)  # Cantidad total de enemigos
    
    # Bucle principal del combate
    while True:
        time.sleep(5)  # Pausa de 5 segundos entre turnos
        os.system('cls')

        # Turno del jugador
        if player.is_alive():
            while True:
                print(ACTIONSDIS)

                action_input = input(ACTIONINT)
                if action_input.isdigit():
                    action = int(action_input)
                else:
                    print(INVALIDENTRY_NUM)
                    time.sleep(2)
                    os.system('cls')
                    continue

                if action == 1:
                    while True:
                        os.system('cls')

                        team_health = ', '.join([f"{ally.name} (Salud: {ally.health})" for ally in allies if ally.health > 0])
                        print(f"\nLa vida de tu equipo es: {player.name} (Salud: {player.health}), {team_health}")

                        print(ENEMYDISP)
                        for i, enemy in enumerate(enemies):
                            print(f"{i + 1}. {enemy.name} (Salud: {enemy.health})")

                        target_input = input(SELECTENEMY)
                        if target_input.isdigit():
                            target_index = int(target_input) - 1
                        else:
                            print(INVALIDENTRY_NUM)
                            time.sleep(2)
                            os.system('cls')
                            continue

                        if 0 <= target_index < len(enemies):
                            target = enemies[target_index]
                            damage = player.strength  # Calcula el daño basado en la fuerza del jugador
                            target.take_damage(damage)
                            
                            # Verifica si el daño supera la defensa del enemigo
                            if damage - target.defense <= 0:
                                print(f"{player.name} ataca a {target.name} pero no logra hacer daño.")
                            else:
                                print(f"{player.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                            
                            if not target.is_alive():
                                print(f"{target.name} ha sido derrotado.")
                                enemies.remove(target)
                            break
                        else:
                            print(INVALIDENTRY_ENEMY)
                            time.sleep(2)
                            os.system('cls')
                    break

                elif action == 2:
                    os.system('cls')
                    if player.has_items():
                        while True:
                            print(ITEMSDISP)
                            for i, item in enumerate(player.items):
                                print(f"{i + 1}. {item.name}")

                            item_input = input(SELECTITEM)
                            if item_input.isdigit():
                                item_index = int(item_input) - 1
                            else:
                                print(INVALIDENTRY_NUM)
                                time.sleep(2)
                                os.system('cls')
                                continue

                            if 0 <= item_index < len(player.items):
                                item = player.items[item_index]
                                item.effect(player)
                                print(f"{player.name} usa {item.name}.")
                                
                                if item.name == 'Poción de Salud':
                                    print(f"Salud aumentada a {player.name} en 20. Ahora su salud es: {player.health}")
                                elif item.name == 'Amuleto de Fuerza':
                                    print(f"Fuerza aumentada a {player.name} en 5. Ahora su fuerza es: {player.strength}")
                                elif item.name == 'Escudo Mágico':
                                    print(f"Defensa aumentada a {player.name} en 5. Ahora su defensa es: {player.defense}")

                                player.items.remove(item)
                                break
                            else:
                                print(INVALIDENTRY)
                                time.sleep(2)
                                os.system('cls')
                    else:
                        print(f"{player.name} no tiene ítems. Debes atacar.")
                        time.sleep(2)
                        os.system('cls')

                else:
                    print(INVALIDENTRY)
                    time.sleep(2)
                    os.system('cls')

        # Verificar si todos los enemigos han sido derrotados
        if not enemies:
            print(WINCOMBAT)
            experiencia_ganada = 30 * total_enemies
            print(f"Has ganado {experiencia_ganada} puntos de experiencia.")
            player.add_experience(experiencia_ganada)
            return True

        # Turno de los aliados
        for ally in allies:
            if ally.is_alive() and enemies:  # Si el aliado está vivo y hay enemigos
                target = random.choice(enemies)
                damage = ally.strength
                target.take_damage(damage)
                if damage - target.defense <= 0:
                    print(f"{ally.name} ataca a {target.name} pero no logra hacer daño.")
                else:
                    print(f"{ally.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                if not target.is_alive():
                    print(f"{target.name} ha sido derrotado.")
                    enemies.remove(target)

        # Verificar si todos los enemigos han sido derrotados
        if not enemies:
            print(WINCOMBAT)
            experiencia_ganada = 30 * total_enemies
            print(f"Has ganado {experiencia_ganada} puntos de experiencia.")
            player.add_experience(experiencia_ganada)
            return True

        # Turno de los enemigos
        for enemy in enemies:
            # Verifica si todos los aliados y el jugador han sido derrotados
            if not any(ally.is_alive() for ally in allies) and not player.is_alive():
                return False
            elif enemy.is_alive():
                target = random.choice(heroes)
                damage = enemy.strength
                target.take_damage(damage)
                if damage - target.defense <= 0:
                    print(f"{enemy.name} ataca a {target.name} pero no logra hacer daño.")
                else:
                    print(f"{enemy.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                if not target.is_alive():
                    print(f"{target.name} ha sido derrotado.")
                    heroes.remove(target)

        # Verificar si todos los aliados y el jugador han sido derrotados
        if not any(ally.is_alive() for ally in allies) and not player.is_alive():
            return False  # Si todos están muertos, termina el combate
