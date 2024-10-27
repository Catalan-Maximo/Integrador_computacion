import random 
import os 
import time 
from constantes import *

# Función que gestiona el combate por turnos entre el jugador, aliados y enemigos
def turn_based_combat(player, allies, enemies):
    # Lista que agrupa al jugador y sus aliados
    heroes = [player] + allies
    total_enemies = len(enemies)  # Cantidad total de enemigos
    
    # Bucle principal del combate
    while True:
        time.sleep(5)  # Pausa de 5 segundos entre turnos
        os.system('cls')  # Limpia la pantalla (comando 'cls' es para Windows)

        # Turno del jugador
        if player.is_alive():  # Verifica si el jugador está vivo
            while True:
                print(ACTIONSDIS)  # Muestra las acciones disponibles (atacar, usar ítems, etc.)

                action_input = input(ACTIONINT)  # Entrada de acción del jugador
                if action_input.isdigit():  # Verifica si la entrada es un número
                    action = int(action_input)
                else:
                    print(INVALIDENTRY_NUM)  # Mensaje de entrada inválida
                    time.sleep(2)
                    os.system('cls')
                    continue  # Reinicia el ciclo si la entrada no es válida

                if action == 1:  # Si el jugador elige atacar
                    while True:  # Ciclo para repetir el ataque hasta que sea válido
                        os.system('cls')  # Limpia la pantalla

                        # Muestra la vida del equipo
                        team_health = ', '.join([f"{ally.name} (Salud: {ally.health})" for ally in allies if ally.health > 0])
                        print(f"\nLa vida de tu equipo es: {player.name} (Salud: {player.health}), {team_health}")
                        
                        # Muestra los enemigos disponibles para atacar
                        print(ENEMYDISP)
                        for i, enemy in enumerate(enemies):
                            print(f"{i + 1}. {enemy.name} (Salud: {enemy.health})")

                        # Entrada del jugador para seleccionar un enemigo
                        target_input = input(SELECTENEMY)
                        if target_input.isdigit():  # Verifica si la entrada es un número
                            target_index = int(target_input) - 1
                        else:
                            print(INVALIDENTRY_NUM)
                            time.sleep(2)
                            os.system('cls')
                            continue  # Reinicia el ciclo si la entrada no es válida

                        if 0 <= target_index < len(enemies):  # Verifica si el enemigo seleccionado es válido
                            target = enemies[target_index]
                            damage = player.strength  # Calcula el daño basado en la fuerza del jugador
                            target.take_damage(damage)  # El enemigo recibe el daño
                            
                            # Verifica si el daño supera la defensa del enemigo
                            if damage - target.defense < 0:
                                print(f"{player.name} ataca a {target.name} pero no logra hacer daño.")
                            else:
                                print(f"{player.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                            
                            if not target.is_alive():  # Si el enemigo es derrotado
                                print(f"{target.name} ha sido derrotado.")
                                enemies.remove(target)  # Elimina al enemigo de la lista
                            break  # Sale del ciclo de ataque
                        else:
                            print(INVALIDENTRY_ENEMY)
                            time.sleep(2)
                            os.system('cls')
                    break  # Sale del ciclo de selección de acciones si se realizó un ataque válido

                elif action == 2:  # Si el jugador elige usar un ítem
                    os.system('cls')
                    if player.has_items():  # Verifica si el jugador tiene ítems disponibles
                        while True:  # Ciclo para usar ítems
                            print(ITEMSDISP)
                            for i, item in enumerate(player.items):  # Muestra los ítems disponibles
                                print(f"{i + 1}. {item.name}")

                            item_input = input(SELECTITEM)
                            if item_input.isdigit():  # Verifica si la entrada es un número
                                item_index = int(item_input) - 1
                            else:
                                print(INVALIDENTRY_NUM)
                                time.sleep(2)
                                os.system('cls')
                                continue  # Reinicia el ciclo si la entrada no es válida

                            if 0 <= item_index < len(player.items):  # Verifica si el ítem seleccionado es válido
                                item = player.items[item_index]
                                item.effect(player)  # Aplica el efecto del ítem
                                print(f"{player.name} usa {item.name}.")
                                
                                # Mostrar el aumento del atributo correspondiente
                                if item.name == 'Poción de Salud':
                                    print(f"Salud aumentada a {player.name} en 20. Ahora su salud es: {player.health}")
                                elif item.name == 'Amuleto de Fuerza':
                                    print(f"Fuerza aumentada a {player.name} en 5. Ahora su fuerza es: {player.strength}")
                                elif item.name == 'Escudo Mágico':
                                    print(f"Defensa aumentada a {player.name} en 5. Ahora su defensa es: {player.defense}")

                                player.items.remove(item)  # Elimina el ítem usado del inventario
                                break  # Sale del ciclo si el ítem se usó correctamente
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
            print(WINCOMBAT)  # Mensaje de victoria
            experiencia_ganada = 30 * total_enemies  # Calcula la experiencia ganada (30 por enemigo)
            print(f"Has ganado {experiencia_ganada} puntos de experiencia.")
            player.add_experience(experiencia_ganada)  # Añade experiencia al jugador
            return True

        # Turno de los aliados
        for ally in allies:
            if ally.is_alive() and enemies:  # Si el aliado está vivo y hay enemigos
                target = random.choice(enemies)  # Elige un enemigo al azar
                damage = ally.strength  # Calcula el daño del aliado
                target.take_damage(damage)  # El enemigo recibe el daño
                if damage - target.defense < 0:
                    print(f"{ally.name} ataca a {target.name} pero no logra hacer daño.")
                else:
                    print(f"{ally.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                if not target.is_alive():  # Si el enemigo es derrotado
                    print(f"{target.name} ha sido derrotado.")
                    enemies.remove(target)  # Elimina al enemigo de la lista

        # Verificar si todos los enemigos han sido derrotados
        if not enemies:
            print(WINCOMBAT)  # Mensaje de victoria
            experiencia_ganada = 30 * total_enemies  # Calcula la experiencia ganada
            print(f"Has ganado {experiencia_ganada} puntos de experiencia.")
            player.add_experience(experiencia_ganada)  # Añade experiencia al jugador
            return True

        # Turno de los enemigos
        for enemy in enemies:
            # Verifica si todos los aliados y el jugador han sido derrotados
            if not any(ally.is_alive() for ally in allies) and not player.is_alive():
                return False
            elif enemy.is_alive():  # Si el enemigo está vivo
                target = random.choice(heroes)  # Elige un objetivo al azar (jugador o aliado)
                damage = enemy.strength  # Calcula el daño del enemigo
                target.take_damage(damage)  # El objetivo recibe el daño
                if damage - target.defense < 0:
                    print(f"{enemy.name} ataca a {target.name} pero no logra hacer daño.")
                else:
                    print(f"{enemy.name} ataca a {target.name} causando {damage - target.defense} de daño.")
                if not target.is_alive():  # Si el objetivo es derrotado
                    print(f"{target.name} ha sido derrotado.")
                    heroes.remove(target)  # Elimina al objetivo de la lista

        # Verificar si todos los aliados y el jugador han sido derrotados
        if not any(ally.is_alive() for ally in allies) and not player.is_alive():
            return False  # Si todos están muertos, termina el combate
