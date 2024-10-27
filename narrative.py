from constantes import INTRO_NARRATIVE, BATTLE_HISTORIES

class Narrative:
    def __init__(self):
        self.story = self.get_story()  # Inicializa el atributo story llamando al método get_story

    def get_story(self):
        return INTRO_NARRATIVE  # Retorna la narrativa de introducción desde las constantes importadas
    
    def get_battle_stories(self):
        return BATTLE_HISTORIES  # Retorna las historias de batalla desde las constantes importadas
