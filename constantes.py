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
INTRO_GAME = ("¡Bienvenido a este fantastico juego de rol!\n"
              "Creemos tu personaje y dejemoslo listo para la batalla"
              )
INTRO_NARRATIVE = (
        "╔════════════════════════════════════════════════════════════════╗\n"
        "║ Te encuentras al borde de una aventura épica. Tras días de     ║\n"
        "║ viajar a través de tierras oscuras, finalmente llegas a la     ║\n"
        "║ entrada de la legendaria Mazmorra de las Sombras, donde se     ║\n"
        "║ dice que el malvado jefe final aguarda.                        ║\n"
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
                "║ de enemigos acechando en la oscuridad. Sientes que esta batalla║\n"
                "║ será crucial para tu supervivencia. ¡No puedes darte el lujo   ║\n"
                "║ de fallar ahora!                                               ║\n"
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
                "║ Has llegado al punto culminante de tu aventura. Al final de    ║\n"
                "║ este corredor, el jefe final aguarda, observándote con una     ║\n"
                "║ sonrisa siniestra. Esta será la batalla que decidirá el destino║\n"
                "║ de todo lo que has luchado por proteger. ¡Es ahora o nunca!    ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
            (
                "╔════════════════════════════════════════════════════════════════╗\n"
                "║                         Sexta Batalla                          ║\n"
                "║ Te encuentras cara a cara con el temible jefe final: un Orco   ║\n"
                "║ colosal, cuya presencia imponente llena la sala. Su hacha,     ║\n"
                "║ forjada en las llamas del infierno, brilla con un resplandor   ║\n"
                "║ siniestro.                                                     ║\n"                    "║                                                                ║\n"
                "║ La batalla será feroz. Cada golpe que asestas resuena en las   ║\n"
                "║ paredes de la mazmorra, mientras el Orco contraataca con una   ║\n"
                "║ fuerza devastadora. ¡Prepárate para la lucha más intensa de tu ║\n"
                "║ vida!                                                          ║\n"
                "╚════════════════════════════════════════════════════════════════╝"
            ),
        ]
FINAL_NARRATIVE =  (
    "╔══════════════════════════════════════════════════════════════════╗\n"
    "║                         El Fin de la Aventura                    ║\n"
    "║ Tras una intensa lucha, el Orco colosal cae derrotado a tus pies.║\n"
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