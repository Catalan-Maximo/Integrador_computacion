# Constantes del juego
PLAYER_CLASSES = ['Guerrero', 'Mago', 'Arquero']
TEXT_PLAYER_SELECT = ("Bien, ahora selecciona la clase de tu personaje:\n"
        "1. Guerrero\n"
        "2. Mago\n"
        "3. Arquero")
ITEMS = ['Poción de Salud', 'Amuleto de Fuerza', 'Escudo Mágico']
DUNGEON1_ENEMIES = ['Goblin', 'Skeleton', 'Witch']
DUNGEON2_ENEMIES = ['Skeleton', 'Witch', 'Demon']
DUNGEON3_ENEMIES = ['Witch', 'Demon', 'Orc']
PLNAME_CREATOR = "Por favor, ingresa el nombre de tu personaje: "
CLASSSEL = "Selecciona el número de la clase: "
INVALIDSELPLAYER = "Selección inválida. Se asignará la clase Guerrero por defecto."
LOSECOMBAT = "¡Has perdido la batalla! Fin del juego."
WINCOMBAT = "¡Has ganado la batalla!"
INVALIDENTRY_NUM = "Entrada inválida. Por favor, ingresa un número válido."
INVALIDENTRY_ENEMY = "Selección inválida. Por favor, selecciona un enemigo válido."
INVALIDENTRY = "Selección inválida. Intenta de nuevo."
ACTIONSDIS = ("Acciones disponibles:\n"
            "1. Atacar\n"
            "2. Usar ítem")
ACTIONINT = "Introduce el número de la acción: "
ENEMYDISP = "\nEnemigos disponibles:"
SELECTENEMY = "Selecciona el número del enemigo para atacar: "
ITEMSDISP = "\nItems disponibles:"
SELECTITEM = "Selecciona el número del ítem: "
INTRO_GAME = ("¡Bienvenido a este fantastico juego de rol!\n"
              "Creemos tu personaje y dejemoslo listo para la batalla"
              )
INTRO_NARRATIVE = (
        "╔════════════════════════════════════════════════════════════════╗\n"
        "║ Te encuentras al borde de una aventura épica. Tras días de     ║\n"
        "║ viajar a través de tierras oscuras, finalmente llegas a la     ║\n"
        "║ entrada de la legendaria Cripta del Olvido, donde se           ║\n"
        "║ dice que reposan secretos antiguos y tesoros inimaginables,    ║\n"
        "║ pero también un peligro que ni siquiera los más valientes      ║\n"
        "║ han logrado enfrentar.                                         ║\n"
        "║                                                                ║\n"
        "║ Sin embargo, no estás solo. Mientras te preparas para entrar,  ║\n"
        "║ te encuentras con dos extraños, ambos con el mismo objetivo:   ║\n"
        "║ desafiar los peligros de la mazmorra y derrotar al mal.        ║\n"
        "║                                                                ║\n"
        "║ Decides unir fuerzas con ellos para tener una mayor oportunidad║\n"
        "║ de éxito. Juntos, se adentran en lo desconocido, cada paso     ║\n"
        "║ acercándolos a la batalla final.                               ║\n"
        "╚════════════════════════════════════════════════════════════════╝")
BATTLE_HISTORIES = [
            (
                "╔═══════════════════════════════════════════════════════════════╗\n"
                "║                         Primera Batalla                       ║\n"
                "║ Mientras exploras los oscuros pasillos de la mazmorra, te     ║\n"
                "║ enfrentas a tus primeros enemigos. Sientes que estos son solo ║\n"
                "║ los primeros obstáculos que desafiarán tu habilidad y valor.  ║\n"
                "║ ¡Es el momento de demostrar tu fuerza!                        ║\n"
                "╚═══════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔═══════════════════════════════════════════════════════════════╗\n"
                "║                         Segunda Batalla                       ║\n"
                "║ Tras tu primera victoria, los corredores de la mazmorra se    ║\n"
                "║ vuelven aún más oscuros y peligrosos. Los enemigos ahora      ║\n"
                "║ son más letales, y debes estar preparado para lo inesperado.  ║\n"
                "║ ¡Prepárate para una batalla aún más difícil!                  ║\n"
                "╚═══════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Tercera Batalla                        ║\n"
                "║ A medida que avanzas más profundamente en la mazmorra, los     ║\n"
                "║ ecos de tus pasos son seguidos por la presencia inquietante    ║\n"
                "║ de enemigos acechando en la oscuridad. Te adentras aún más en  ║\n"
                "║ los rincones más oscuros de la mazmorra. Esta batalla será     ║\n"
                "║ crucial para tu supervivencia. ¡No puedes darte el lujo de     ║\n"
                "║ fallar ahora!                                                  ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Cuarta Batalla                         ║\n"
                "║ Los desafíos continúan creciendo, y esta vez te enfrentas a un ║\n"
                "║ enemigo cuyo poder es abrumador. La mazmorra parece ponerse    ║\n"
                "║ en tu contra, y cada paso que das es un riesgo. ¡Esta batalla  ║\n"
                "║ pondrá a prueba tu valentía y habilidades!                     ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Quinta Batalla                         ║\n"
                "║ A medida que te adentras aún más en la mazmorra, el aire se    ║\n"
                "║ vuelve denso y opresivo. Los enemigos que enfrentas parecen    ║\n"
                "║ haber sido fortalecidos por la oscuridad. Cada batalla es más  ║\n"
                "║ peligrosa, y esta será decisiva para acercarte a tu objetivo.  ║\n"
                "║ ¡Es ahora o nunca!                                             ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Sexta Batalla                          ║\n"
                "║ Has llegado a una cámara vasta y oscura donde los secuaces del ║\n"
                "║ Orco final te esperan. Su presencia es intimidante, y sabes que║\n"
                "║ esta batalla es clave para debilitar al enemigo antes del      ║\n"
                "║ enfrentamiento final. ¡Lucha con todas tus fuerzas!            ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Batalla final                          ║\n"
                "║ Frente a ti se alza la última barrera entre tú y la salvación, ║\n"
                "║ el poderoso orco llamado 'Thrall, el Guardián de la Oscuridad'.║\n"
                "║ El destino de todo lo que has luchado por proteger está en     ║\n"
                "║ juego. Esta será tu mayor desafío.                             ║\n"
                "║ Cada movimiento cuenta, y el margen de error es inexistente.   ║\n"
                "║ Solo tu coraje y habilidad te llevarán a la victoria final.    ║\n"
                "║ ¡Prepárate para el combate!                                    ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            )
        ]

FINAL_NARRATIVE =  (
    "╔══════════════════════════════════════════════════════════════════╗\n"
    "║                         El Fin de la Aventura                    ║\n"
    "║ Tras una intensa lucha, el Gran Thrall cae derrotado a tus pies. ║\n"
    "║ La mazmorra, que antes resonaba con el eco de la batalla, ahora  ║\n"
    "║ se sumerge en un profundo silencio. La oscuridad que había       ║\n"
    "║ asolado estas tierras comienza a disiparse, y la luz de la       ║\n"
    "║ esperanza brilla con fuerza.                                     ║\n"
    "║                                                                  ║\n"
    "║ Tus aliados se reúnen a tu alrededor, celebrando la victoria y   ║\n"
    "║ agradeciéndote por haber liberado a la tierra de una amenaza     ║\n"
    "║ que la atormentaba. A medida que abandonas la mazmorra, el sol   ║\n"
    "║ comienza a brillar en el horizonte, iluminando el camino hacia   ║\n"
    "║ un futuro lleno de esperanza. Tu aventura ha llegado a su fin,   ║\n"
    "║ pero las historias de tus hazañas vivirán para siempre.          ║\n"
    "╚══════════════════════════════════════════════════════════════════╝"
)