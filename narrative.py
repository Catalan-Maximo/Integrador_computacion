from constantes import INTRO_NARRATIVE, BATTLE_HISTORIES
class Narrative:
    def __init__(self):
        self.story = self.get_story()

    def get_story(self):
        return INTRO_NARRATIVE
    
    def get_battle_stories(self):
        return BATTLE_HISTORIES