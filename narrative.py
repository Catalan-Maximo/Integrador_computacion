from constantes import INTRO
class Narrative:
    def __init__(self):
        self.story = self.get_story()

    def get_story(self):
        return INTRO
    
    def get_battle_stories(self):
        return [
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
                "║ decidirá si estás listo para enfrentarte al mal verdadero!     ║\n"
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
                "╔═══════════════════════════════════════════════════════════════╗\n"
                "║                         Sexta Batalla                         ║\n"
                "║ Después de la batalla final, cuando piensas que todo ha       ║\n"
                "║ terminado, el suelo tiembla y un enemigo aún más poderoso     ║\n"
                "║ emerge desde las profundidades. Esta será la batalla más      ║\n"
                "║ desafiante, con todas tus habilidades y recursos puestos a    ║\n"
                "║ prueba. ¡El destino del mundo está en tus manos!              ║\n"
                "╚═══════════════════════════════════════════════════════════════╝"
            ),
        ]